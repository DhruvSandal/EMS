from tkinter import *
from tkinter import messagebox
import pymysql #install mysql
import time
import os
import tempfile
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Employee Finance Managment System')
        self.root.geometry('1520x950+0+0')
        self.root.iconbitmap('minecraft.ico')
        self.root.config(bg='white')
        title=Label(root,text="Employee Finance Managment System",bg='#656A57',anchor="w",fg='white',padx= 30,font=("Times New Roman", 30,"bold")).place(x=0,y=0,relwidth=1)
        
        ##=========== This is frame one ==============##
        
        
        ###------ Variables -----###
        
        self.var_emp_code=StringVar() 
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar() 
        self.var_contact=StringVar()
        self.var_status=StringVar()        
        self.var_experience=StringVar() 
        self.var_location=StringVar() 
        
        Frame1=Frame(self.root,bd=3,relief=RIDGE)
        Frame1.place(x=10,y=60,width=800,height=750)
        title1=Label(Frame1, text="Employee details",bg='#656A57',anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=10,relwidth=1)
        
        ##========  ROW 0 =========##
        
        Employee_code=Label(Frame1, text="Employee Code",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=80)
        self.txt_Employee_code=Entry(Frame1,bg='lightyellow',textvariable=self.var_emp_code,font=("Times New Roman",15,"bold"))
        self.txt_Employee_code.place(x=230,y=85,width=300)
        btn_search=Button(Frame1,text='Search',command=self.search,font=("Times New Roman",15,"bold"),bg='#656A57',padx=20).place(x=560,y=80)
        
        ##====== ROW 1 ========##
        
        designation=Label(Frame1, text="Designation",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=140)
        txt_designation=Entry(Frame1,bg='lightyellow',textvariable=self.var_designation,font=("Times New Roman",15,"bold")).place(x=175,y=145)
        
        DOJ=Label(Frame1, text="D.O.J",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=380,y=140)
        txt_DOJ=Entry(Frame1,bg='lightyellow',textvariable=self.var_doj,font=("Times New Roman",15,"bold")).place(x=560,y=145)
        
        ##====== ROW 2 ========##
        
        Name=Label(Frame1, text="Name",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=200)
        txt_Name=Entry(Frame1,textvariable=self.var_name, font=("Times New Roman",15,),bg='lightyellow').place(x=175,y=205)
        
        DOB=Label(Frame1, text="D.O.B",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=380,y=200)
        txt_DOB=Entry(Frame1,bg='lightyellow',textvariable=self.var_dob,font=("Times New Roman",15,"bold")).place(x=560,y=205)
        
        ##====== ROW 3 ========##
            
        Age=Label(Frame1, text="Age",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=260)
        txt_Age=Entry(Frame1, font=("Times New Roman",15,),bg='lightyellow',textvariable=self.var_age).place(x=175,y=265)
        
        Experience=Label(Frame1, text="Experience",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=380,y=260)
        txt_Experience=Entry(Frame1,bg='lightyellow',textvariable=self.var_experience,font=("Times New Roman",15,"bold")).place(x=560,y=260)
        
        ##====== ROW 4 ========##
                      
        Gender=Label(Frame1, text="Gender",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=320)
        txt_Gender=Entry(Frame1, font=("Times New Roman",15,),textvariable=self.var_gender,bg='lightyellow').place(x=175,y=325)
        
        Proof_ID=Label(Frame1, text="Proof ID",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=380,y=320)
        txt_Proof_ID=Entry(Frame1,bg='lightyellow',textvariable=self.var_proof_id,font=("Times New Roman",15,"bold")).place(x=560,y=325)
        
        ##====== ROW 5 ========##
        
        Email=Label(Frame1, text="Email",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=380)
        txt_Email=Entry(Frame1, font=("Times New Roman",15,),textvariable=self.var_email,bg='lightyellow').place(x=175,y=385)
        
        Contact_no=Label(Frame1, text="Contact No",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=380,y=380)
        txt_Contact_no=Entry(Frame1,bg='lightyellow',textvariable=self.var_contact,font=("Times New Roman",15,"bold")).place(x=560,y=385)
        
        ##====== ROW 6 ========##
        
        Hired_location=Label(Frame1, text="Hired Loc",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=440)
        txt_Hired_location=Entry(Frame1, font=("Times New Roman",15,),textvariable=self.var_location,bg='lightyellow').place(x=175,y=445)
        
        Status=Label(Frame1, text="Status",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=380,y=440)
        txt_Status=Entry(Frame1,bg='lightyellow',textvariable=self.var_status,font=("Times New Roman",15,"bold")).place(x=560,y=445)
        
        
        ##====== ROW 7 ========##
        
        Address=Label(Frame1,text="Address",anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=500)
        self.txt_Address=Text(Frame1,font=("Times New Roman",15),bg='lightyellow')
        self.txt_Address.place(x=175,y=505,width=590,height=200)
        
        
        ##=========== This is frame two ==============##
        
        ##----------variable for frame two ---------##
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_total_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
        
        
        
        Frame2=Frame(self.root,bd=3,relief=RIDGE)
        Frame2.place(x=820,y=60,width=690,height=345)
        title2=Label(Frame2, text="Employee Salary details",bg='#656A57',anchor="w",fg='black',padx= 20,font=("Times New Roman",20,"bold")).place(x=0,y=10,relwidth=1)
        
        ##====== ROW 1 ========##
        
        Month=Label(Frame2, text="Month",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=0,y=80)
        txt_Month=Entry(Frame2,textvariable=self.var_month, font=("Times New Roman",15,),bg='lightyellow').place(x=105,y=85,width=80)
        
        Year=Label(Frame2, text="Year",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=205,y=80)
        txt_Year=Entry(Frame2,textvariable=self.var_year,bg='lightyellow',font=("Times New Roman",15,"bold")).place(x=290,y=85,width=80)
                
        Salary=Label(Frame2, text="Salary",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=390,y=80)
        txt_Salary=Entry(Frame2,textvariable=self.var_salary,bg='lightyellow',font=("Times New Roman",15,"bold")).place(x=500,y=85,width=120)
        
        ##====== ROW 2 ========##
            
        Total_days=Label(Frame2, text="Total Days",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=0,y=150)
        txt_Total_days=Entry(Frame2,textvariable=self.var_total_days, font=("Times New Roman",15,),bg='lightyellow').place(x=175,y=155,width=140)
        
        Absents=Label(Frame2, text="Absents",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=320,y=150)
        txt_Absents=Entry(Frame2,textvariable=self.var_absent,bg='lightyellow',font=("Times New Roman",15,"bold")).place(x=460,y=155,width=140)
        
        ##====== ROW 3 ========##
                      
        Medical=Label(Frame2, text="Medical",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=0,y=180)
        txt_Medical=Entry(Frame2,textvariable=self.var_medical, font=("Times New Roman",15,),bg='lightyellow').place(x=175,y=185,width=140)
        
        PF=Label(Frame2, text="PF",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=320,y=180)
        txt_PF=Entry(Frame2,textvariable=self.var_pf,bg='lightyellow',font=("Times New Roman",15,"bold")).place(x=460,y=185,width=140)
        
        ##====== ROW 4 ========##
        
        Convence=Label(Frame2, text="Convence",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=0,y=210)
        txt_Convence=Entry(Frame2,textvariable=self.var_convence, font=("Times New Roman",15,),bg='lightyellow').place(x=175,y=215,width=140)
        
        Net_salary=Label(Frame2, text="Net Salary",anchor="w",fg='black',padx= 20,font=("Times New Roman",18,"bold")).place(x=320,y=210)
        txt_Net_salary=Entry(Frame2,textvariable=self.var_net_salary,bg='lightyellow',font=("Times New Roman",15,"bold")).place(x=460,y=215,width=140)
        
        ##====== Buttons =========##
        Calculate=Button(Frame2,text='Calculate',command=self.calculate,bg='lightblue',font=("Times New Roman",18,"bold"),).place(x=20,y=275,height=40,width=120)
        
        self.Update=Button(Frame2,text='Update',state=DISABLED,command=self.update,bg='lightblue',font=("Times New Roman",18,"bold"),)
        self.Update.place(x=150,y=275,height=40,width=120)
        
        self.Save=Button(Frame2,text='Save',state=DISABLED,command=self.add,bg='lightgreen',font=("Times New Roman",18,"bold"),)
        self.Save.place(x=280,y=275,height=40,width=120)
        
        Clear=Button(Frame2,text='Clear',comman=self.clear,bg='lightgrey',font=("Times New Roman",18,"bold"),).place(x=410,y=275,height=40,width=120)
        
        self.Delete=Button(Frame2,text='Delete',state=DISABLED,command=self.delete,bg='red',font=("Times New Roman",18,"bold"),)
        self.Delete.place(x=540,y=275,height=40,width=120)
        
        
        ##=========== This is frame three ==============##
        Frame3=Frame(self.root,bd=3,relief=RIDGE)
        Frame3.place(x=820,y=445,width=690,height=366)
        
        ##========= Calculater ======##    
        title4=Label(Frame3,text="        Calculator",bg='#656A57',anchor="w",fg='BLACK',font=("Times New Roman", 20,"bold")).place(x=10,y=5,width=253)
        
        self.var_txt=StringVar()
        self.var_operator=""
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
            
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
        
        def clear():
            self.var_txt.set('')
            self.var_operator=''
                
        calculater=Frame(Frame3,bd=3,relief=RIDGE)
        calculater.place(x=10,y=40,width= 253, height= 310 )       
            
        #======== buttons =======#
        display=Entry(calculater,textvariable=self.var_txt,font=("Times New Roman",20),justify=RIGHT,bg='lightyellow').place(x=0,y=4,height=35,relwidth=1)
        num_7=  Button(calculater,text='7',command=lambda:btn_click(7),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=2,y=50,w=60,h=60)
        num_8=  Button(calculater,text='8',command=lambda:btn_click(8),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=64,y=50,w=60,h=60)
        num_9=  Button(calculater,text='9',command=lambda:btn_click(9),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=126,y=50,w=60,h=60)
        num_div=Button(calculater,text='/',command=lambda:btn_click('/'),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=188,y=50,w=60,h=60)
        num_4=  Button(calculater,text='4',command=lambda:btn_click(4),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=2,y=113,w=60,h=60)
        num_5=  Button(calculater,text='5',command=lambda:btn_click(5),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=64,y=113,w=60,h=60)
        num_6=  Button(calculater,text='6',command=lambda:btn_click(6),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=126,y=113,w=60,h=60)
        num_mul=Button(calculater,text='*',command=lambda:btn_click('*'),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=188,y=113,w=60,h=60)
        num_1=  Button(calculater,text='1',command=lambda:btn_click(1),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=2,y=176,w=60,h=60)
        num_2=  Button(calculater,text='2',command=lambda:btn_click(2),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=64,y=176,w=60,h=60)
        num_3=  Button(calculater,text='3',command=lambda:btn_click(3),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=126,y=176,w=60,h=60)
        num_min=Button(calculater,text='-',command=lambda:btn_click('-'),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=188,y=176,w=60,h=60)
        num_0=  Button(calculater,text='0',command=lambda:btn_click(0),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=2,y=239,w=60,h=60)
        num_dot=Button(calculater,text='C',command=clear,font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=64,y=239,w=60,h=60)
        num_add=Button(calculater,text='+',command=lambda:btn_click('+'),font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=126,y=239,w=60,h=60)
        num_equ=Button(calculater,text='=',command=result,font=("Times New Roman",15,"bold"),bg='lightgrey').place(x=188,y=239,w=60,h=60) 
               
               
        ##========= Salary Frame =============#
        salary_f=Frame(Frame3,bd=3,relief=RIDGE)
        salary_f.place(x=269,y=3,width= 410, height= 347 )
        title5=Label(salary_f,text="Salary Reciept",bg='#656A57',anchor="w",fg='BLACK',font=("Times New Roman", 20,"bold")).place(x=0,y=0,height=34,width=253,relwidth=1)
        
        salary_f2=Frame(salary_f,bg='white',relief=RIDGE,bd=2)
        salary_f2.place(x=0,y=40,relwidth=1,height=260)
        
        self.sample=f'''\tCompany Name, Titan\n\tAddress: Chandigarh
------------------------------------------------------
Employee ID\t\t: 
Salary Of\t\t: DD-MM-YYYY
Generated On\t\t: DD-MM-YYYY
------------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs,-------
Medical\t\t:  Rs,-------
PF\t\t:  Rs,-------
Gross Payment\t\t:  Rs,-------
Net Salary\t\t:  Rs,-------
------------------------------------------------------
This is computer generated slip, not
required any signature
'''
        
        scroll_y=Scrollbar(salary_f2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        self.txt_salary_reciept=Text(salary_f2,font=("Times New Roman",15),bg='lightgrey',yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,self.sample)
        
        self.btn_print=Button(salary_f,text='Print',state=DISABLED,command=self.print_,font=("Times New Roman",18,"bold"),bg='lightgrey',fg='black')
        self.btn_print.place(x=260,y=302,width=120,height=40)
        self.check_connection()
        
################################ all funtions ################################
                
       
    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='project')
            cur=con.cursor( )
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            rows=cur.fetchone()
            #print(rows)
            if rows==None:
                messagebox.showerror("Error","Invalid Eployee ID, please try another Eployee ID",parent=self.root)
            else:
                #print(rows)
                self.var_emp_code.set(rows[0])
                self.var_designation.set(rows[1])
                self.var_name.set(rows[2])
                self.var_age.set(rows[3])
                self.var_gender.set(rows[4])
                self.var_email.set(rows[5])
                self.var_location.set(rows[6])
                self.var_doj.set(rows[7])
                self.var_dob.set(rows[8])
                self.var_experience.set(rows[9])
                self.var_proof_id.set(rows[10]) 
                self.var_contact.set(rows[11])
                self.var_status.set(rows[12])
                self.txt_Address.delete('1.0',END)
                self.txt_Address.insert(END,rows[13])
                
       
                self.var_month.set(rows[14])
                self.var_year.set(rows[15])
                self.var_salary.set(rows[16])
                self.var_total_days.set(rows[17])
                self.var_absent.set(rows[18])
                self.var_medical.set(rows[19])
                self.var_pf.set(rows[20])
                self.var_convence.set(rows[21])
                self.var_net_salary.set(rows[22])
                file_=open('salary_reciept/'+str(rows[23]),'r')
                self.txt_salary_reciept.delete('1.0',END)      
                for i in file_:
                    self.txt_salary_reciept.insert(END,i)          
                file_.close()
                self.Save.config(state=DISABLED)
                self.Update.config(state=NORMAL)
                self.Delete.config(state=NORMAL)       
                self.txt_Employee_code.config(state='readonly') 
                self.btn_print.config(state=NORMAL)         
                
        except Exception as ex: 
            messagebox.showerror("Error",f'Error due to :{str(ex)}')        
        
    def clear(self):
        self.Save.config(state=NORMAL)
        self.Update.config(state=DISABLED)
        self.Delete.config(state=DISABLED)
        self.txt_Employee_code.config(state=NORMAL)       
        self.btn_print.config(state=DISABLED)   
        
        
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('') 
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_Address.delete('1.0',END)
        

        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_total_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')      
        self.txt_salary_reciept.delete('1.0',END) 
        self.txt_salary_reciept.insert(END,self.sample) 
        self.txt_
    def delete(self):
        if self.var_emp_code.get() =='':
            messagebox.showerror("Error","Employee ID required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='project')
                cur=con.cursor( )
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                rows=cur.fetchone()
                #print(rows)
                if rows==None:
                    messagebox.showerror("Error","Invalid employee ID, please try another employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    #print(op)
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))      
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Records deleted successfully",parent=self.root)
                        self.clear()
            except Exception as ex: 
                messagebox.showerror("Error",f'Error due to :{str(ex)}')     
                  
    def add(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee details are required")
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='project')
            cur=con.cursor( )
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            rows=cur.fetchone()
            #print(rows)
            if rows!=None:
                messagebox.showerror("Error","This employee ID is already available in our record",parent=self.root)
            else:
                cur.execute ("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (   self.var_emp_code.get(),
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_location.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(), 
                                self.var_contact.get(),
                                self.var_status.get(),
                                self.txt_Address.get('1.0',END),     
                        ##---------- variable for frame two ---------##
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_salary.get(),
                                self.var_total_days.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convence.get(),
                                self.var_net_salary.get(),
                                self.var_emp_code.get()+".txt"
                            ))
                            
                con.commit()
                con.close()
                file_=open('salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                file_.write(self.txt_salary_reciept.get('1.0',END))
                file_.close()
                messagebox.showinfo("Success","Record address succesfully")
                
        except Exception as ex: 
            messagebox.showerror("Error",f'Error due to :{str(ex)}')
        
    def update(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee details are required")
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='project')
            cur=con.cursor( )
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            rows=cur.fetchone()
            #print(rows)
            if rows==None:
                messagebox.showerror("Error","This Employee ID is invalid, try again with valid Eployee ID",parent=self.root)
            else:
                cur.execute ("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`total_days`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_slip`=%s WHERE `e_id`=%s",
                            (   
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_location.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof_id.get(), 
                                self.var_contact.get(),
                                self.var_status.get(),
                                self.txt_Address.get('1.0',END),    
                                 
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_salary.get(),
                                self.var_total_days.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convence.get(),
                                self.var_net_salary.get(),
                                self.var_emp_code.get()+".txt",
                                self.var_emp_code.get(),
                            ))
                            
                con.commit()
                con.close()
                file_=open('salary_reciept/'+str(self.var_emp_code.get())+".txt",'w')
                file_.write(self.txt_salary_reciept.get('1.0',END))
                file_.close()
                messagebox.showinfo("Success","Record updated succesfully")
                
        except Exception as ex: 
            messagebox.showerror("Error",f'Error due to :{str(ex)}')
        
        
        
        
    def calculate(self):
        
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='':
            messagebox.showerror('Error','All fields are required')    
        else:
            
            per_day=int(self.var_salary.get())/int(self.var_total_days.get()) 
            work_day=int(self.var_total_days.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal_ - deduct+addition
            self.var_net_salary.set(net_sal)
            self.txt_salary_reciept.delete('1.0',END)
            final_sample=f'''\tCompany Name, Titan\n\tAddress: Chandigarh 
------------------------------------------------------
Employee ID\t\t: {self.var_emp_code.get()}
Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()} 
Generated On\t\t: {str(time.strftime("%d-%m-%Y"))}
------------------------------------------------------
Total Days\t\t:  {self.var_total_days.get()} 
Total Present\t\t:  {str(int(self.var_total_days.get())-int(self.var_absent.get()))} 
Total Absent\t\t:  {self.var_absent.get()}
Convence\t\t:  Rs{self.var_convence.get()}
Medical\t\t:  Rs{self.var_medical.get()}
PF\t\t:  Rs{self.var_pf.get()}
Gross Payment\t\t:  Rs{self.var_salary.get()}
Net Salary\t\t:  Rs{self.var_net_salary.get()}
------------------------------------------------------
This is computer generated slip, not
required any signature 
'''         
            self.txt_salary_reciept.insert(END,final_sample)
            
            
            
        
    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='project')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to :{str(ex)}')
     
    def print_(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_reciept.get('1.0',END))
        os.startfile(file_,'print')
            
        
        
        
root=Tk()

obj=EmployeeSystem(root)
root.mainloop()
        
        
        
        
        
        