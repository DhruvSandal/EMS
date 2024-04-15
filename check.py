 def clear(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='project')
            cur=con.cursor( )
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            rows=cur.fetchone()
            #print(rows)
            if rows==None:
                messagebox.showerror("Error","Invalid employee ID, please try another employee ID",parent=self.root)
            else:
                self.var_emp_code.delete('1.0',END)
                self.var_designation.delete('1.0',END)
                self.var_name.delete('1.0',END)
                self.var_age.delete('1.0',END)
                self.var_gender.delete('1.0',END)
                self.var_email.delete('1.0',END)
                self.var_location.sdelete('1.0',END)
                self.var_doj.delete('1.0',END)
                self.var_dob.delete('1.0',END)
                self.var_experience.delete('1.0',END)
                self.var_proof_id.delete('1.0',END)
                self.var_contact.delete('1.0',END)
                self.var_status.delete('1.0',END)
                self.txt_Address.delete('1.0',END)
                    
                self.var_month.delete('1.0',END)
                self.var_year.delete('1.0',END)
                self.var_salary.delete('1.0',END)
                self.var_total_days.delete('1.0',END)
                self.var_absent.set(rows[18])
                self.var_medical.delete('1.0',END)
                self.var_pf.delete('1.0',END)
                self.var_convence.delete('1.0',END)
                self.var_net_salary.delete('1.0',END)
                file_=open('salary_reciept/'+str(rows[23]),'r')
                self.txt_salary_reciept.delete('1.0',END)      
                for i in file_:
                    self.txt_salary_reciept.insert(END,i)          
                file_.close()
                
                
        except Exception as ex: 
            messagebox.showerror("Error",f'Error due to :{str(ex)}')  