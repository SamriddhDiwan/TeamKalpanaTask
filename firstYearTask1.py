from tkinter import *
from tkinter import ttk
import csv




with open('C:/Users/Samriddh Diwan/Downloads/Sample Data - Software Task - Data Sheet 1.csv') as data:
   num=csv.reader(data, delimiter=',')
   row=[]
   for k in data:
      row.append(k)
   del row[0]


root=Tk()
frame=Frame(root, width=850, height=800)
frame.grid(row=1,column=0)
telemetry= Label( root,text="TEAM KALPANA", font=("Arial bold", 15)).grid(row=0,column=0,padx=40,pady=20)



header=Text(frame)
header.place(x=0, y=0, height=800, width=850)
str_head="TEAM_ID"+str("%16s"%"MISSION_TIME")+str("%16s"%"PACKET_COUNT")+str("%15s"%"PACKET_COUNT")+str("%8s"%"MODE")+str("%20s"%"PAYLOAD_REALITY")+str("%12s"%"ALTITUDE")+str("%8s"%"TEMP")+str("%12s"%"VOLTAGE")
header.insert(INSERT,str(str_head))
header.tag_add("header", "1.0", "1.150")
header.tag_config("header",font=("Arial bold", 10))
header.insert(INSERT,"\n")


l=len(row)
def plot(n):
   header.delete(2.0,END)
   header.insert(INSERT,"\n")
   temp_row=[]
   for i in range(n+1):
      temp_row.append(row[i])
   for j in range(-1,-(n+2),-1):
      a=temp_row[j].split(",")
      strg=str(a[0])+str("%14s"%a[1])+str("%12s"%a[2])+str("%15s"%a[3])+str("%10s"%a[4])+str("%12s"%a[5])+str("%14s"%a[6])+str("%11s"%a[7])+str("%10s"%a[8])
      header.insert(INSERT,str(strg)) 
      header.insert(END,'\n')
   n+=1
   if n<l:
      root.after(1000,lambda: plot(n))
   
plot(0)
root.mainloop()