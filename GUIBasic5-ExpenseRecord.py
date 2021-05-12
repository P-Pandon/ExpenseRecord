#GUIBasic1.py

from tkinter import * #import ทั้งหมดใน Tkinter,
from tkinter import ttk, messagebox #ttk = theme of Tk
import csv, time
from datetime import datetime


GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่ายของลุงข้างบ้าน_Version112')
GUI.geometry('600x650+0+0')  # 500x300 คือ ขนาด ui  +0+0 คือ ตำแหกน่งของ ui


# B1 = Button(GUI,text='DO NOT CLICK')
# B1.pack(ipadx=50, ipady=20 ) # .pack  คือ แปะปุ่มลง GUI หลัก

Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill='both', expand=True)

expenseIcon = PhotoImage(file = "Coin.png")
listicon = PhotoImage(file = "List.png")

Tab.add(T1, text='Add Expense',image=expenseIcon,compound='top')
Tab.add(T2, text='Expense List',image=listicon,compound='top')

F1 = Frame(T1)
F1.place(x=100, y=50)

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

mainImage = PhotoImage(file = "Wallet2.png")

ttk.Label(F1, image = mainImage).pack()


def Save(event=None):
    expense = v_expense.get()  #.get() คือการดึงค่ามาจาก v_expense = StringVar()
    price = v_price.get()
    quantity = v_quantity.get()

    if expense == '':
        print('No Date')
        massagebox.showwarning('Error','กรุณากรอกข้อมูลให้ถูกต้อง')
        return
    elif price == '':
        massagebox.showwarning('Error','กรุณากรอกราคา')
    elif quantity == '':
        quantity = 1
        

    total = float(price) * float(quantity)
    try:
        total = float(price) * float(quantity)
        print('รายการ: {} ราคา: {}'.format(expense,price))        
        print('จำนวน:{} รวมทั้งหมด: {} บาท'.format(quantity,total))
        text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
        text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
        v_total.set(text)

        v_expense.set('')
        v_price.set('')    #.set คือการเคลียร์ข้อมูลเก่าออก
        v_quantity.set('')
    
        today = datetime.now().strftime('%a')
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dt = days[today] + '-' + dt
        #บันทุกข้อมูลลง csv อย่าลืม import csv ด้วย
        with open('savedata.csv', 'a',encoding='utf-8',newline='') as f:
            #with คือสั่งเปิดไฟล์และปิดอัตโนมัติหลังทำงานเสร็จ
            # 'a' = append  คือการบันทึกข้อมูลเพิ่มจากข้อมูลเก่า
            #newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f) #สร้างฟังก์ชั่นสำหรับเขียนข้อมูล
            data = [dt,expense,price,quantity,total]
            fw.writerow(data)
            
        # ทำให้เคอเซอร์กลับไปตำแหน่งช่องเริ่่มต้น E1
        E1.focus()
        resulttable.delete(*resulttable.get_children())
        update_table()
        update_record()
    except:
        print('ERROR')
        messagebox.showerror('Error','กรุณากรอกตัวเลขให้ถูกต้อง')
        #messagebox.showwarning('Error','กรุณากรอกตัวเลขให้ถูกต้อง')
        #messagebox.showinfo('Error','กรุณากรอกตัวเลขให้ถูกต้อง')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')
    


# ทำให้สามารถกด enter = การกดปุ่ม Saveได้
GUI.bind('<Return>' ,Save) #ต้องเพิ่มใน def Save(event=None) ด้วย
            
    

Font1 = (None,20)  # none คือชื่่อฟ้อนท์ เช่น 'Angsana NEW'


#-----------Text1--------------

L = ttk.Label(F1,text='รายการ', font=Font1,).pack()
v_expense = StringVar() # StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI


E1 = ttk.Entry(F1, textvariable = v_expense, font = Font1)
E1.pack()
#------------------------------


#-----------Text2--------------

L = ttk.Label(F1,text='ราคา (บาท)', font=Font1).pack()
v_price = StringVar() # StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI



E2 = ttk.Entry(F1, textvariable = v_price, font = Font1)
E2.pack()
#------------------------------


#-----------Text3--------------

L = ttk.Label(F1,text='จำนวน (ชิ้้น)', font=Font1).pack()
v_quantity = StringVar() # StringVar() คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI


E3 = ttk.Entry(F1, textvariable = v_quantity, font = Font1)
E3.pack()
#------------------------------


#-----------Text4--------------

saveIcon = PhotoImage(file = "saveIcon.png")

B2 = ttk.Button(F1,text='Save',image = saveIcon, compound = 'left', command=Save)

B2.pack(padx=100, pady=30)

#L = ttk.Label(F1,text='รวมราคา', font=Font1).pack()
v_total = StringVar()
v_total.set('--------ผลลัพธ์--------')
total = ttk.Label(F1, textvariable=v_total,font=Font1,foreground='green')

total.pack(pady=20)

GUI.bind('<Tab>',lambda x: E2.Focus())

#E4 = ttk.Entry(F1, textvariable = v_total, font = Font1)
#E4.pack()
#------------------------------
#Tab2
def read_csv():
    with open('savedata.csv' ,newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data

def update_record():
    getdata = read_csv()
    v_allrecord.set('')
    text = ''
    for d in getdata:
        txt = '{}---{}---{}---{}---{}\n'.format(d[0],d[1],d[2],d[3],d[4],)
        text = text + txt

    v_allrecord.set(text)

v_allrecord = StringVar()
v_allrecord.set('-------All Record-------')
Allrecord = ttk.Label(T2,textvariable=v_allrecord,font=(None,15),foreground='green')
Allrecord.pack()

header = ['วัน-เวลา','รายการ','ราคา/หน่วย','จำนวน','รวม']
resulttable = ttk.Treeview(T2, columns=header, show='headings', height=10)
resulttable.pack()

for hd in header:
    resulttable.heading(hd,text=hd)

headerwidth = [150,170,80,80,80]
for hd,W in zip(header,headerwidth):
    resulttable.column(hd,width=W)

def update_table():
    getdata = read_csv()
    for dt in getdata:
        resulttable.insert('','end',value=dt)


#-------------------------------

def format_time():
    t = datetime.datetime.now()
    s = t.strftime('%Y-%m-%d %H:%M:%S.%f')
    return s[:-3]


class Clock:
    def __init__(self):
        self.time1 = ''
        self.time2 = time.strftime('%Y-%m-%d %H:%M:%S')
        self.mFrame = Frame()
        self.mFrame.pack(side=TOP,expand=NO,fill=X)

        self.watch = Label(self.mFrame, text=self.time2, font=('times',12,'bold'))
        self.watch.pack()

        self.changeLabel() #first call it manually

    def changeLabel(self): 
        self.time2 = time.strftime('%Y-%m-%d %H:%M:%S')
        self.watch.configure(text=self.time2)
        self.mFrame.after(200, self.changeLabel) #it'll call itself continuously

obj1 = Clock()

#----------------------------------

update_table()
update_record()

GUI.mainloop()  #ทำให้รันเช็คตลอดเวลา
