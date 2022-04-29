import tkinter as tk
from tkinter import font as tkfont 
from tkinter import messagebox , scrolledtext , ttk
from tkinter import  *
import mysql.connector
from time import strftime
import os 
from datetime import datetime
from tkinter.filedialog import asksaveasfile
from mysql.connector import Error
#  config database
config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'app',
  'port':3306,
  'raise_on_warnings': True
}
# DATE   AND  TIME
def tmnow():
    now = datetime.now()
    gettime= str (now.strftime("%H:%M:%S") )
    return gettime
def daynow():
    now = datetime.now()
    nowday = str(now.day)
    nowmonth = str(now.month)
    years = int(now.year)
    calyear = int(years+543)
    getdate = f"{nowday}-{nowmonth}-{calyear}"
    return getdate
class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font','tomaho 10')
        #Main background
        self.bgpath  = os.path.join(os.path.dirname(__file__),'Asserts/main/main.png')
        self.bg = PhotoImage(file =self.bgpath)
        background = tk.Label(self,image =  self.bg)
        background.place(x=0,y=0)
        #buton user
        self.photo_user_path  = os.path.join(os.path.dirname(__file__),'Asserts/main/button/b_user.png')
        self.photo_user_B = PhotoImage(file =  self.photo_user_path )
        self.user_B = tk.Button(self,text = 'adduser'  ,image = self.photo_user_B , command = self.open_User_page,borderwidth = 0, highlightthickness=0,cursor="heart"  )
        self.user_B.place(x= 50 , y = 350)
        #button stock
        self.photo_stock_path  = os.path.join(os.path.dirname(__file__),'Asserts/main/button/b_stock.png')
        self.photo_stock_B = PhotoImage(file = self.photo_stock_path)
        self.stock_B = tk.Button(self,text = 'stock'  ,image = self.photo_stock_B ,  command = self.open_Stock_page,borderwidth = 0, highlightthickness=0,cursor="heart")
        self.stock_B.place(x= 300 , y = 350)
        #button order
        self.photo_user_path  = os.path.join(os.path.dirname(__file__),'Asserts/main/button/b_cart.png')
        self.photo_order_B = PhotoImage(file =self.photo_user_path)
        self.order_B = tk.Button(self,text = 'Order'  , image = self.photo_order_B , command = self.open_Order_page ,borderwidth = 0, highlightthickness=0 ,cursor="heart")
        self.order_B.place(x= 300 , y = 500)

        self.bill_path  = os.path.join(os.path.dirname(__file__),'Asserts/main/button/b_bill.png')
        self.photo_bill_B = PhotoImage(file =self.bill_path)
        self.Bill_B = tk.Button(self,text = 'Bill' ,borderwidth = 0, highlightthickness=0, image = self.photo_bill_B  ,cursor="heart" , command = self.open_Bill_page)
        self.Bill_B.place(x= 50 , y = 500)

        #time Label
        date = tk.Label(self, font = ('calibri', 14, 'bold'),background = 'white',foreground = 'black' , cursor = "heart")
        date.place(x = 68 , y = 30 )
        def time():   # create fuctuin time
            string = strftime('%H:%M:%S %p')
            date.config(text = string)
            date.after(1000, time)
        time()   #call fuction time    
    #fuction open_page_button
    def open_User_page(self):   #config User_page
        User = User_page(self)
        User.protocol("WM_DELETE_WINDOW", lambda x=User: on_closing(x))
        self.user_B['state'] = DISABLED
        def on_closing(window):
            self.user_B['state'] = ACTIVE
            User.destroy()
    def open_Stock_page(self):       # config Stock_page
        Stock = Stock_page(self)
        Stock.protocol("WM_DELETE_WINDOW", lambda x=Stock: close_stock_page(x))
        self.stock_B['state'] = DISABLED
        def close_stock_page(window):
            self.stock_B['state'] =ACTIVE
            Stock.destroy()
    def open_Order_page(self):    # config Order_page
        Order = Order_page(self)
        Order.protocol("WM_DELETE_WINDOW", lambda x=Order: close_order_page(x))
        self.order_B['state'] = DISABLED
        def close_order_page(window):
            self.order_B['state'] = ACTIVE
            Order.destroy()
    def open_Bill_page(self):
        Bill = Bill_Page(self)
        Bill.protocol("WM_DELETE_WINDOW", lambda x=Bill: close_bill_page(x))
        self.Bill_B['state'] = DISABLED
        def close_bill_page(window):
            self.Bill_B['state'] = ACTIVE
            Bill.destroy()
class User_page(tk.Toplevel):
    def __init__(self, user ):
        super().__init__(user )
        self.geometry('600x640')
        self.title('จัดการผู้ใช้')
        self.resizable(False, False)

        #Frame userpage
        self.frameuser = Frame(self)
        self.frameuser.pack()
        self.frame_tv_user = Frame(self, width = 600 ,  heigh = 600 ,bg ='pink' ) #Frame
        self.frame_tv_user.pack()
        self.frameuser2 = LabelFrame(self , text ="" ,padx = 5 , pady = 5 )
        self.frameuser2.pack()
        self.frameuser3 = LabelFrame(self , text = "สมัครสมาชิก" , padx  = 5 , pady = 5)
        self.frameuser3.pack()

        self.nonelabel = tk.Label(self.frameuser,text='').grid(row=0,column=0)
        Laorder_name =  tk.Label(self.frameuser , text ="ค้นหา" ).grid(row = 1 ,  column  = 0  )
        self.fake_user_combo = ttk.Combobox(self.frameuser).grid(row = 1 , column = 1 )

        search_order_b = tk.Button(self.frameuser, text = "ค้นหา",command = self.consearchuser).grid(row = 1 , column = 2)
        self.typeorderuserp = StringVar(None,'0')
        select1 = tk.Radiobutton(self.frameuser, text="ค้นหาด้วยชื่อ", variable= self.typeorderuserp , value='NAME' , command =  self.Search_user_p  )
        select1.grid(row = 2 , column = 0)
        select2 = tk.Radiobutton(self.frameuser, text="ค้นหาด้วยเบอร์", variable= self.typeorderuserp , value='PHONE' , command =  self.Search_user_p )
        select2.grid(row = 2 ,column = 1)
         #buton user
        #self.photo_user_B = PhotoImage(file = "Asserts/main/button/b_user.png")
        self.useredit_B = tk.Button(self.frameuser2,text = 'แก้ไข', command = self.check_Page_update_user  )
        self.useredit_B.grid(row = 0 , column = 1 , padx = 5)
        self.userdelete_B = tk.Button(self.frameuser2,text = 'ลบ'  , command = self.check_delete_user)
        self.userdelete_B.grid(row = 0 , column = 2 , padx = 5)

        self.userclear_B = tk.Button(self.frameuser3,text = 'เคลียร์'  , command =  self.user_clear,width=10)
        self.userclear_B.grid(row = 6 , column = 1 , padx = 5)

        #treeview_User
        self.user_scroll = Scrollbar(self.frame_tv_user)   #Scroll
        self.user_scroll.pack(side = RIGHT,fill=Y)
        self.tv_user= ttk.Treeview(self.frame_tv_user, yscrollcommand=self.user_scroll.set) #command Scroll
        self.user_scroll.config(command = self.tv_user.yview)
        self.tv_user['columns']=('ID' ,  'Name', 'Phone'  , 'Sex' , 'Address')   
        self.tv_user.column('#0', width=0, stretch=NO)
        self.tv_user.column('ID', anchor=CENTER, width= 80)
        self.tv_user.column('Name', anchor=CENTER, width=200)
        self.tv_user.column('Phone', anchor=CENTER, width= 100)
        self.tv_user.column('Sex', anchor=CENTER, width= 50)
        self.tv_user.column('Address', anchor=CENTER, width= 100)
        
        # head table_ User
        self.tv_user.heading('#0', text='', anchor=CENTER)
        self.tv_user.heading('ID', text='ID', anchor=CENTER)
        self.tv_user.heading('Name', text='ชื่อลูกค้า', anchor=CENTER)
        self.tv_user.heading('Phone', text='เบอร์', anchor=CENTER)
        self.tv_user.heading('Sex', text='เพศ', anchor=CENTER)
        self.tv_user.heading('Address', text='ที่อยู่', anchor=CENTER)
        self.tv_user.pack(side ='left')
 
        # call fuction display tree view
        self.viewuser()

        # insert
        name = tk.Label(self.frameuser3 ,text = "ชื่อ").grid(row = 0 , column  = 0)
        lasex_user = tk.Label(self.frameuser3 , text = "เพศ").grid(row = 1 ,column = 0)
        self.var = StringVar(None,'0')  #RADIO SELECT_USER
        select1 = tk.Radiobutton(self.frameuser3, text="Male", variable= self.var , value='M' )
        select1.grid(row = 1 , column = 1)
        select2 = tk.Radiobutton(self.frameuser3, text="Female", variable= self.var , value='F' )
        select2.grid(row = 1 , column = 2)
        laphone_user = tk.Label(self.frameuser3).grid(row = 2 ,column = 0)
        phone = tk.Label(self.frameuser3 ,text = "เบอร์โทรศัพท์").grid(row = 2 , column = 0)
        self.phone_in = tk.Entry(self.frameuser3)
        self.name_in = tk.Entry(self.frameuser3)
        self.name_in.grid(row =  0 , column = 1 )
        self.phone_in.grid(row = 2 , column = 1)
        self.teeyou = tk.Label(self.frameuser3,text="ที่อยู่")
        self.teeyou.grid(row=4,column=0)

        self.address_in = tk.Text(self.frameuser3, width = 30 , height = 5 )
        self.address_in.grid(row = 4 , column = 1 , pady = 10)

        self.useradd_B = tk.Button(self.frameuser3,text = 'เพิ่ม' , command  = self.insert_user ,width=10 )
        self.useradd_B.grid(row  = 5 ,column  = 1 , padx = 5 )
        
    #fuction USer Page
    def viewuser(self):
        con = mysql.connector.connect(**config)
        cur = con.cursor()
        cur.execute("select * from customer" )
        user_view = cur.fetchall()
        for Del in self.tv_user.get_children():
            self.tv_user.delete(Del)
        for row_user in user_view:
            self.tv_user.insert("",'end' ,iid = row_user[0] , values = (row_user[0] ,row_user[1]  , row_user[2] , row_user[4] ,row_user[3]))
        con.close()
    # update_page User
    def check_Page_update_user(self):
        check_update_user = list( [self.tv_user.focus()] )
        if check_update_user[0] == '':
            messagebox.showerror("Error", "โปรดเลือกข้อมูลในตาราง")
        else:
            self.Page_update_user()

    def check_delete_user(self):
        check_delete_user = list( [self.tv_user.focus()] )
        if check_delete_user[0] == '':
            messagebox.showerror("Error", "โปรดเลือกข้อมูลในตาราง")
        else:
            self.delete_user()
    def Page_update_user(self):
        self.update_userp = tk.Toplevel()
        self.update_userp.geometry('400x250')
        self.update_userp.resizable(False,False)
        self.update_userp.title('อัพเดตข้อมูลผู้ใช้')

        self.Frameup = LabelFrame(self.update_userp , padx = 10 , pady = 10 , text = "แก้ไขข้อมูลผู้ใช้")
        self.Frameup.pack()
        laup_name =  tk.Label(self.Frameup , text = "ชื่อ").grid(row = 0 , column = 0 , padx =5 , pady = 5)
        self.name_field = tk.Entry(self.Frameup)
        self.name_field.grid(row = 0 , column = 1)
        laup_phone = tk.Label(self.Frameup  , text = "เบอร์โทรศัพท์"  , pady = 5 ).grid(row = 1  , column = 0 , padx = 5)
        self.phone_user = tk.Entry(self.Frameup)
        self.phone_user.grid(row = 1 , column = 1)
        self.varupdate = StringVar(None,'0')  #RADIO SELECT_USER
        select1 = tk.Radiobutton(self.Frameup, text="Male", variable= self.varupdate , value='M' )
        select1.grid(row = 2 , column = 0)
        select2 = tk.Radiobutton(self.Frameup, text="Female", variable= self.varupdate , value='F' )
        select2.grid(row = 2 , column = 1)
        self.ID_update = tk.Entry(self.Frameup )
        self.update_userp.grab_set()
        self.addupdatelabel = tk.Label(self.Frameup,text='ที่อยู่')
        self.addupdatelabel.grid(row=3,column=0)
        self.address_user = tk.Text(self.Frameup ,width=20 ,height = 5 )
        self.address_user.grid(row=3,column=1)

        self.concernbtn = tk.Frame(self.update_userp)
        self.concernbtn.pack()
        self.userupdate_B = tk.Button(self.concernbtn,text = 'ยืนยัน'  , command = self.update)
        self.userupdate_B.pack()
        self.update_user()
    def update_user(self):
        self.name_field.delete(0,END)
        self.phone_user.delete(0,END)
        self.ID_update.delete(0,END)
        self.address_user.delete("1.0","end")
        selected_user = list( [self.tv_user.focus()] )
        values_user = self.tv_user.item(selected_user,"values")
        self.ID_update.insert(0,values_user[0])
        self.name_field.insert(0,values_user[1])
        self.phone_user.insert(0,values_user[2])
        self.address_user.insert (INSERT,values_user[4])
        ID = self.ID_update.get()
        name = self.name_field.get()
        phone = self.phone_user.get()
        address = self.address_user.get("1.0",END)
    def update(self):
        con = mysql.connector.connect(**config)
        cur = con.cursor()
        sexcheck = self.varupdate.get()
        try:
            if self.phone_user.get().isdigit() and sexcheck != '0': 
                cur.execute("UPDATE customer set  NAME_USER=%s ,ADDRESS_USER=%s, PHONE_USER=%s  , SEX_USER=%s where ID_USER=%s",
                (self.name_field.get() , self.address_user.get("1.0",END) , self.phone_user.get()  ,self.varupdate.get() , self.ID_update.get()  ))
                con.commit()
                self.viewuser()
                self.update_userp.destroy()
                messagebox.showinfo("เสร็จสิ้น", "ข้อมูลอัพเดทเรียบร้อย")
            else:
                con.close()
                messagebox.showinfo("ผิดพลาด", "ตรวจดูข้อมูลซ่้ำหรือใส่ข้อมูลให้ถูกต้อง")
        except Exception as E:
            messagebox.showinfo("ผิดพลาด", "กรุณากรอกข้อมูลให้ครบและถูกต้อง")
            print(E)
    def insert_user(self):
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        try:
            selection  = str(self.var.get() ) 
            result_namein = self.name_in.get()
            result_addressin = self.address_in.get("1.0",END)
            result_phone  = self.phone_in.get()
            if self.phone_in.get().isdigit(): 
                cursor.execute("INSERT INTO customer(NAME_USER,ADDRESS_USER,PHONE_USER , SEX_USER)VALUES(%s,%s,%s,%s)"
                ,(result_namein,result_addressin,result_phone,selection))
                con.commit()
                con.close()
                self.viewuser()
                self.user_clear()
                messagebox.showinfo("แสดงผล", "ข้อมูลผู้ใช้ได้ถูกบันทึกไว้แล้ว")
            else:
                con.close()
                messagebox.showinfo("ผิดพลาด", "ตรวจดูข้อมูลซ่้ำหรือใส่ข้อมูลให้ถูกต้อง")
        except Exception as Error:
            messagebox.showinfo("ผิดพลาด", "ตรวจดูข้อมูลซ่้ำหรือใส่ให้ถูกต้อง")
            print(Error)
            
    def delete_user(self):
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        selected_user = list( [self.tv_user.focus()] )
        values_user = self.tv_user.item(selected_user,"values")
        #print(values_user)
        sql = "delete from customer where ID_USER = %s "
        cursor.execute(sql,selected_user)
        con.commit()
        self.viewuser()
    def user_clear(self):
        self.phone_in.delete(0,END)
        self.name_in.delete(0,END)
        self.address_in.delete("1.0","end")
        self.var.set(None)
        
    # sql Combobox 
    def Search_user_p(self):
        s_cu = self.typeorderuserp.get()
        if s_cu =='NAME' :
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            query = "SELECT NAME_USER  from  customer;"
            cursor.execute(query)
            rowuser = [item[0] for item in cursor.fetchall()]
            self.userorder = (rowuser)
            self.combosearch_user()
        elif s_cu == 'PHONE':
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            query2 = "SELECT PHONE_USER  from  customer;"
            cursor.execute(query2)
            rowuser2 = [item[0] for item in cursor.fetchall()]
            self.userorder = (rowuser2)
            self.combosearch_user()
    def event_searchuser(self,event):
        value = event.widget.get()
        if value == '':
            self.search_ug['value'] = self.userorder
        else:
            data = [ ]
            for item in self.userorder:
                if value.lower() in item.lower( ):
                    data.append(item)
                self.search_ug['value'] = data
    def combosearch_user(self):
        self.search_ug = ttk.Combobox(self.frameuser , value = self.userorder)
        self.search_ug.grid(row = 1 , column = 1)
        self.search_ug.bind('<KeyRelease>',self.event_searchuser)
    def consearchuser(self):
        try:
            Ut =  self.typeorderuserp.get()
            currentSuser =self.search_ug.get()
            if Ut == 'NAME':
                con = mysql.connector.connect(**config)
                cursor = con.cursor()
                like1 = f"""SELECT * FROM customer WHERE NAME_USER like '%{currentSuser}%' """
                cursor.execute(like1)
                userlikename = cursor.fetchall() 
                for Del in self.tv_user.get_children():
                    self.tv_user.delete(Del)
                for row_user in userlikename:
                    self.tv_user.insert("",'end' ,iid = row_user[0] , values = (row_user[0] ,row_user[1]  , row_user[2] , row_user[4] ,row_user[3]))
                con.close()
            elif Ut =='PHONE':
                con = mysql.connector.connect(**config)
                cursor = con.cursor()
                like2 = f"""SELECT * FROM customer WHERE PHONE_USER like '%{currentSuser}%' """
                cursor.execute(like2)
                userlikename2 = cursor.fetchall() 
                for Del in self.tv_user.get_children():
                    self.tv_user.delete(Del)
                for row_user2 in userlikename2:
                    self.tv_user.insert("",'end' ,iid = row_user2[0] , values = (row_user2[0] ,row_user2[1]  , row_user2[2] , row_user2[4] ,row_user2[3]))
                con.close()
        except Exception :
            messagebox.showerror("Error","กรุณาเลือกประเภทการค้นหา")
class Stock_page(tk.Toplevel):
    def __init__(self,stock):
        super().__init__(stock)
        self.geometry('600x600')
        self.title('จัดการสินค้า')
        self.resizable(False,False)
       #search

       #Frame Stock
        self.frameorder = Frame(self,pady=15)
        self.frameorder.pack()
        frame_tv_stock = Frame(self , width = 600 ,  heigh = 600 ,bg ='pink' ) #Frame
        frame_tv_stock.pack()
        self.framemenu = Frame(self , width = 600 ,  heigh = 600) #Framemenu
        self.framemenu.pack()
        self.frame1 = tk.LabelFrame(self.framemenu , text = "ข้อมูลสินค้า" , padx = 10 , pady = 5)
        self.frame1.grid(row=0,column=0)
        self.frame2 = tk.LabelFrame(self.framemenu ,text= "เมนู" , padx = 10 , pady = 5)
        self.frame2.grid(row=1,column=0)
        self.frame3 = tk.LabelFrame(self.framemenu,text="เรียงลำดับ", padx = 10 , pady = 5)
        self.frame3.grid(row=0,column=1,sticky='N')

        Laorder_name =  tk.Label(self.frameorder , text ="ค้นหา" ).grid(row = 0 ,  column  = 0  )
        self.fake_frame_stock = ttk.Combobox(self.frameorder).grid(row = 0 , column = 1,padx=5)
        search_order_b = tk.Button(self.frameorder, text = "ค้นหา" , command = self.confirmsqlstock ).grid(row = 0 , column = 2)
        self.typeorder = StringVar(None,'0')
        select1 = tk.Radiobutton(self.frameorder, text="ชื่อสินค้า", variable= self.typeorder , value='NAMESTOCK' ,command = self.sqlStock)
        select1.grid(row = 1 , column = 0)
        select2 = tk.Radiobutton(self.frameorder, text="ประเภท", variable= self.typeorder , value='TYPESTOCK'  ,command = self.sqlStock)
        select2.grid(row = 1 ,column = 1)
        search_order_b = tk.Button(self.frame3, text = "เรียงสต๊อกน้อยไปมาก" , command = self.orderascstock).grid(row = 1 , column = 2 , padx = 5 , pady = 5)
        search_order_b = tk.Button(self.frame3, text = "เรียงสต๊อกมากไปน้อย" , command = self.orderdescstock).grid(row = 1 , column = 3, padx = 5 , pady = 5)
        #treeview
        
        self.stock_scroll = Scrollbar(frame_tv_stock)   #Scroll
        self.stock_scroll.pack(side = RIGHT,fill=Y)
        self.tv_stock= ttk.Treeview(frame_tv_stock, yscrollcommand=self.stock_scroll.set) #command Scroll
        self.stock_scroll.config(command = self.tv_stock.yview)
        self.tv_stock['columns']=('ID' ,  'Name', 'Qty'  , 'Type' , 'Unit')   
        self.tv_stock.column('#0', width=0, stretch=NO)
        self.tv_stock.column('ID', anchor=CENTER, width= 80)
        self.tv_stock.column('Name', anchor=CENTER, width=200)
        self.tv_stock.column('Qty', anchor=CENTER, width= 100)
        self.tv_stock.column('Type', anchor=CENTER, width= 50)
        self.tv_stock.column('Unit', anchor=CENTER, width= 100)
        
        # head table_ User
        self.tv_stock.heading('#0', text='', anchor=CENTER)
        self.tv_stock.heading('ID', text='รหัสสินค้า', anchor=CENTER)
        self.tv_stock.heading('Name', text='ชื่อสินค้า', anchor=CENTER)
        self.tv_stock.heading('Qty', text='จำนวนที่มี', anchor=CENTER)
        self.tv_stock.heading('Type', text='ประเภท', anchor=CENTER)
        self.tv_stock.heading('Unit', text='ราคาต่อหน่วย', anchor=CENTER)
        self.tv_stock.pack(side ='left')

        #Label frame
        Labelstock = tk.Label(self.frame1 , text = "ไอดีสินค้า" , pady = 5 ).grid(row = 0 , column = 0)
        Lanamestock = tk.Label(self.frame1 , text = "ชื่อสินค้า" , pady = 5 ).grid(row = 1 , column = 0)
        Laqtystock = tk.Label(self.frame1 , text = "จำนวน", pady = 5).grid(row = 2 , column = 0)
        Latypestock = tk.Label(self.frame1,text = "ประเภท", pady = 5).grid(row = 3 , column = 0)
        Launitstock = tk.Label(self.frame1 , text = "ราคา", pady = 5).grid(row = 4 , column = 0)
        self.idstock_in = tk.Entry(self.frame1  )
        self.idstock_in.grid(row = 0 , column =1 )
        self.namestock_in = tk.Entry(self.frame1)
        self.namestock_in.grid(row = 1,  column = 1 )
        self.qtystock_in = tk.Entry(self.frame1 )
        self.qtystock_in.grid(row = 2 , column = 1)
        self.typestock_in = ttk.Combobox(self.frame1)
        self.typestock_in['values'] = ('Food', 'Water')
        self.typestock_in['state'] = 'readonly'
        self.typestock_in.grid(row = 3 , column = 1)
        self.unitstock_in = tk.Entry(self.frame1)
        self.unitstock_in.grid(row = 4 , column = 1)
        self.tag_stock = tk.Entry(self.frame1)
        self.display_stock() #call fuction display stock
        #Labelself.frame2
        self.ok_stock = tk.Button(self.frame2 , text = "เพิ่ม" , command = self.insert_stock ).pack(side = "left" , padx = 5 )
        self.update_stock = tk.Button(self.frame2 , text = "เลือก" , command = self.select_stock ).pack(side = "left" , padx = 5)
        self.select_stock_b = tk.Button(self.frame2 , text = "แก้ไข"  , command = self.updatenew_stock).pack(side = "left" , padx = 5)
        self.del_stock = tk.Button(self.frame2 , text = "ลบ"  , command = self.del_stock).pack(side = "left" , padx = 5 )
        self.clear_stock = tk.Button(self.frame2 , text = "เคลียร์" , command = self.clear_input_stock ).pack(side = "right" , padx = 5 )
    #fuction_stock
    def display_stock(self):
        con = mysql.connector.connect(**config)
        cur = con.cursor()
        cur.execute("select * from part" )
        stock_view = cur.fetchall()
        for Del in self.tv_stock.get_children():
            self.tv_stock.delete(Del)
        for row_stock in stock_view:
            self.tv_stock.insert("",'end' ,iid = row_stock[0] , values = (row_stock[0] ,row_stock[1]  , row_stock[2] , row_stock[3] ,row_stock[4] ))
        con.close()
    def clear_input_stock(self):
        result_idstock = self.idstock_in.delete(0, END)
        result_namestock = self.namestock_in.delete(0, END)
        result_qtystock  = self.qtystock_in.delete(0, END)
        result_typestock  = self.typestock_in.delete(0, END)
        result_unitstock  = self.unitstock_in.delete(0, END)
    def insert_stock(self):
        result_idstock = self.idstock_in.get()
        result_namestock = self.namestock_in.get()
        result_qtystock  = self.qtystock_in.get()
        result_typestock  = self.typestock_in.get()
        result_unitstock  = self.unitstock_in.get()
        try:
            if self.unitstock_in.get().isdigit() and self.qtystock_in.get().isdigit(): 
                con = mysql.connector.connect(**config)
                cursor = con.cursor()
                cursor.execute("INSERT INTO part(PART_ID,PART_NAME,QTY_PART, TYPE_PART , UNIT_PART )VALUES(%s,%s,%s,%s,%s)"
                ,(result_idstock  ,  result_namestock  ,    result_qtystock   ,  result_typestock   ,   result_unitstock  ))
                con.commit()
                self.display_stock()
                self.clear_input_stock()
                messagebox.showinfo("เสร็จสิ้น", "บันทึกข้อมูลเสร็จสิ้น")
            else:
                messagebox.showinfo("ผิดพลาด", "ตรวจดูข้อมูลซ่้ำหรือใส่ข้อมูลให้ถูกต้อง")
        except Exception as Error:
            print(Error)
    def select_stock(self):
        try:
            self.clear_input_stock()
            self.tag_stock.delete(0,END)
            selected_stock = list( [self.tv_stock.focus()] )
            values_stock = self.tv_stock.item(selected_stock,"values")
            self.idstock_in.insert(0,values_stock[0])
            self.namestock_in.insert(0,values_stock[1])
            self.qtystock_in.insert(0,values_stock[2])
            self.typestock_in.insert(0,values_stock[3])
            self.unitstock_in.insert(0,values_stock[4])
            #selected_stock.clear()
            result_tag = list ( [self.idstock_in.get()] )
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            cursor.execute("SELECT TAG_PART  FROM part WHERE PART_ID  = %s"  ,  (result_tag ) )
            test_view = cursor.fetchall()
            self.tag_stock.insert(0,test_view)
            con.close()
        except Exception as E:
            messagebox.showinfo("ผิดพลาด", "เลือกข้อมูลจากตารางก่อนแก้ไขข้อมูล")
    def updatenew_stock(self):
        result_idstock = self.idstock_in.get()
        result_namestock = self.namestock_in.get()
        result_qtystock  = self.qtystock_in.get()
        result_typestock  = self.typestock_in.get()
        result_unitstock  = self.unitstock_in.get()
        result_tag = self.tag_stock.get()
        if result_typestock == '':
            messagebox.showinfo("Error", "เลือกประเภทสินค้าที่จะทำการแก้ไข")
        else:
            con = mysql.connector.connect(**config)
            cur = con.cursor()
            cur.execute("UPDATE part set  PART_ID=%s , PART_NAME=%s, QTY_PART=%s  , TYPE_PART = %s , UNIT_PART = %s where TAG_PART=%s ",
            ( result_idstock ,  result_namestock , result_qtystock  , result_typestock , result_unitstock  ,  result_tag  ))
            con.commit()
            self.display_stock()
            self.clear_input_stock()
            self.tag_stock.delete(0,END)
    def del_stock(self):
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        selected_stock = list( [self.tv_stock.focus()] )
        if selected_stock[0] == '':
            messagebox.showinfo("Error", "เลือกประเภทสินค้าที่จะทำการลบ")
        else:
            values_stock = self.tv_stock.item(selected_stock,"values")
            sql = "delete from part where PART_ID = %s "
            cursor.execute(sql,selected_stock)
            con.commit()
            self.display_stock()
            #SQL SEARCH COMBOBOX
    def StockEventsearch(self,event):
        value = event.widget.get()
        if value == '':
            self.search_order['value'] = self.usestock
        else:
            data = [ ]
            for item in self.usestock:
                if value.lower() in item.lower( ):
                    data.append(item)
                self.search_order['value'] = data
    def sqlStock(self):
        order_type = self.typeorder.get()
        if order_type =='NAMESTOCK':
            con  = mysql.connector.connect(**config)
            cursor = con.cursor()
            query = "SELECT PART_NAME From part;"
            cursor.execute(query)
        #row = cursor.fetchall()
            StockSresult = [item[0] for item in cursor.fetchall()]
            self.usestock = (StockSresult)
            self.Searchstock_S()
        elif order_type == 'TYPESTOCK':
            self.Searchstock_S()
            
    def Searchstock_S(self):
        order_type = self.typeorder.get()
        if order_type == 'NAMESTOCK':
            self.search_order = ttk.Combobox(self.frameorder , value = self.usestock)
            self.search_order.grid(row = 0 , column = 1 , padx = 5)
            self.search_order.bind('<KeyRelease>',self.StockEventsearch)
        elif order_type == 'TYPESTOCK':
            self.search_order = ttk.Combobox(self.frameorder)
            self.search_order.grid(row = 0 , column = 1 , padx = 5)
            self.search_order['values'] = ('FOOD','WATER')
            self.search_order['state'] = 'readonly'  
    def confirmsqlstock(self):
        try:
            order_type = self.typeorder.get()
            stockSS = self.search_order.get()
            con  = mysql.connector.connect(**config)
            cursor = con.cursor()
            if order_type == 'NAMESTOCK':
                likestocknamepart = f"""SELECT * FROM part WHERE PART_NAME like '%{stockSS}%' """
                cursor.execute(likestocknamepart)
                likerepart = cursor.fetchall() 
                for Del in self.tv_stock.get_children():
                    self.tv_stock.delete(Del)
                for row_stock in likerepart:
                    self.tv_stock.insert("",'end' ,iid = row_stock[0] , values = (row_stock[0] ,row_stock[1]  , row_stock[2] , row_stock[3] ,row_stock[4] ))
                con.close()
            elif order_type == 'TYPESTOCK':
                likestocknamepart2 = f"""SELECT * FROM part WHERE TYPE_PART like '%{stockSS}%' """
                cursor.execute(likestocknamepart2)
                likerepart = cursor.fetchall() 
                for Del in self.tv_stock.get_children():
                    self.tv_stock.delete(Del)
                for row_stock in likerepart:
                    self.tv_stock.insert("",'end' ,iid = row_stock[0] , values = (row_stock[0] ,row_stock[1]  , row_stock[2] , row_stock[3] ,row_stock[4] ))
                con.close()
        except Exception:
            messagebox.showerror("Error","กรุณาเลือกประเภทการค้นหา")
    def orderascstock(self):
        con  = mysql.connector.connect(**config)
        cursor = con.cursor()
        sql = 'SELECT * FROM part ORDER BY QTY_PART ASC;'
        cursor.execute(sql)
        sqlasc = cursor.fetchall()
        for Del in self.tv_stock.get_children():
            self.tv_stock.delete(Del)
        for row_stock in sqlasc:
            self.tv_stock.insert("",'end' ,iid = row_stock[0] , values = (row_stock[0] ,row_stock[1]  , row_stock[2] , row_stock[3] ,row_stock[4] ))
        con.close()
    def orderdescstock(self):
        con  = mysql.connector.connect(**config)
        cursor = con.cursor()
        sql = 'SELECT * FROM part ORDER BY QTY_PART DESC;'
        cursor.execute(sql)
        sqlDESC = cursor.fetchall()
        for Del in self.tv_stock.get_children():
            self.tv_stock.delete(Del)
        for row_stock in sqlDESC:
            self.tv_stock.insert("",'end' ,iid = row_stock[0] , values = (row_stock[0] ,row_stock[1]  , row_stock[2] , row_stock[3] ,row_stock[4] ))
        con.close()
class Order_page(tk.Toplevel):
    def __init__(self,order):
        super().__init__(order)
        self.geometry('625x650')
        self.title('Order')
        self.resizable(False, False)
        # search
        frame_tv_pre = Frame(self , width = 600 ,  heigh = 600 ,bg ='pink' ) #Frame
        frame_tv_pre.pack()
        framepreorder = LabelFrame(self, text = "ค้นหาข้อมูล" , padx = 5 , pady = 5 )
        framepreorder.pack()
        self.amountdashboard = tk.LabelFrame(self , text = 'รายละเอียด' , padx = 5 , pady = 5 )
        self.amountdashboard.pack()
        self.ok_frame = Frame(self) #Frame
        self.ok_frame.pack()
        
        #call fuction Combobox
        self.sql_search()
        self.current_table = tk.StringVar()
        Laorder_name =  tk.Label(framepreorder , text ="ชื่อสินค้า" ).grid(row = 1 ,  column  = 0  )
        self.typemember = StringVar(None,'0')
        self.select1 = tk.Radiobutton( framepreorder , text="เป็นสมาชิก", variable= self.typemember , value='MEMBER'  ,command =  self.user_or_guest )
        self.select1.grid(row = 0 , column = 0)
        self.select2 = tk.Radiobutton( framepreorder , text="ไม่เป็นสมาชิก", variable= self.typemember, value='GUEST' ,command = self.user_or_guest)
        self.select2.grid(row = 0 ,column = 1)
        self.search_combopreorder = ttk.Combobox(framepreorder , value =self.result_engine , textvariable =self.current_table  )
        self.search_combopreorder .bind('<KeyRelease>',self.select_event)
        self.search_combopreorder.current()
        self.search_combopreorder.grid(row = 1 ,  column = 1 , padx = 5)
        self.button_engine = tk.Button(framepreorder, text = 'เพิ่มลงตะกร้า' , command =  self.sql_select)
        self.button_engine.grid(row = 1 , column = 2 , padx = 5)
        self.button_predelete = tk.Button(framepreorder, text = 'นำออกจากตะกร้า' , command =  self.select_preorder)
        self.button_predelete.grid(row = 1 , column = 3 , padx = 5)
        labelpre1 = tk.Label(framepreorder , text = 'จำนวน').grid(row  = 2 ,column = 0)
        self.qtyorder = tk.Entry(framepreorder)
        self.qtyorder.grid(row = 2 , column = 1 , pady = 10)
        self.final = tk.Button(self.ok_frame, text = 'ชำระเงิน'  , command = self.Pay,width=10,height=3)
        self.final.pack()
        #tree view  Pre_order
        self.pre_scroll = Scrollbar(frame_tv_pre)   #Scroll
        self.pre_scroll.pack(side = RIGHT,fill=Y)
        self.tv_pre= ttk.Treeview(frame_tv_pre, yscrollcommand=self.pre_scroll.set) #command Scroll
        self.pre_scroll.config(command = self.tv_pre.yview)
        self.tv_pre['columns']=( 'ORDER', 'ID' , 'Name', 'SEX'  ,  'Store' , 'Unit' )   
        self.tv_pre.column('#0', width=0, stretch=NO)
        self.tv_pre.column('ORDER', anchor=CENTER, width=100)
        self.tv_pre.column('ID', anchor=CENTER, width=100)
        self.tv_pre.column('Name', anchor=CENTER, width=100)
        self.tv_pre.column('SEX', anchor=CENTER, width= 100)
        self.tv_pre.column('Store', anchor=CENTER, width= 100)
        self.tv_pre.column('Unit', anchor=CENTER, width= 100)
        
        # head table_Preorder
        self.tv_pre.heading('#0', text='', anchor=CENTER)
        self.tv_pre.heading('ORDER', text='รหัสออร์เดอร์', anchor=CENTER)
        self.tv_pre.heading('ID', text='รหัสสินค้า', anchor=CENTER)
        self.tv_pre.heading('Name', text='ชื่อสินค้า', anchor=CENTER)
        self.tv_pre.heading('SEX', text='จำนวน', anchor=CENTER)
        self.tv_pre.heading('Store', text='สินค้าที่มีอยู่ในคลัง', anchor=CENTER)
        self.tv_pre.heading('Unit', text='ราคาต่อหน่วย', anchor=CENTER)
        self.tv_pre.pack(side ='left')
        #user detail and amount dashboard

        self.headuser = tk.Label(self.amountdashboard,text= 'ชื่อ :')
        self.headtel = tk.Label(self.amountdashboard,text='เบอร์ :')
        self.headid = tk.Label(self.amountdashboard,text='Id :')
        self.headuser.grid(row=0,column=0,sticky='E')
        self.headtel.grid(row=0,column=2,sticky='E')
        self.headid.grid(row=0,column=4,sticky='E')


        self.userbath = tk.Label(self.amountdashboard , text = '')
        self.phonebath = tk.Label(self.amountdashboard , text = '')
        self.IDbath = tk.Label(self.amountdashboard , text = '')
        self.userbath.grid(row = 0 , column = 1)
        self.phonebath.grid(row = 0 , column = 3)
        self.IDbath.grid(row = 0 , column = 5)

        bath_cash = tk.DoubleVar()
        labath = Label(self.amountdashboard , text = 'ยอดชำระ :' )
        self.bath = tk.Label(self.amountdashboard , text = '0' ,fg = 'orange')
        labath.grid(row = 1 , column = 0,sticky='E')
        self.bath.grid(row = 1 , column = 1  , padx =  10)

        self.billid1 = tk.Label(self.amountdashboard,text="หมายเลขใบเสร็จ :")
        self.billid2 = tk.Label(self.amountdashboard,text="")
        self.billid1.grid(row=2,column=0,sticky='E')
        self.billid2.grid(row=2,column=1)

        self.freelabel1 = tk.Label(self.amountdashboard,text='                                        ')
        self.freelabel2 = tk.Label(self.amountdashboard,text='                              ')
        self.freelabel3 = tk.Label(self.amountdashboard,text='                       ')
        self.freelabel1.grid(row=3,column=1)
        self.freelabel2.grid(row=3,column=3)
        self.freelabel3.grid(row=3,column=5)
        
        
        
        #call Error
        self.canclebutton()

        #------------------
    def sql_search(self):
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        query = "SELECT PART_NAME FROM  part;"
        cursor.execute(query)
        row = [item[0] for item in cursor.fetchall()]
        self.result_engine = (row)
    def select_event(self , event):
        value = event.widget.get()
        if value =='':
            self.search_combopreorder['value'] = self.result_engine
        else:
            data = [ ]
            for item in  self.result_engine:
                if value.lower() in item.lower( ):
                    data.append(item)
            self.search_combopreorder['value'] = data
            
    def  sql_select(self):
        memberuser = self.typemember.get()
        qty =  self.qtyorder.get()
        current  = self.current_table.get()
        if memberuser =='MEMBER':
            current_order = self.xo
            tupleconvert = (current ,)
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            cursor.execute("SELECT PART_ID , PART_NAME  , QTY_PART ,UNIT_PART  FROM  part  WHERE  PART_NAME = %s  " ,  (tupleconvert))
            stock_pre = cursor.fetchall()
            if len(qty) == 0:
                try:
                    messagebox.showerror('Error', 'กรุณากรอกข้อมูลให้ครบและถูกต้อง!')
                except Exception :
                    pass
            else:
                try:
                    for row_pre in stock_pre:
                        self.tv_pre.insert("",'end' ,iid = row_pre[0], values =  ( current_order ,  row_pre[0] , row_pre[1] , qty , row_pre[2], row_pre[3] ))
                    con.close()
                except Exception:
                    messagebox.showerror('Error', 'ข้อมูลมีความซ้ำซ้อนกัน')
                    con.close()
            # cal Fuction 
                self.cal()
        elif  memberuser =='GUEST':
            current_order = self.xo
            tupleconvert2 = (current ,)
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            cursor.execute("SELECT PART_ID , PART_NAME  , QTY_PART ,UNIT_PART  FROM  part  WHERE  PART_NAME = %s  " ,  (tupleconvert2))
            stock_pre2 = cursor.fetchall()
            if len(qty) == 0:
                try:
                    messagebox.showerror('Error', 'กรุณากรอกข้อมูลให้ครบและถูกต้อง!')
                except Exception :
                    pass
            else:
                try:
                    for row_pre in stock_pre2:
                        self.tv_pre.insert("",'end' ,iid = row_pre[0], values =  ( current_order ,  row_pre[0] , row_pre[1] , qty , row_pre[2], row_pre[3] ))
                    con.close()
                except Exception:
                    messagebox.showerror('Error', 'ข้อมูลมีความซ้ำซ้อนกัน')
                    con.close()
                self.cal()
        #----------CAL-----------------
    def cal(self):      
        total = 0.0
        try:
            for child1 in self.tv_pre.get_children():
                qtycount = int(self.tv_pre.item(child1,'values')[3])
                stockcount = int(self.tv_pre.item(child1,'values')[4])
                countresult = (stockcount - qtycount )
                if countresult <0:
                    messagebox.showinfo("Error", "สินค้าหมด")
                    for line in self.tv_pre.get_children():
                        pass
                    self.tv_pre.delete(line)
                    self.bath.config(text=0.0)

            for child in self.tv_pre.get_children():
                qtycal = float(self.tv_pre.item(child,'values')[5])
                countcal =  int(self.tv_pre.item(child,'values')[3])
                total +=float(qtycal*countcal)
                if qtycal ==0.0:
                    messagebox.showinfo("Error", "สินค้าหมด")
                    for line2 in self.tv_pre.get_children():
                        pass
                    self.tv_pre.delete(line2)
            self.bath.config(text=total)
        except Exception as e:
            print(e)
    def select_preorder(self):
        selected_preorder = list( [self.tv_pre.focus()] )
        values_stock_pre = self.tv_pre.item(selected_preorder,"values")
        self.tv_pre.delete( selected_preorder)
        try:
            self.cal()
        except:
            print('Error')

# ------------------------------------INSERT   TREEVIEW CART ----------------------------------
    def clearpay(self):
        self.billid2.config(text='')
        self.bath.config(text='')
        self.phonebath.config(text='')
        self.IDbath.config(text='')
        self.userbath.config(text='')
        self.search_combopreorder.set('')
        self.qtyorder.delete(0,END)
        for Delorder in self.tv_pre.get_children():
            self.tv_pre.delete(Delorder)
    
    def inputtable(self):
        gettime = tmnow()
        getdate = daynow()
        genauto = self.xo
        IDCOS = self.IDbath.cget('text')
        currentbath = self.bath.cget('text')
        namecurrent = self.userbath.cget('text')
        try:
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            cursor.execute( "INSERT INTO ordercus(ORDER_NUM, NOWDATE ,ORDER_TIME ,Payment,ID_USER ,NAME_USER )VALUES (%s,%s,%s,%s,%s,%s)"
            , (genauto , getdate , gettime,currentbath ,IDCOS,namecurrent) )
            con.commit()
            con.close()
        except  Exception as e:
            print(e)
            con.close()
    def updateqty(self):  #-----------------------------FIX -----------------------------
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        cursor.execute("""select  part.PART_ID,part.PART_NAME ,(part.QTY_PART-order_line.NUM_ORDER) as QTY_PART
        from order_line
        INNER JOIN part ON order_line.PART_ID = part.PART_ID;""")
        m = cursor.fetchall()
        for i in m:            # index 0 = PART_ID   |  index 1 = PART_NAME  | index 2 = CURRENT_STOCK
            PART_ID = (i[0]) 
            PART_NAME = (i[1])
            CURRENT_STOCK = (i[2])
        #print('update is','PART_ID =', PART_ID , '|' , 'PART_NAME =' , PART_NAME  , '|' ,' CURRENT_STOCK = ' , CURRENT_STOCK)
        reup = (str(PART_ID),str(PART_NAME),str(CURRENT_STOCK))
        #print('result INNER JOIN IS = ' , reup)
        try:   # UPDATE STOCK
            updatestock = ("UPDATE part SET QTY_PART = ('"+str(CURRENT_STOCK)+"') WHERE PART_ID = ('"+PART_ID+"')")
            cursor.execute(updatestock)
            con.commit()
            o = cursor.fetchall()
        except Exception as update :
            print(update) 
        #con.close()
    def Pay(self):  #------------------------FIX
        self.typemember.set('0')
        IDCOS = self.IDbath.cget('text')
        getcom = self.search_combopreorder.get()
        getqty = self.qtyorder.get()
        currentbath = self.bath.cget('text')
        jojo = self.tv_pre.get_children()
        if len(jojo) > 0:
            if IDCOS !='':
                con = mysql.connector.connect(**config)
                cursor = con.cursor()
                try:
                    self.inputtable()
                    for child in self.tv_pre.get_children():
                        x = (self.tv_pre.item(child) ['values'] )
                        cursor.execute("INSERT INTO order_line(ORDER_NUM , PART_ID, PART_NAME ,NUM_ORDER,QTY_PART , PRICE_ORDER )VALUES(%s,%s,%s,%s,%s,%s)",(x))
                        tot = cursor.fetchall()
                        con.commit()
                    #con.close()
                        try: #---------------------- 
                            self.updateqty()
                        except Exception as test:
                            messagebox.showinfo("Error", "เลือกข้อมูลให้ครบก่อนชำระเงิน")
                            print(test)
                    self.clearpay()
                    self.canclebutton()
                    self.select1.config(state=NORMAL,value = 'MEMBER' ,takefocus=0)
                    self.select2.config(state=NORMAL , value ='GUEST' , takefocus=0)
                    con.close()
                except Exception as e :
                    messagebox.showinfo("Error", "เลือกข้อมูลให้ครบก่อนชำระเงิน")
                    con.close()
            elif getcom == '' and getqty =='' :
                messagebox.showinfo("Error", "เลือกสินค้าก่อน")
            elif currentbath  == '':
                messagebox.showinfo("Error", "เลือกสินค้าก่อน")
            else:
                messagebox.showinfo("Error", "เลือกว่าเป็นสมาชิกหรือไม่เป็นสมาชิกก่อน")
        else:
            messagebox.showerror("Error","กรุณาเพิ่มสินค้า อย่างน้อย 1 ชิ้น")
            self.clearpay()
            self.select2.config(state=NORMAL,takefocus='GUEST')
            self.select1.config(state=NORMAL,takefocus='MEMBER')
            self.canclebutton()
            
   
#-----------------------------------PAGE USER OR ----GUEST ------------------------------------
    def user_or_guest(self):
        memberuser = self.typemember.get()
        if memberuser == 'MEMBER':
            self.U_G = Toplevel()
            self.U_G.geometry("300x100")
            self.U_G.title('กรอกสมาชิก')
            self.U_G.resizable(False, False)
            self.lb_ug  = tk.LabelFrame(self.U_G , text = 'ค้นหา' , padx = 5 , pady = 5)
            self.lb_ug.pack()
            self.typeu_gx = StringVar(None,'0')
            select1ug = tk.Radiobutton(self.lb_ug, text="ค้นหาด้วยชื่อ", variable= self.typeu_gx , value='NAME' ,command= self.selectedCombo )
            select1ug.grid(row = 0 , column = 0)
            select2ug = tk.Radiobutton(self.lb_ug, text="ค้นหาด้วยเบอร์", variable= self.typeu_gx , value='PHONE' , command = self.selectedCombo )
            select2ug.grid(row = 0 ,column = 1)
            self.fake_combo_select = ttk.Combobox(self.lb_ug).grid(row = 1 , column = 0)
            button_engine = tk.Button(self.lb_ug, text = 'ยืนยัน' , command = self.confirmsearch).grid(row = 1 , column = 1)
            self.U_G.grab_set()
        elif memberuser =='GUEST':
            self.FIX_BUGORDER_NUM()
            self.phonebath.config(text='GUEST')
            self.IDbath.config(text='GUEST')
            self.userbath.config(text='GUEST')
            self.userbutton()
            
#--------------------------------Fuction Search_Engine------------------

#------------------------------------Fuction SQL------------------------------
    def ComboSearch(self):
        self.current_sqlug= tk.StringVar()
        self.search_ug = ttk.Combobox(self.lb_ug , value = self.order, textvariable =self.current_sqlug )
        self.search_ug.grid(row = 1 , column = 0)
        self.search_ug.bind('<KeyRelease>', self.search_u_g)
    def selectedCombo(self):
        T = self.typeu_gx.get()
        if T == 'NAME':
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            query = "SELECT NAME_USER  from  customer;"
            cursor.execute(query)
            row = [item[0] for item in cursor.fetchall()]
            self.order = (row)
            self.ComboSearch()
        elif T == 'PHONE':
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            query = "SELECT PHONE_USER  from  customer;"
            cursor.execute(query)
            row = [item[0] for item in cursor.fetchall()]
            self.order = (row)
            self.ComboSearch()
    def search_u_g(self,event):
        value = event.widget.get()
        if value == '':
            self.search_ug['value'] = self.order
        else:
            data = [ ]
            for item in self.order:
                if value.lower() in item.lower( ):
                    data.append(item)
            self.search_ug['value'] = data
#-----------------------------------ConFIRM USER -------------------------------------------
    def auto_id(self):
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        cursor.execute("SELECT SUBSTR(MD5(RAND()), 1, 10) AS checksumResult;")
        idauto = cursor.fetchone()
        self.xo = str(''.join(map(str, idauto)))
        con.close()
        self.billid2.config(text=self.xo)

    def confirmsearch(self):
        try:
            T = self.typeu_gx.get()
            current =self.search_ug.get()
            memberuser = self.typemember.get()
            if memberuser == 'MEMBER':
                if T == 'NAME':
                    con = mysql.connector.connect(**config)
                    cursor = con.cursor()
                    cursor.execute("SELECT PHONE_USER FROM customer WHERE NAME_USER  = %s"  ,  (current,) )
                    test_view1 = cursor.fetchone()
                    self.resultb = str(''.join(map(str, test_view1)))
                    self.phonebath.config(text=self.resultb)
                    self.varuserbath = current
                    self.userbath.config(text = self.varuserbath )
                    cursor.execute("SELECT  ID_USER  FROM customer WHERE NAME_USER  = %s"  ,  (current,) )
                    subtest_view11 = cursor.fetchone()
                    resultsub11 = str(''.join(map(str,subtest_view11)))
                    self.IDbath.config(text=resultsub11)
                    #call fuction
                    self.FIX_BUGORDER_NUM()
                    self.userbutton()
                    self.U_G.destroy()
                elif T=='PHONE':
                    con = mysql.connector.connect(**config)
                    cursor = con.cursor()
                    cursor.execute("SELECT  NAME_USER  FROM customer WHERE PHONE_USER  = %s"  ,  (current,) )
                    test_view2 = cursor.fetchone()
                    result2 = str(''.join(map(str, test_view2)))
                    cursor.execute("SELECT  ID_USER  FROM customer WHERE PHONE_USER  = %s"  ,  (current,) )
                    subtest_view22 = cursor.fetchone() 
                    resultsub22 = str(''.join(map(str,subtest_view22)))
                    self.IDbath.config(text=resultsub22)
                    self.phonebath.config(text=current)
                    self.userbath.config(text = result2 )
                    self.FIX_BUGORDER_NUM()
                    self.userbutton()
                    self.U_G.destroy()
            elif memberuser == 'GUEST':
                pass
        except Exception as e:
            messagebox.showerror("Error", "กรุณาเลือกประเภทการค้นหา")
    def canclebutton(self):
        self.button_engine['state'] = DISABLED
        self.button_predelete['state'] = DISABLED
        self.final['state'] = DISABLED
    def userbutton(self):
        self.button_engine['state'] = NORMAL
        self.button_predelete['state'] = NORMAL
        self.final['state'] = NORMAL
    def FIX_BUGORDER_NUM(self):
        memberusers = self.typemember.get()
        if memberusers == 'MEMBER':
            self.select1.config(state=DISABLED,takefocus='MEMBER')
            # self.INPUTAUTOID()
            self.auto_id()
            self.select2.config(state=NORMAL)
            for Del1 in self.tv_pre.get_children():
                self.tv_pre.delete(Del1)
            self.bath.config(text=0.0)
        elif memberusers == 'GUEST':
            self.select2.config(state=DISABLED,takefocus='GUEST')
            # self.INPUTAUTOID()
            self.auto_id()
            self.select1.config(state=NORMAL)
            for Del2 in self.tv_pre.get_children():
                self.tv_pre.delete(Del2)
            self.bath.config(text=0.0)
class Bill_Page(tk.Toplevel):
    def __init__(self,bill):
        super().__init__(bill)
        self.geometry('1200x400')
        self.title('บิลสินค้า')
        self.resizable(False, False)

        main_frame = Frame(self)
        main_frame.pack()
        main_frame_bill = Frame(main_frame)
        main_frame_bill.grid(column=1,row=0,padx=25)
        main_frame_table = Frame(main_frame)
        main_frame_table.grid(column=0,row=0,padx=25)

        self.frame_tv_bill = Frame(main_frame_table, width = 600 ,  heigh = 600 ,bg ='pink' ) #Frame
        self.frame_tv_bill.grid(column=0,row=1)

        self.searchframe = LabelFrame(main_frame_table  , text = 'ค้นหาตาม' ,padx = 5)
        self.searchframe.grid(column=0,row=0)

        frame_mode = Frame(main_frame_table, width = 600 ,  heigh = 600 ) #Frame
        frame_mode.grid(column=0,row=3)

        type_bill = LabelFrame(frame_mode  , text = 'เลือกประเภท' , padx = 5 , pady = 5)
        type_bill.grid(column=0,row=0,padx=25)
        searchbill = LabelFrame(frame_mode  , text = 'บิล')
        searchbill.grid(column=1,row=0,padx=25 )
        
        displayframe = LabelFrame(main_frame_bill  , text = 'แสดงผลบิล' , padx = 10)
        displayframe.grid(column=0,row=0)

        self.bill_scroll = Scrollbar(self.frame_tv_bill)   #Scroll
        self.bill_scroll.pack(side = RIGHT,fill=Y)
        self.tv_bill= ttk.Treeview(self.frame_tv_bill, yscrollcommand=self.bill_scroll.set) #command Scroll
        self.bill_scroll.config(command = self.tv_bill.yview)
        self.tv_bill['columns']=('ID' ,  'Date', 'Time'  , 'Payment' , 'User')   
        self.tv_bill.column('#0', width=0, stretch=NO)
        self.tv_bill.column('ID', anchor=CENTER, width= 100)
        self.tv_bill.column('Date', anchor=CENTER, width=100)
        self.tv_bill.column('Time', anchor=CENTER, width=100)
        self.tv_bill.column('Payment', anchor=CENTER, width= 100)
        self.tv_bill.column('User', anchor=CENTER, width= 200)
        
        # head table_ User
        self.tv_bill.heading('#0', text='', anchor=CENTER)
        self.tv_bill.heading('ID', text='รหัสบิล', anchor=CENTER)
        self.tv_bill.heading('Date', text='วันที่', anchor=CENTER)
        self.tv_bill.heading('Time', text='เวลา', anchor=CENTER)
        self.tv_bill.heading('Payment', text='ยอดรวมชำระ', anchor=CENTER)
        self.tv_bill.heading('User', text='ชื่อผู้ซื้อ', anchor=CENTER)
        self.tv_bill.pack(side ='left')
        
        info_all = tk.Button(type_bill , width  =8 , text = 'ทั้งหมด' , command = self.displaytablebill).grid(row = 0 , column = 0 , padx = 5)
        info_bguest = tk.Button(type_bill , width = 8 , text = 'ไม่เป็นสมาชิก' , command = self.displaytableguest).grid(row = 0 , column = 2 , padx = 5)
        info_user = tk.Button(type_bill , width = 8, text = 'สมาชิก' , command = self.displaytableuser).grid(row = 0 , column = 1 , padx = 5)
        
        info_B = tk.Button(searchbill,text = 'ดูรายละเอียด' , command = self.INFOPAGE).grid(row = 0 ,column = 0 , padx = 5 , pady = 5)
        #callfuction displayall
        self.displaytablebill()
        self.displaybill = scrolledtext.ScrolledText(displayframe , width = 55 , height  = 20 )
        self.displaybill.pack()
        savetxt = Button(displayframe , text = 'save' , command = self.savefiles).pack(pady = 5)
        self.value_billbox = tk.StringVar(None,'0')
        self.R1bill = Radiobutton(self.searchframe, text="หมายเลขบิล", variable=self.value_billbox, value='ordernum',command=self.selectowo_bill)
        self.R1bill.grid(row = 0  , column = 0)
        self.R2bill = Radiobutton(self.searchframe, text="ชื่อผู้ซื้อ", variable=self.value_billbox, value='userbuy',command=self.selectowo_bill)
        self.R2bill.grid(row = 0  , column = 1)
        self.fake_combo_bill = ttk.Combobox(self.searchframe).grid(row = 1 , column = 0)
        self.search_Bill_B = Button(self.searchframe , text = 'ค้นหา' ,command = self.confirm_searchbill)
        self.search_Bill_B.grid(row = 1 , column = 1)
        self.displaybill['state'] = DISABLED
    def displaytablebill(self): # display all
        
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        query = "SELECT ORDER_NUM , NOWDATE , ORDER_TIME , Payment , NAME_USER FROM ordercus ORDER BY bill_now DESC "
        cursor.execute(query)
        result = cursor.fetchall()  
        for Del in self.tv_bill.get_children():
            self.tv_bill.delete(Del)
        for row_bill in result:
            self.tv_bill.insert("",'end' ,iid = row_bill[0] , values = (row_bill[0] ,row_bill[1]  , row_bill[2] , row_bill[3] ,row_bill[4]))
        con.close()
    def displaytableguest(self):  #displayguest
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        queryguest = "SELECT ORDER_NUM , NOWDATE , ORDER_TIME , Payment , NAME_USER FROM ordercus where NAME_USER = 'GUEST' ORDER BY bill_now DESC"
        cursor.execute(queryguest)
        result = cursor.fetchall()  
        for Del in self.tv_bill.get_children():
            self.tv_bill.delete(Del)
        for row_bill in result:
            self.tv_bill.insert("",'end' ,iid = row_bill[0] , values = (row_bill[0] ,row_bill[1]  , row_bill[2] , row_bill[3] ,row_bill[4]))
        con.close()
    def displaytableuser(self):  #displayuser
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        queryuser = """SELECT  ordercus.ORDER_NUM , ordercus.NOWDATE , ordercus.ORDER_TIME , ordercus.Payment ,customer.NAME_USER
        FROM ordercus INNER JOIN customer ON customer.NAME_USER = ordercus.NAME_USER ORDER BY bill_now DESC"""
        cursor.execute(queryuser)
        result = cursor.fetchall()  
        for Del in self.tv_bill.get_children():
            self.tv_bill.delete(Del)
        for row_bill in result:
            self.tv_bill.insert("",'end' ,iid = row_bill[0] , values = (row_bill[0] ,row_bill[1]  , row_bill[2] , row_bill[3] ,row_bill[4]))
        con.close()
    def INFOPAGE(self):
        selected_bill = list( [self.tv_bill.focus()] )
        self.displaybill['state'] = 'normal'
        self.displaybill.delete("1.0","end")
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
        queryB ="""SELECT order_line.ORDER_NUM , order_line.PART_NAME , order_line.NUM_ORDER  ,order_line.PRICE_ORDER , ordercus.NOWDATE,
        ordercus.ORDER_TIME , ordercus.Payment , ordercus.NAME_USER
        FROM order_line
        INNER JOIN ordercus ON ordercus.ORDER_NUM = order_line.ORDER_NUM WHERE order_line.ORDER_NUM = %s ORDER BY ordercus.bill_now DESC """
        cursor.execute(queryB,selected_bill)
        x = cursor.fetchall()
        re = []
        for i in x:
            partname =i[1]
            numorder = i[2]
            priceorder =i[3]
            resultallorder = f"   {partname} \t\t\t QTY  {numorder}   \t Unit {priceorder}   Bath \n"
            re.append(resultallorder)
        ordernum = i[0]
        payment = i[6]
        nameuser = i[7]
        nowdate = i[4]
        ordertime =i[5]
        con.close()
        #convertlist to str
        string1 ='\n '
        convertlist = string1.join(re)
        format = f""" \t    ***** LungKang Papaya Is Love SHOP *****  
        \n\n  No. \t {ordernum}\t\t\t   Date {nowdate}\n\t\t\t\t\t\t\t\t\t\t\t   Time {ordertime}
        \n  Purchased By {nameuser}\n\n {convertlist} \n\n \t\tTotal payment {payment} Bath 
        \n ***************************************************************************
        \n\n """
        self.displaybill.insert(1.0,f"{format}")
        self.displaybill['state'] = DISABLED
        # insert to display
    def savefiles(self):
        getdate = daynow()
        utf = self.displaybill.get(1.0,END)
        Files = [('All Files', '*.*'),
        ('Text Document', '*.txt')]
        file = asksaveasfile(initialfile = f'{getdate}.txt',filetypes = Files, defaultextension =".txt")
        file.write(utf)
    #Search fuction
    def add_bill(self,event):
        value = event.widget.get()
        if value == '':
            self.cbill['value'] = self.billappend 
        else:
            data = [ ]
            for item in self.billappend :
                if value.lower() in item.lower( ):
                    data.append(item)
                self.cbill['value'] = data
    def bobox_bill(self):
        self.cbill = ttk.Combobox(self.searchframe , value = self.billappend   )
        self.cbill.grid(row = 1, column = 0)
        self.cbill.bind('<KeyRelease>',self.add_bill)
    def selectowo_bill(self):
        getselect = self.value_billbox.get()
        if getselect =='ordernum':
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            sqlordernumGG = "SELECT ORDER_NUM from ordercus"
            cursor.execute(sqlordernumGG)
            rowbill = [item[0] for item in cursor.fetchall()]
            self.billappend = (rowbill)
            self.bobox_bill()
        elif getselect =='userbuy':
            con = mysql.connector.connect(**config)
            cursor = con.cursor()
            sqlnumuserGG = "SELECT DISTINCT NAME_USER from ordercus"
            cursor.execute(sqlnumuserGG)
            rowbilluser = [item[0] for item in cursor.fetchall()]
            self.billappend = (rowbilluser)
            self.bobox_bill()
    def confirm_searchbill(self):
        try:
            getselect = self.value_billbox.get()
            getcbill = self.cbill.get()
            if getselect =='ordernum':
                con = mysql.connector.connect(**config)
                cursor = con.cursor()
                sqlconfirmsearch = "SELECT ORDER_NUM , NOWDATE , ORDER_TIME , Payment , NAME_USER from ordercus WHERE ORDER_NUM =%s ORDER BY bill_now DESC"
                cursor.execute(sqlconfirmsearch,(getcbill,))
                result = cursor.fetchall()
                for Del in self.tv_bill.get_children():
                    self.tv_bill.delete(Del)
                for row_bill in result:
                    self.tv_bill.insert("",'end' ,iid = row_bill[0] , values = (row_bill[0] ,row_bill[1]  , row_bill[2] , row_bill[3] ,row_bill[4]))
                con.close()
            elif getselect =='userbuy':
                con = mysql.connector.connect(**config)
                cursor = con.cursor()
                sqlconfirmsearch = "SELECT ORDER_NUM , NOWDATE , ORDER_TIME , Payment , NAME_USER from ordercus WHERE NAME_USER =%s ORDER BY bill_now DESC"
                cursor.execute(sqlconfirmsearch,(getcbill,))
                result2 = cursor.fetchall()
                for Del2 in self.tv_bill.get_children():
                    self.tv_bill.delete(Del2)
                for row_bill2 in result2:
                    self.tv_bill.insert("",'end' ,iid = row_bill2[0] , values = (row_bill2[0] ,row_bill2[1]  , row_bill2[2] , row_bill2[3] ,row_bill2[4]))
                con.close()
        except Exception:
            messagebox.showerror("Error","กรุณาเลือกประเภทการค้นหา")

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("550x650")
    app.resizable(False, False)
    app.title('หน้าหลัก ❤')
    app.mainloop()
    
