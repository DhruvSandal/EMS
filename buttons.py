from tkinter import*
root=Tk()

root.title("Buttons")

root.iconbitmap('minecraft.ico')

root.geometry('500x500')

def my_click():
    my_lable =Label(root, text= "welome to this program",fg='#B233FF').pack()
    
mybutton = Button(root, text="clIck kar", fg='#FF3371',bg='#D9F38F',padx=30,pady=30 ,command= my_click)
mybutton.pack()

e=Entry(root,width=50,fg='red').pack()  

button1=Button(root,text="Enter your email id",padx=30,bg='white',fg='#B233FF').pack()  

def clickme():
    mylabel1=Label(root,text="Hello " + e.get()).pack()

root.mainloop()

final_sample=f'''\tCompany Name, Titan\n\tAddress: Chandigarh
------------------------------------------------------
Employee ID\t\t: {self.var_emp_code.get()}
Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()} 
Generated On\t\t: {str(time.strftime("%d-%M-%Y"))}
------------------------------------------------------
Total Days\t\t:  {self.var_t_days.get()}
Total Present\t\t:  {str(int(self.var_total_days))-int(self.var_absent.get())}
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
            self.txt_salary_reciept.delete('1.0',END)
            self.txt_salary_reciept.insert(END,final_sample)