from tkinter import *
from tkinter import messagebox
from tkinter import ttk #Theme TTK


import csv
from datetime import datetime
#Database
from db_maintenace import * 

def writecsv(record_list):
    with open('data.csv','a',newline= '' ,encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)

GUI = Tk()
GUI.title('โปรแกรมซ่อมบำรุงของซ่อมไฟฟ้า')
GUI.geometry('1000x400+950+50')#x,y 
###############Font############### 
FONT1=('Angsana New',20,'bold')
FONT2=('Angsana New',15)

###############TAB############### 
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = Frame(Tab)
T5 = Frame(Tab)
T6 = Frame(Tab)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูใบแจ้งซ่อม')
Tab.add(T3,text='Spare')
Tab.add(T4,text='Spare')
Tab.add(T5,text='Spare')
Tab.add(T6,text='สรุป')
Tab.pack(fill=BOTH,expand=1)

#################################
L = Label(T1,text='โปรแกรมซ่อมบำรุง',font = FONT1)
L.place(x=80,y=10)
#L.pack() # อยู่บนสุด
'''L.place(x=5,y=1)
L.grid(row=0,column=0)

L = Label(T1,text=' คิว',font = ('Angsana New',40,'bold'))
L.grid(row=0,column=1)

'''
L = Label(T1,text='ชื่อ',font = FONT2)
L.place(x=30,y=50)
v_name = StringVar() # ตัวแปรพิเศษ T1
E1 = Entry(T1, textvariable=v_name,font=FONT2)
E1.place(x=150,y=50)
#------
L = Label(T1,text='แผนก',font = FONT2)
L.place(x=30,y=100)
v_department = StringVar()
E2 = Entry(T1, textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#------
L = Label(T1,text='เครื่อง',font = FONT2)
L.place(x=30,y=150)
v_machine = StringVar()
E3 = Entry(T1, textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#------
L = Label(T1,text='อาการเสีย',font = FONT2)
L.place(x=30,y=200)
v_problem = StringVar()
E4 = Entry(T1, textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)
#------
L = Label(T1,text='หมายเลข',font = FONT2)
L.place(x=30,y=250)
v_number = StringVar()
E5 = Entry(T1, textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#------
L = Label(T1,text='เบอร์โทร',font = FONT2)
L.place(x=30,y=300)
v_tel = StringVar()
E6 = Entry(T1, textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)

def save():
    name = v_name.get()
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง: '+ name + '\n'
    text = text + 'แผนก: '+ department + '\n'
    text = text + 'เครื่อง: '+ machine + '\n'
    text = text + 'อาการเสีย: '+ problem + '\n'
    text = text + 'หมายเลข: '+ number + '\n'
    text = text + 'เบอร์โทร: '+ tel + '\n'
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #Generate Transaction
    
    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S'))+114152147165)  #ทำให้โค้ดห้ามซ้ำ
    insert_mtworkorder(tsid, name, department, machine, problem, number, tel)
    v_name.set('')
    v_machine.set('')
    v_department.set('')
    v_number.set('')
    v_problem.set('')
    v_tel.set('')
    update_table()
    
    #datalist = [dt,name,department,machine,problem,number,tel]
    #writecsv(datalist) #logdata
    # messenger.sendtext(text)
    #messagebox.showinfo('กำลังบันทึกข้อมูล..',text)

B= Button(T1, text='บันทึกแจ้งซ่อม' , command = save)
B.place(x=200,y=350)


######################TAB2##############################
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']
headerw = [50,100,100,150,200,100,100]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtworkorderlist.pack()

for h,w in zip(header,headerw):
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w)

# mtworkorderlist.insert('','end',values=['A','B','C','D','E','F','G']) #EP2-7:40

def update_table():
    #mtworkorderlist.delete(*mtworkorderlist.get_children())  #ลบข้อมูลในตารางแสดงผลเก่า
    data = view_mtworkorder() #ต้อง import db_maintenace (database) 
    for d in data:
        d = list(d) #แปลง tuple () gxHo list [] ถึงจะลบบางข้อมูลได้
        del d[0] #ลบคอลัมแรกจาก database
        mtworkorderlist.insert('','end',values=d)
        mtworkorderlist.column(h,width=w,anchor='center')

    mtworkorderlist.column('TSID',anchor='e')

#########################START UP###############################
update_table()



GUI.mainloop()
#EP2-5-58