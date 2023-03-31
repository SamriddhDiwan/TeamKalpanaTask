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
my_frame = Frame(root)
root.title("TEAM KALPANA")




frame=Frame(root, width=850, height=800)
frame.grid(row=0,column=0)
header=Text(frame)
header.place(x=0, y=0, height=800, width=850)
header.insert(INSERT,"TEAM_ID"+"    "+"MISSION_TIME"+"    "+"PACKET_COUNT"+"    "+"PACKET_TYPE"+"    "+"MODE"+"    "+"PAYLOAD_REALITY"+"    "+"ALTITUDE"+"    "+"TEMP"+"    "+"VOLTAGE")
header.tag_add("header", "1.0", "1.150")
header.tag_config("header",font=("Arial bold", 10))
header.insert(INSERT,"\n")





l=len(row)




def plot(n):
	header.delete(2.0,END)
	header.insert(INSERT,"\n")
	for j in range(n+1):
		a=row[j].split(",")
		strg=str(a[0])+" "*6+str(a[1])+" "*12+str(a[2])+" "*12+str(a[3])+" "*6+str(a[4])+" "*13+str(a[5])+" "*10+str(a[6])+" "*10+str(a[7])+" "*4+str(a[8])
		header.insert(INSERT,strg) 
		header.insert(END,'\n')
		x=[]
	y=[]
	for i in range(n+1):
		a=row[i].split(",")
		y.append(float(a[6]))
		x.append(i)
	fig = Figure(figsize = (5, 5),dpi = 100)
	plot1 = fig.add_subplot(111)
	plot1.clear()
	plot1.plot(x,y)
	canvas = FigureCanvasTkAgg(fig,master = root)  
	canvas.draw()
	canvas.get_tk_widget().grid(row=0,column=1)
	n+=1
	if n<l:
		root.after(1000,lambda: plot(n))
	
plot(0)
root.mainloop()