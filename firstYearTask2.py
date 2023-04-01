from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import csv


with open('C:/Users/Samriddh Diwan/Downloads/Sample Data - Software Task - Data Sheet 1.csv') as data:
   num=csv.reader(data, delimiter=',')
   row=[]
   for k in data:
      row.append(k)
   del row[0]


root=Tk()
telemetry= Label( root,text=" "*50+"TEAM KALPANA", font=("Arial bold", 30)).grid(row=0,column=0,padx=40,pady=20,columnspan=5)
space1= Label( root,text="   ").grid(row=1,column=0,padx=30)
telemetry= Label( root,text="TELEMETRY", font=("Arial bold", 25)).grid(row=1,column=1,padx=40,pady=20,columnspan=2)
space2= Label( root,text="   ").grid(row=1,column=4,padx=80)
grph= Label( root,text="ALTITUDE GRAPH", font=("Arial bold", 25)).grid(row=1,column=5,padx=40,pady=20,)

label1= Label( root,text="TEAM_ID        ", font=("Arial bold", 12)).grid(row=2,column=1,padx=20,pady=20)
label2= Label( root,text="MISSION_TIME   ", font=("Arial bold", 12)).grid(row=3,column=1,padx=20,pady=20)
label3= Label( root,text="PACKET_COUNT   ", font=("Arial bold", 12)).grid(row=4,column=1,padx=20,pady=20)
label4= Label( root,text="PACKET_TYPE    ", font=("Arial bold", 12)).grid(row=5,column=1,padx=20,pady=20)
label5= Label( root,text="MODE           ", font=("Arial bold", 12)).grid(row=6,column=1,padx=20,pady=20)
label6= Label( root,text="PAYLOAD_REALITY", font=("Arial bold", 12)).grid(row=7,column=1,padx=20,pady=20)
label7= Label( root,text="ALTITUDE       ", font=("Arial bold", 12)).grid(row=8,column=1,padx=20,pady=20)
label8= Label( root,text="TEMP           ", font=("Arial bold", 12)).grid(row=9,column=1,padx=20,pady=20)
label9= Label( root,text="VOLTAGE        ", font=("Arial bold", 12)).grid(row=10,column=1,padx=20,pady=20)


l=len(row)

def lifeChanger(i):

   a=row[i].split(",")

   value1= Label( root,text=str(a[0]), font=("Arial", 10))
   value1.grid(row=2,column=2,padx=100,pady=20)
   value2= Label( root,text=str(a[1]), font=("Arial", 10))
   value2.grid(row=3,column=2,padx=100,pady=20)
   value3= Label( root,text=str(a[2]), font=("Arial", 10))
   value3.grid(row=4,column=2,padx=100,pady=20)
   value4= Label( root,text=str(a[3]), font=("Arial", 10))
   value4.grid(row=5,column=2,padx=100,pady=20)
   value5= Label( root,text=str(a[4]), font=("Arial", 10))
   value5.grid(row=6,column=2,padx=100,pady=20)
   value6= Label( root,text=str(a[5]), font=("Arial", 10))
   value6.grid(row=7,column=2,padx=100,pady=20)
   value7= Label( root,text=str(a[6]), font=("Arial", 10))
   value7.grid(row=8,column=2,padx=100,pady=20)
   value8= Label( root,text=str(a[7]), font=("Arial", 10))
   value8.grid(row=9,column=2,padx=100,pady=20)
   value9= Label( root,text=str(a[8]), font=("Arial", 10))
   value9.grid(row=10,column=2,padx=100,pady=20)


   value1.config(text=str(a[0]))
   value2.config(text=str(a[1]))
   value3.config(text=str(a[2]))
   value4.config(text=str(a[3]))  
   value5.config(text=str(a[4]))
   value6.config(text=str(a[5]))
   value7.config(text=str(a[6]))
   value8.config(text=str(a[7]))
   value9.config(text=str(a[8]))

   x=[]
   y=[]
   for j in range(i+1):
      a=row[j].split(",")
      y.append(float(a[6]))
      x.append(j)
   fig = Figure(figsize = (5, 5),dpi = 100)
   plot1 = fig.add_subplot(111)
   plot1.clear()
   plot1.plot(x,y)
   canvas = FigureCanvasTkAgg(fig,master = root)  
   canvas.draw()
   canvas.get_tk_widget().grid(row=3,column=5,rowspan=9)



   i+=1
   if i<l:
      root.after(1000,lambda: lifeChanger(i))
lifeChanger(0)
root.mainloop()