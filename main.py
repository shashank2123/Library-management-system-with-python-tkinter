# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:19:22 2020

@author: shash
"""
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkfont
import Login_page_function
from difflib import get_close_matches
from tkinter import ttk
import re
from datetime import date,timedelta

class home_page:
    def __init__(self,master):
        self.master=master
        self.headingFrame1 = Frame(self.master,bg="#333945",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        
        self.headingFrame2 = Frame(self.headingFrame1,bg="#EAF0F1")
        self.headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
        headingLabel = Label(self.headingFrame2, text="Welcome to ISE Library", fg='black',font='Times 12 bold')
        headingLabel.place(relx=0.2,rely=0.2, relwidth=0.6, relheight=0.5)
        
        self.font_button=tkfont.Font(size=12,weight='bold')
        
        self.btn1 = Button(self.master,text="Admin",bg='#7C81F7', fg='black',font=self.font_button,command=self.admin_button)
        self.btn1.place(relx=0.4,rely=0.3, relwidth=0.2,relheight=0.1)
        
        self.img=ImageTk.PhotoImage(Image.open('logo.png'))
        self.l4=Label(self.master,image=self.img,bg='#0067AD')
        self.l4.place(relx=0.27,rely=0.45,relwidth=0.45,relheight=0.4)
        
        self.btn3 = Button(self.master,text="Exit",bg='#7C81F7', fg='black',font=self.font_button,command=self.exit_button)
        self.btn3.place(relx=0.75,rely=0.8, relwidth=0.15,relheight=0.1)

    def exit_button(self):
        self.master.destroy()
    def admin_button(self):
        self.master.destroy()
        login_page()

class login_page:
    def __init__(self):
        self.log=Tk()
        self.log.config(bg='#EEDFF2')
        
        self.log.title('ISE Library Managment System')
        self.log.iconbitmap('lib-icon.ico')
        self.log.geometry('600x500+500+150')
        
        self.log.maxsize(800,700)
        
        self.bg_image=ImageTk.PhotoImage(Image.open('bg_im4.jpg'))
        self.canvas=Canvas(self.log,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        
        self.headingFrame1 = Frame(self.log,bg="#333945",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.1)
        
        self.headingFrame2 = Frame(self.headingFrame1,bg="#EAF0F1")
        self.headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
        self.headingLabel = Label(self.headingFrame2, text="Hello, Admin", fg='black',font='Times 12 bold')
        self.headingLabel.place(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.5)
        
        self.entryFrame=Frame(self.log,bg='#1C797B')
        self.entryFrame.place(relx=0.15,rely=0.25,relwidth=0.7,relheight=0.4)
        
        self.label1=Label(self.entryFrame,text='Name :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label1.place(relx=0.05,rely=0.1,relwidth=0.2,relheight=0.2)
        
        self.name_var=StringVar()    
        self.name_entry=Entry(self.entryFrame,bd=5,textvariable=self.name_var)
        self.name_entry.place(relx=0.27,rely=0.1,relwidth=0.6,relheight=0.2)
        
        self.label2=Label(self.entryFrame,text='Email ID :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label2.place(relx=0.05,rely=0.4,relwidth=0.2,relheight=0.2)
        
        self.email_id_var=StringVar()
        self.email_entry=Entry(self.entryFrame,bd=5,textvariable=self.email_id_var)
        self.email_entry.place(relx=0.27,rely=0.4,relwidth=0.6,relheight=0.2)
        
        self.label3=Label(self.entryFrame,text='Password :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label3.place(relx=0.05,rely=0.7,relwidth=0.2,relheight=0.2)
        
        self.password_var=StringVar()
        self.password_entry=Entry(self.entryFrame,bd=5,textvariable=self.password_var)
        self.password_entry.place(relx=0.27,rely=0.7,relwidth=0.6,relheight=0.2)
        
        self.font_button=tkfont.Font(size=14,weight='bold')
        
        self.b1 = Button(self.log,text="login",bg='#7C81F7', fg='black',bd=3,font=self.font_button,command=self.login_commad)
        self.b1.place(relx=0.1,rely=0.7, relwidth=0.2,relheight=0.1)
        
    
        self.b3 = Button(self.log,text="Cancel",bg='#7C81F7', fg='black',bd=3,font=self.font_button,command=self.cancel_log_command)
        self.b3.place(relx=0.7,rely=0.7, relwidth=0.2,relheight=0.1)
        
        self.log.mainloop()

    def check_all_filled(self):
        if self.name_var.get()=='' and self.email_id_var.get()=='' and self.password_var.get()=='' :
            messagebox.showinfo('Message','Enter your name,E-mail,password')
        elif self.name_var.get()=='' and self.email_id_var.get()=='':
            messagebox.showinfo('Message','Enter your name,E-mail')
        elif self.name_var.get()=='' and self.password_var.get()=='':
             messagebox.showinfo('Message','Enter your name,password')              
        elif self.email_id_var.get()=='' and self.password_var.get()=='':
             messagebox.showinfo('Message','Enter your E-mail,password')
        elif self.email_id_var.get()=='':
            messagebox.showinfo('Message','Enter your E-mail')
        elif self.password_var.get()=='':
            messagebox.showinfo('Message','Enter your password')
        else:
            messagebox.showinfo('Message','Enter your name')
    def cancel_log_command(self):
        self.log.destroy()
    
    
    def login_commad(self):       
        if self.name_var.get()!='' and self.email_id_var.get()!='' and self.password_var.get()!='':
            emailRegex=re.compile(r'''[A-Za-z0-9%+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}''')
            if emailRegex.search(self.email_id_var.get()) != None:
                if self.email_id_var.get()!='admin@gmail.com':
                    messagebox.showerror('Message','incorrect E-mail')
                else:
                    self.check_password()
                    
            else:
                messagebox.showinfo('Message','invalid E-mail')
        else:            
            self.check_all_filled()
    def check_password(self):
        if 'password123'==self.password_var.get():
            messagebox.showinfo('Message','You Log-in Successfully  ')
            self.log.destroy()
            Menu_page()
        else:
            messagebox.showerror('Message','incorrect password')
        
class Menu_page:
    def __init__(self):
        self.emp_menu=Tk()
        self.emp_menu.geometry('600x500+500+150')
        self.emp_menu.config(bg='#28BFF5')
        self.emp_menu.title('ISE Library Managment System')
        self.emp_menu.iconbitmap('lib-icon.ico')
        self.emp_menu.geometry('600x500+500+150')
        self.emp_menu.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('bg_im3.jpg'))
        self.canvas=Canvas(self.emp_menu,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.headingFrame1 = Frame(self.emp_menu,bg="#333945",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.1)
        self.headingFrame2 = Frame(self.headingFrame1,bg="#EAF0F1")
        self.headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        self.headingLabel = Label(self.headingFrame2, text="Menu", fg='black',font='Times 18 bold')
        self.headingLabel.place(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.5)
        self.new_book_img=ImageTk.PhotoImage(Image.open('new_book.png'))
        self.new_book_button=Button(self.emp_menu,image=self.new_book_img,bg='white',command=self.new_book_command)
        self.new_book_button.place(relx=0.05,rely=0.25,relwidth=0.1,relheight=0.1)
        self.new_book_label=Label(self.emp_menu,text='New Book',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.new_book_label.place(relx=0.05,rely=0.35,relwidth=0.1,relheight=0.05)
        self.new_std_img=ImageTk.PhotoImage(Image.open('new_student.png'))
        self.new_std_button=Button(self.emp_menu,image=self.new_std_img,bg='white',command=self.new_std_command)
        self.new_std_button.place(relx=0.45,rely=0.25,relwidth=0.1,relheight=0.1)
        self.new_std_label=Label(self.emp_menu,text='New student',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.new_std_label.place(relx=0.43,rely=0.35,relwidth=0.15,relheight=0.05)
        self.search_img=ImageTk.PhotoImage(Image.open('search.png'))
        self.search_button=Button(self.emp_menu,image=self.search_img,bg='white',command=self.search_command)
        self.search_button.place(relx=0.85,rely=0.25,relwidth=0.1,relheight=0.1)
        self.search_label=Label(self.emp_menu,text='Search',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.search_label.place(relx=0.85,rely=0.35,relwidth=0.1,relheight=0.05)
        self.issue_img=ImageTk.PhotoImage(Image.open('issue.jpg'))
        self.issue_button=Button(self.emp_menu,image=self.issue_img,bg='white',command=self.issue_command)
        self.issue_button.place(relx=0.05,rely=0.45,relwidth=0.1,relheight=0.1)
        self.issue_label=Label(self.emp_menu,text='Issue',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.issue_label.place(relx=0.05,rely=0.55,relwidth=0.1,relheight=0.05)
        self.renewal_img=ImageTk.PhotoImage(Image.open('renewal.png'))
        self.renewal_button=Button(self.emp_menu,image=self.renewal_img,bg='white',command=self.renewal_command)
        self.renewal_button.place(relx=0.45,rely=0.45,relwidth=0.1,relheight=0.1)
        self.renewal_label=Label(self.emp_menu,text='Renewal',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.renewal_label.place(relx=0.45,rely=0.55,relwidth=0.1,relheight=0.05)
        self.return_img=ImageTk.PhotoImage(Image.open('return.png'))
        self.return_button=Button(self.emp_menu,image=self.return_img,bg='white',command=self.return_command)
        self.return_button.place(relx=0.85,rely=0.45,relwidth=0.1,relheight=0.1)
        self.return_label=Label(self.emp_menu,text='Return',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.return_label.place(relx=0.85,rely=0.55,relwidth=0.1,relheight=0.05)
        self.history_img=ImageTk.PhotoImage(Image.open('history.png'))
        self.history_button=Button(self.emp_menu,image=self.history_img,bg='white',command=self.history_command)
        self.history_button.place(relx=0.05,rely=0.65,relwidth=0.1,relheight=0.1)
        self.history_label=Label(self.emp_menu,text='History',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.history_label.place(relx=0.05,rely=0.75,relwidth=0.1,relheight=0.05)
        self.details_img=ImageTk.PhotoImage(Image.open('details.png'))
        self.details_button=Button(self.emp_menu,image=self.details_img,bg='white',command=self.fine_command)
        self.details_button.place(relx=0.45,rely=0.65,relwidth=0.1,relheight=0.1)
        self.details_label=Label(self.emp_menu,text='Fine',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.details_label.place(relx=0.45,rely=0.75,relwidth=0.1,relheight=0.05)
        self.profile_img=ImageTk.PhotoImage(Image.open('profile.png'))
        self.profile_button=Button(self.emp_menu,image=self.profile_img,bg='white',command=self.profile_command)
        self.profile_button.place(relx=0.85,rely=0.65,relwidth=0.1,relheight=0.1)
        self.profile_label=Label(self.emp_menu,text='Profile',fg='black',font='Times 8 bold',bg='#D8F18A')
        self.profile_label.place(relx=0.85,rely=0.75,relwidth=0.1,relheight=0.05)
        self.back=Button(self.emp_menu,text='<=Back',fg='white',bg='black',bd=3,font='Times 10 bold',command=self.back_command)
        self.back.place(relx=0.45,rely=0.85,relwidth=0.1,relheight=0.05)
        self.emp_menu.mainloop()
    def back_command(self):
        self.emp_menu.destroy()
        login_page()
    def new_book_command(self):
        self.emp_menu.destroy()
        new_book_page()
    def new_std_command(self):
        self.emp_menu.destroy()
        new_std_page()  
    def search_command(self):
        self.emp_menu.destroy()
        search_page()  
    def issue_command(self):
        self.emp_menu.destroy()
        issue_page()
    def renewal_command(self):
        self.emp_menu.destroy()
        renewal_page()        
    def return_command(self):
        self.emp_menu.destroy()
        return_page() 
    def history_command(self):
        self.emp_menu.destroy()
        history_page()
    def fine_command(self):
        self.emp_menu.destroy()
        fine_page()
    def profile_command(self):
        self.emp_menu.destroy()
        profile_page()
        
class new_book_page:
    def __init__(self):
        self.new_book=Tk()
        self.new_book.config(bg='#EEDFF2')
        self.new_book.title('ISE Library Managment System')
        self.new_book.iconbitmap('lib-icon.ico')
        self.new_book.geometry('600x500+500+150')
        self.new_book.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.new_book,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.entryFrame=Frame(self.new_book,bg='#8D9A99')
        self.entryFrame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.7)
        self.label1=Label(self.entryFrame,text='Title  :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.1)
        self.title_var=StringVar()
        self.entry1=Entry(self.entryFrame,bd=5,textvariable=self.title_var)
        self.entry1.place(relx=0.3,rely=0.1,relwidth=0.6,relheight=0.1)
        self.label2=Label(self.entryFrame,text='ID    :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label2.place(relx=0.1,rely=0.25,relwidth=0.2,relheight=0.1)
        self.id_var=StringVar()
        self.entry2=Entry(self.entryFrame,bd=5,textvariable=self.id_var)
        self.entry2.place(relx=0.3,rely=0.25,relwidth=0.6,relheight=0.1)
        self.label3=Label(self.entryFrame,text='Author :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label3.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.1)
        self.author_var=StringVar()
        self.entry3=Entry(self.entryFrame,bd=5,textvariable=self.author_var)
        self.entry3.place(relx=0.3,rely=0.4,relwidth=0.6,relheight=0.1)
        self.label4=Label(self.entryFrame,text='Subject :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label4.place(relx=0.1,rely=0.55,relwidth=0.2,relheight=0.1)
        self.subject_var=StringVar()
        self.entry4=Entry(self.entryFrame,bd=5,textvariable=self.subject_var)
        self.entry4.place(relx=0.3,rely=0.55,relwidth=0.6,relheight=0.1)
        self.label5=Label(self.entryFrame,text='ISBN  :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label5.place(relx=0.1,rely=0.7,relwidth=0.2,relheight=0.1)
        self.isbn_var=StringVar()
        self.entry5=Entry(self.entryFrame,bd=5,textvariable=self.isbn_var)
        self.entry5.place(relx=0.3,rely=0.7,relwidth=0.6,relheight=0.1)
        self.submit = Button(self.new_book,text="Submit", fg='black',bd=3,font='Times 9 bold',command=self.submit_command)
        self.submit.place(relx=0.1,rely=0.8, relwidth=0.15,relheight=0.07)
        self.cancel = Button(self.new_book,text="Cancel", fg='black',bd=3,font='Times 9 bold',command=self.cancel_command)
        self.cancel.place(relx=0.7,rely=0.8, relwidth=0.15,relheight=0.07)
        self.new_book.mainloop()
    
    def cancel_command(self):
        self.new_book.destroy()
        Menu_page()
    def submit_command(self):
        if self.title_var.get()!='' and self.id_var.get()!=0 and self.author_var.get()!='' and self.subject_var.get()!='' and self.isbn_var.get()!='':
            verify_id=str(self.id_var.get())
            if verify_id.isdigit() and len(verify_id)==5:
                if Login_page_function.get_book_from_id(int(self.id_var.get()))==[]:
                    Login_page_function.insert_new_book(self.title_var.get(),int(self.id_var.get()),self.author_var.get(),self.subject_var.get(),self.isbn_var.get(),'yes')
                    messagebox.showinfo('Message','Title:- {} id :-{} Author :- {} Subject :- {} ISBN :-{}  added succesfully'.format(self.title_var.get(),int(self.id_var.get()),self.author_var.get(),self.subject_var.get(),self.isbn_var.get()))
                else:
                    messagebox.showinfo('Message','id already exist')
                
            else:
                messagebox.showerror('Message','invalid id')
                
        else:
            messagebox.showinfo('Message','Please fill all entries')
 
        
 
    
class new_std_page:
    def __init__(self):
        self.new_student=Tk()
        self.new_student.config(bg='#EEDFF2')
        self.new_student.title('ISE Library Managment System')
        self.new_student.iconbitmap('lib-icon.ico')
        self.new_student.geometry('600x500+500+150')
        self.new_student.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.new_student,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.entryFrame=Frame(self.new_student,bg='#8D9A99')
        self.entryFrame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.7)
        self.label1=Label(self.entryFrame,text='Name  :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.1)
        self.std_name_var=StringVar()
        self.entry1=Entry(self.entryFrame,bd=5,textvariable=self.std_name_var)
        self.entry1.place(relx=0.3,rely=0.1,relwidth=0.6,relheight=0.1)
        self.label2=Label(self.entryFrame,text='USN   :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label2.place(relx=0.1,rely=0.25,relwidth=0.2,relheight=0.1)
        self.usn_var=StringVar()
        self.entry2=Entry(self.entryFrame,bd=5,textvariable=self.usn_var)
        self.entry2.place(relx=0.3,rely=0.25,relwidth=0.6,relheight=0.1)
        self.label3=Label(self.entryFrame,text='Email ID :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label3.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.1)
        self.std_email_var=StringVar()
        self.entry3=Entry(self.entryFrame,bd=5,textvariable=self.std_email_var)
        self.entry3.place(relx=0.3,rely=0.4,relwidth=0.6,relheight=0.1)
        self.label4=Label(self.entryFrame,text='DOB(dd/mm/yyyy):',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label4.place(relx=0.1,rely=0.55,relwidth=0.2,relheight=0.1)
        self.std_dob_var=StringVar()
        self.entry4=Entry(self.entryFrame,bd=5,textvariable=self.std_dob_var)
        self.entry4.place(relx=0.3,rely=0.55,relwidth=0.6,relheight=0.1)
        self.label5=Label(self.entryFrame,text='Semester :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label5.place(relx=0.1,rely=0.7,relwidth=0.15,relheight=0.1)
        self.std_sem_var=StringVar()
        self.entry5=Entry(self.entryFrame,bd=5,textvariable=self.std_sem_var)
        self.entry5.place(relx=0.25,rely=0.7,relwidth=0.2,relheight=0.1)
        self.label5=Label(self.entryFrame,text='Section :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label5.place(relx=0.55,rely=0.7,relwidth=0.15,relheight=0.1)
        self.std_sec_var=StringVar()
        self.entry5=Entry(self.entryFrame,bd=5,textvariable=self.std_sec_var)
        self.entry5.place(relx=0.7,rely=0.7,relwidth=0.2,relheight=0.1)
        self.submit = Button(self.new_student,text="Register", fg='black',bd=3,font='Times 9 bold',command=self.register_command)
        self.submit.place(relx=0.1,rely=0.8, relwidth=0.15,relheight=0.07)
        self.cancel = Button(self.new_student,text="Cancel", fg='black',bd=3,font='Times 9 bold',command=self.std_cancel_command)
        self.cancel.place(relx=0.75,rely=0.8, relwidth=0.15,relheight=0.07)
        self.new_student.mainloop()

    def std_cancel_command(self):
        self.new_student.destroy()
        Menu_page() 
    def register_command(self):
        if self.std_name_var.get()!='' and self.usn_var.get()!='' and self.std_email_var.get()!='' and self.std_dob_var.get()!='' and self.std_sem_var.get()!='' and self.std_sec_var.get()!='' :
            usn_Regex=re.compile('\dDS\d\dIS\d\d\d')
            if usn_Regex.search(self.usn_var.get())!=None:
                emailRegex=re.compile(r'''[A-Za-z0-9%+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}''')
                if emailRegex.search(self.std_email_var.get()) != None :
                    dobRegex=re.compile(r'\d\d/\d\d/\d\d\d\d')
                    if dobRegex.search(self.std_dob_var.get()) != None :
                        if self.std_sem_var.get().isdigit() and len(self.std_sem_var.get())==1:
                            if str(self.std_sec_var.get()).isalpha():
                                if Login_page_function.get_details_by_usn(self.usn_var.get())==[]:
                                    if Login_page_function.get_details_by_email(self.std_email_var.get())==[]:
                                        Login_page_function.student_details(self.std_name_var.get(),self.usn_var.get(),self.std_email_var.get(),self.std_dob_var.get(),int(self.std_sem_var.get()),self.std_sec_var.get().upper(),0,0,0,0)
                                        messagebox.showinfo('Message','{} Registration Completed'.format(self.usn_var.get()))
                                    else:
                                        messagebox.showerror('Message','this Email is already registered with different usn!!')
                                        
                                    
                                else:
                                    messagebox.showerror('Message','this usn is already registered !!')
                            else:
                                messagebox.showinfo('Message','invalid Section !!')
                                
                        else:
                            messagebox.showinfo('Message','invalid semester !!')
                        
                    else:
                        messagebox.showinfo('Message','Invalid DOB !!')
                         
                
                else:
                    messagebox.showinfo('Message','Invalid E-mail id !!')

            else:
                messagebox.showinfo('Message','Invalid usn !!')
                
        else:
            messagebox.showinfo('Message','Please fill all entries')
        
 
class search_page:
    def __init__(self):
        self.search_tk=Tk()
        self.search_tk.config(bg='#F9F7B0')
        self.search_tk.title('ISE Library Managment System')
        self.search_tk.iconbitmap('lib-icon.ico')
        self.search_tk.geometry('600x500+500+150')
        self.search_tk.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.search_tk,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)      
        self.search_button=Button(self.search_tk,text='Search',fg='black',font='Times 10 bold',bd=2,command=self.search_button_command)
        self.search_button.place(relx=0.8,rely=0.05,relwidth=0.15,relheight=0.075)
        self.item_var=StringVar()        
        self.search_entry=Entry(self.search_tk,bd=5,textvariable=self.item_var)
        self.search_entry.place(relx=0.1,rely=0.05,relwidth=0.7,relheight=0.075)        
        self.r=StringVar()
        self.r.set('id')       
        Radiobutton(self.search_tk,text='ID',font='Times 12 bold',variable=self.r,value='id').place(relx=0.05,rely=0.2,relwidth=0.15,relheight=0.07)
        Radiobutton(self.search_tk,text='Subject',font='Times 12 bold',variable=self.r,value='subject').place(relx=0.3,rely=0.2,relwidth=0.15,relheight=0.07)
        Radiobutton(self.search_tk,text='Title',font='Times 12 bold',variable=self.r,value='title').place(relx=0.55,rely=0.2,relwidth=0.15,relheight=0.07)
        Radiobutton(self.search_tk,text='Author',font='Times 12 bold',variable=self.r,value='author').place(relx=0.8,rely=0.2,relwidth=0.15,relheight=0.07)
        self.result_text=Text(self.search_tk,fg='white',bg='black')
        self.result_text.place(relx=0.02,rely=0.3,relwidth=0.96,relheight=0.6)
        self.back=Button(self.search_tk,text='<=Back',bd=5,font='Times 10 bold',command=self.search_back_command)
        self.back.place(relx=0.45,rely=0.92,relwidth=0.1,relheight=0.05)          
        self.search_tk.mainloop()
                
    def search_back_command(self):
        self.search_tk.destroy()
        Menu_page() 
    
    def search_button_command(self):
        if self.item_var.get()!='':
            if self.r.get()=='id':
                self.search_by_id()
            elif self.r.get()=='title':
                self.search_by_title()
            elif self.r.get()=='author':
                self.search_by_author()
            else:
                self.search_by_subject()
        else:
            messagebox.showinfo('Message','Fill the entry')
            
    
    def search_by_id(self):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.config(state=DISABLED)
        book_id=str(self.item_var.get())
        if book_id.isdigit() and len(book_id)==5:
            result=Login_page_function.get_book_from_id(int(self.item_var.get()))
            if result!=[]:
                self.text_output_id(result)
                
            else:
                messagebox.showinfo('Message','Not found')
        else:
            messagebox.showinfo('Message','invalid id')
        
    def text_output_id(self,row):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.see(END)
        self.result_text.insert(END,'\tName\t\t\tAuthor\t  Subject\t   ISBN    Status\n')
        self.result_text.insert(END,'-'*71+'\n')
        for bk in row:
            self.result_text.insert(END,'{}\t\t{}\t\t{}\t\t{}\t\t{}\n'.format(bk[0],bk[2],bk[3],bk[4],bk[5]))
        self.result_text.config(state=DISABLED)
    
    def search_by_title(self):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.config(state=DISABLED)
        all_titles_list=Login_page_function.get_all_title()
        all_titles=[]
        for it in all_titles_list:
            all_titles.append(it[0])
        matched_titles=get_close_matches(self.item_var.get(),all_titles)
        if matched_titles!=[]:
            self.result_text.config(state=NORMAL)
            self.result_text.see(END)
            self.result_text.insert(END,'\tName\t\t\tID\tAuthor\tSubject\tISBN\tStatus\n')
            self.result_text.insert(END,'-'*71+'\n')
            for values in matched_titles:
                title_result=Login_page_function.get_book_from_title(values)
                for bk in title_result:
                    self.result_text.insert(END,'{}\t\t\t{}\t{}\t{}\t{}\t{}\n'.format(bk[0],bk[1],bk[2],bk[3],bk[4],bk[5]))
            self.result_text.config(state=DISABLED)
        else:
            messagebox.showinfo('Message','Not found')

    def search_by_author(self):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.config(state=DISABLED)
        all_author_list=Login_page_function.get_all_author()
        all_author=[]
        for it in all_author_list:
            all_author.append(it[0])
        matched_author=get_close_matches(self.item_var.get(),all_author)
        if matched_author!=[]:
            self.result_text.config(state=NORMAL)
            self.result_text.see(END)
            self.result_text.insert(END,'\tName\t\t\tID\tAuthor\tSubject\tISBN\tStatus\n')
            self.result_text.insert(END,'-'*71+'\n')
            for values in matched_author:
                author_result=Login_page_function.get_book_from_author(values)
                for bk in author_result:
                    self.result_text.insert(END,'{}\t\t\t{}\t{}\t{}\t{}\t{}\n'.format(bk[0],bk[1],bk[2],bk[3],bk[4],bk[5]))
            self.result_text.config(state=DISABLED)
        else:
            messagebox.showinfo('Message','Not found')      
      
            
    def search_by_subject(self):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.config(state=DISABLED)
        all_subject_list=Login_page_function.get_all_subject()
        all_subject=[]
        for it in all_subject_list:
            all_subject.append(it[0])
        matched_subject=get_close_matches(self.item_var.get(),all_subject)
        if matched_subject!=[]:
            self.result_text.config(state=NORMAL)
            self.result_text.see(END)
            self.result_text.insert(END,'\tName\t\t\tID\tAuthor\tSubject\tISBN\tStatus\n')
            self.result_text.insert(END,'-'*71+'\n')
            for values in matched_subject:
                subject_result=Login_page_function.get_book_from_subject(values)
                for bk in subject_result:
                    self.result_text.insert(END,'{}\t\t\t{}\t{}\t{}\t{}\t{}\n'.format(bk[0],bk[1],bk[2],bk[3],bk[4],bk[5]))
            self.result_text.config(state=DISABLED)
        else:
            messagebox.showinfo('Message','Not found')
 
class issue_page:
    def __init__(self):
        self.issue_tk=Tk()
        self.issue_tk.config(bg='#EEDFF2')
        self.issue_tk.title('ISE Library Managment System')
        self.issue_tk.iconbitmap('lib-icon.ico')
        self.issue_tk.geometry('600x500+500+150')
        self.issue_tk.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.issue_tk,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.entryFrame=Frame(self.issue_tk,bg='#8D9A99')
        self.entryFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.3)
        self.label1=Label(self.entryFrame,text='ID  :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.2)
        self.issue_id_var=StringVar()
        self.entry1=Entry(self.entryFrame,bd=5,textvariable=self.issue_id_var)
        self.entry1.place(relx=0.3,rely=0.1,relwidth=0.6,relheight=0.2)
        self.label2=Label(self.entryFrame,text='USN    :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label2.place(relx=0.1,rely=0.6,relwidth=0.2,relheight=0.2)
        self.issue_usn_var=StringVar()
        self.entry2=Entry(self.entryFrame,bd=5,textvariable=self.issue_usn_var)
        self.entry2.place(relx=0.3,rely=0.6,relwidth=0.6,relheight=0.2)
        self.submit = Button(self.issue_tk,text="Issue", fg='black',bd=3,font='Times 9 bold',command=self.issue_command)
        self.submit.place(relx=0.1,rely=0.7, relwidth=0.15,relheight=0.07)
        self.cancel = Button(self.issue_tk,text="Cancel", fg='black',bd=3,font='Times 9 bold',command=self.issue_cancel_command)
        self.cancel.place(relx=0.75,rely=0.7, relwidth=0.15,relheight=0.07)
        self.issue_tk.mainloop()
        
    def issue_cancel_command(self):
        self.issue_tk.destroy()
        Menu_page()
    
    def issue_command(self):
        if self.issue_id_var.get() !='' and self.issue_usn_var.get() !='':
            usn_Regex=re.compile('\dDS\d\dIS\d\d\d')
            if usn_Regex.search(self.issue_usn_var.get())!=None and str(self.issue_id_var.get()).isdigit() and len(self.issue_id_var.get())==5:
                if Login_page_function.get_book_from_id(int(self.issue_id_var.get()))!=[]:
                    if Login_page_function.get_details_by_usn(self.issue_usn_var.get())!=[]:
                        self.issue_by_number()
                    else:
                        messagebox.showinfo('Message','usn is not registered')
                else:
                    messagebox.showinfo('Messasge','book is not found')
            else:
                messagebox.showinfo('Message','Invalid USN or ID')
        else:
            messagebox.showinfo('Message','Please all Entries')
    def issue_by_number(self):
        if Login_page_function.get_status(int(self.issue_id_var.get()))=='yes':
            b=Login_page_function.get_b_by_usn(self.issue_usn_var.get())
            b=b[0]
            if b[0]==0:
                Login_page_function.update_b1(self.issue_usn_var.get(),int(self.issue_id_var.get()))
                Login_page_function.update_status('no', int(self.issue_id_var.get()))
                Login_page_function.issue_details(str(date.today()),str(date.today()+timedelta(15)),int(self.issue_id_var.get()),self.issue_usn_var.get())
                Login_page_function.history_insert(int(self.issue_id_var.get()),self.issue_usn_var.get(),'ISSUED')
                messagebox.showinfo('Message','Book {} is issued to {}'.format(self.issue_id_var.get(),self.issue_usn_var.get()))
            elif b[1]==0:
                Login_page_function.update_b2(self.issue_usn_var.get(),int(self.issue_id_var.get()))
                Login_page_function.update_status('no', int(self.issue_id_var.get()))
                Login_page_function.issue_details(str(date.today()),str(date.today()+timedelta(15)),int(self.issue_id_var.get()),self.issue_usn_var.get())
                Login_page_function.history_insert(self.issue_usn_var.get(),int(self.issue_id_var.get()),'ISSUED')
                messagebox.showinfo('Message','Book {} is issued to {}'.format(self.issue_id_var.get(),self.issue_usn_var.get()))
            elif b[2]==0:
                Login_page_function.update_b3(self.issue_usn_var.get(),int(self.issue_id_var.get()))
                Login_page_function.update_status('no', int(self.issue_id_var.get()))
                Login_page_function.issue_details(str(date.today()),str(date.today()+timedelta(15)),int(self.issue_id_var.get()),self.issue_usn_var.get())
                Login_page_function.history_insert(self.issue_usn_var.get(),int(self.issue_id_var.get()),'ISSUED')
                messagebox.showinfo('Message','Book {} is issued to {}'.format(self.issue_id_var.get(),self.issue_usn_var.get()))
            else:
                messagebox.showinfo('Message','book limit is execeded')
        else:
            messagebox.showinfo('Message','book is not available')
        
 
class renewal_page:
    def __init__(self):
        self.renewal_tk=Tk()
        self.renewal_tk.config(bg='#EEDFF2')
        self.renewal_tk.title('ISE Library Managment System')
        self.renewal_tk.iconbitmap('lib-icon.ico')
        self.renewal_tk.geometry('600x500+500+150')
        self.renewal_tk.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.renewal_tk,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.entryFrame=Frame(self.renewal_tk,bg='#8D9A99')
        self.entryFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.3)
        self.label1=Label(self.entryFrame,text='ID  :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.2)
        self.renewal_id_var=StringVar()
        self.entry1=Entry(self.entryFrame,bd=5,textvariable=self.renewal_id_var)
        self.entry1.place(relx=0.3,rely=0.1,relwidth=0.6,relheight=0.2)
        self.label2=Label(self.entryFrame,text='USN    :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label2.place(relx=0.1,rely=0.6,relwidth=0.2,relheight=0.2)
        self.renewal_usn_var=StringVar()
        self.entry2=Entry(self.entryFrame,bd=5,textvariable=self.renewal_usn_var)
        self.entry2.place(relx=0.3,rely=0.6,relwidth=0.6,relheight=0.2)
        self.submit = Button(self.renewal_tk,text="Renewal", fg='black',bd=3,font='Times 9 bold',command=self.submit_command)
        self.submit.place(relx=0.1,rely=0.8, relwidth=0.15,relheight=0.07)
        self.cancel = Button(self.renewal_tk,text="Cancel", fg='black',bd=3,font='Times 9 bold',command=self.renewal_cancel_command)
        self.cancel.place(relx=0.75,rely=0.8, relwidth=0.15,relheight=0.07)  
        self.renewal_tk.mainloop()
    def renewal_cancel_command(self):
        self.renewal_tk.destroy()
        Menu_page()
    def submit_command(self):
        if self.renewal_id_var.get() !='' and self.renewal_usn_var.get() !='':
            usn_Regex=re.compile('\dDS\d\dIS\d\d\d')
            if usn_Regex.search(self.renewal_usn_var.get())!=None and str(self.renewal_id_var.get()).isdigit() and len(self.renewal_id_var.get())==5:
                if Login_page_function.get_book_from_id(int(self.renewal_id_var.get()))!=[]:
                    if Login_page_function.get_details_by_usn(self.renewal_usn_var.get())!=[]:
                        self.renewal_by_number()
                    else:
                        messagebox.showinfo('Message','usn is not registered')
                else:
                    messagebox.showinfo('Messasge','book is not found')
            else:
                messagebox.showinfo('Message','Invalid USN or ID')
        else:
            messagebox.showinfo('Message','Please all Entries')
 
    def renewal_by_number(self):
        details=Login_page_function.get_issue_details(int(self.renewal_id_var.get()))
        if details!=[]:
            if details[0][3]==self.renewal_usn_var.get():
                temp1=date.fromisoformat(details[0][1]) 
                temp2=date.today()
                fine_days=temp2-temp1
                var_fine=fine_days.days
                if var_fine<0:
                    var_fine=0
                old_fine=Login_page_function.get_fine(self.renewal_usn_var.get())
                new_fine=old_fine+var_fine
                Login_page_function.update_fine(self.renewal_usn_var.get(),new_fine)
                Login_page_function.update_date(str(date.today()),str(date.today()+timedelta(15)),int(self.renewal_id_var.get()))
                Login_page_function.history_insert(int(self.renewal_id_var.get()),self.renewal_usn_var.get(),'renewal')
                messagebox.showinfo('message','Renewal of book {} is successful'.format(self.renewal_id_var.get()))
            else:
                messagebox.showerror('Message',"given usn does not match with issued usn" )
        else:
            messagebox.showerror('Message','Book is not issued')
            
 
    
class return_page:
    def __init__(self):
        self.return_tk=Tk()
        self.return_tk.config(bg='#EEDFF2')
        self.return_tk.title('ISE Library Managment System')
        self.return_tk.iconbitmap('lib-icon.ico')
        self.return_tk.geometry('600x500+500+150')
        self.return_tk.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.return_tk,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.entryFrame=Frame(self.return_tk,bg='#8D9A99')
        self.entryFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.3)
        self.label1=Label(self.entryFrame,text='ID  :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.2)
        self.return_id_var=StringVar()
        self.entry1=Entry(self.entryFrame,bd=5,textvariable=self.return_id_var)
        self.entry1.place(relx=0.3,rely=0.1,relwidth=0.6,relheight=0.2)
        self.label2=Label(self.entryFrame,text='USN    :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label2.place(relx=0.1,rely=0.6,relwidth=0.2,relheight=0.2)
        self.return_usn_var=StringVar()
        self.entry2=Entry(self.entryFrame,bd=5,textvariable=self.return_usn_var)
        self.entry2.place(relx=0.3,rely=0.6,relwidth=0.6,relheight=0.2)
        self.submit = Button(self.return_tk,text="Return", fg='black',bd=3,font='Times 9 bold',command=self.return_submit)
        self.submit.place(relx=0.1,rely=0.8, relwidth=0.15,relheight=0.07)
        self.cancel = Button(self.return_tk,text="Cancel", fg='black',bd=3,font='Times 9 bold',command=self.return_cancel_command)
        self.cancel.place(relx=0.75,rely=0.8, relwidth=0.15,relheight=0.07)  
        self.return_tk.mainloop()
    def return_cancel_command(self):
        self.return_tk.destroy()
        Menu_page()  
    def return_submit(self):
        details=Login_page_function.get_issue_details(int(self.return_id_var.get()))
        if details!=[]:
            if details[0][3]==self.return_usn_var.get():
                temp1=date.fromisoformat(details[0][1])
                temp2=date.today()
                fine_days=temp2-temp1
                var_fine=fine_days.days
                print(temp1,temp2,fine_days,var_fine)
                if var_fine<0:
                    var_fine=0
                old_fine=Login_page_function.get_fine(self.return_usn_var.get())
                new_fine=old_fine+var_fine
                print(new_fine,old_fine,var_fine)
                Login_page_function.update_fine(self.return_usn_var.get(),new_fine)
                Login_page_function.delete_issue(int(self.return_id_var.get()))
                Login_page_function.update_status('yes',int(self.return_id_var.get()))
                Login_page_function.history_insert(int(self.return_id_var.get()),self.return_usn_var.get(),'Return')
                self.update_books()
            else:
                messagebox.showerror('Message',"given usn does not match with issued usn" )
        else:
            messagebox.showerror('Message','Book is not issued')
        
        
    def update_books(self):
        all_b=Login_page_function.get_b_by_usn(self.return_usn_var.get())
        all_b=all_b[0]
        if all_b[0]==int(self.return_id_var.get()):
            Login_page_function.update_b1(self.return_usn_var.get(),0)
            messagebox.showinfo('message','book {} is successful returned'.format(self.return_id_var.get()))
        elif all_b[2]==int(self.return_id_var.get()):
            Login_page_function.update_b2(self.return_usn_var.get(),0)
            messagebox.showinfo('message','book {} is successful returned'.format(self.return_id_var.get()))
        else:
            Login_page_function.update_b2(self.return_usn_var.get(),0)
            messagebox.showinfo('message','book {} is successful returned'.format(self.return_id_var.get()))

class history_page:
    def __init__(self):
        self.history_tk=Tk()
        self.history_tk.config(bg='#EEDFF2')
        self.history_tk.title('ISE Library Managment System')
        self.history_tk.iconbitmap('lib-icon.ico')
        self.history_tk.geometry('600x500+500+150')
        self.history_tk.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.history_tk,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.headingFrame1 = Frame(self.history_tk,bg="#333945",bd=5)
        self.headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.1)
        self.headingFrame2 = Frame(self.headingFrame1,bg="#EAF0F1")
        self.headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        self.headingLabel = Label(self.headingFrame2, text="History", fg='black',font='Times 12 bold')
        self.headingLabel.place(relx=0.2,rely=0.2, relwidth=0.6, relheight=0.5)
        self.date_label=Label(text='Date',bd=3).place(relx=0.1,rely=0.2,relwidth=0.1,relheight=0.05)
        today_str=str(date.today())
        today_list=today_str.split('-')
        self.date_var=StringVar()
        self.date_var.set(today_list[2])
        self.date_option=[ '01',  '02',  '03',  '04',  '05',  '06',  '07',  '08',  '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        self.cb1=ttk.Combobox(self.history_tk,state="readonly",values=self.date_option,textvariable=self.date_var).place(relx=0.23,rely=0.2,relwidth=0.1,relheight=0.05)
        self.month_label=Label(text='Month',bd=3).place(relx=0.35,rely=0.2,relwidth=0.1,relheight=0.05)
        self.month_var=StringVar()
        self.month_var.set(today_list[1]) 
        self.month_option=['01','02','03','04','05','06','07','08','09','10','11','12']
        self.cb2=ttk.Combobox(self.history_tk,state="readonly",values=self.month_option,textvariable=self.month_var).place(relx=0.47,rely=0.2,relwidth=0.1,relheight=0.05)
        self.year_label=Label(text='Year',bd=3).place(relx=0.59,rely=0.2,relwidth=0.1,relheight=0.05)
        self.year_var=StringVar()
        self.year_var.set(today_list[0])
        self.year_option=['1990''1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                          '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2044','2045','2046','2047','2048','2049','2050']
        self.cb3=ttk.Combobox(self.history_tk,state="readonly",values=self.year_option,textvariable=self.year_var).place(relx=0.71,rely=0.2,relwidth=0.1,relheight=0.05)
        self.result_text=Text(self.history_tk,fg='white',bg='black')
        self.result_text.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.5) 
        self.go=Button(self.history_tk,text='Go',bd=3,font='Times 10 bold',command=self.his_go).place(relx=0.6,rely=0.9,relwidth=0.1,relheight=0.05)
        self.back=Button(self.history_tk,text='<=Back',bd=3,font='Times 10 bold',command=self.his_back)
        self.back.place(relx=0.35,rely=0.9,relwidth=0.1,relheight=0.05)
        self.history_tk.mainloop()
    def his_back(self):
        self.history_tk.destroy()        
        Menu_page()
    def his_go(self):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.config(state=DISABLED)
        all_dates=Login_page_function.history_get_date()
        dates_match=[]
        for i in all_dates:
            dates_match.append(i[0])
        str_dates=str(self.year_var.get())+'-'+str(self.month_var.get())+'-'+str(self.date_var.get())
        if str_dates in dates_match:
            self.result_text.config(state=NORMAL)
            self.result_text.delete(1.0,END)
            self.result_text.see(END)
            self.result_text.insert(END,"\t Date \t|\t ID \t|\t   USN   \t|\t Action \t\n")
            self.result_text.insert(END,"-"*67+'\n')
            all_his=Login_page_function.history_get_all(str_dates)
            for tr in all_his:
                self.result_text.insert(END,'{}\t\t|\t{}\t|\t{}\t|\t{}\t\n'.format(tr[0],tr[1],tr[2],tr[3]))
            self.result_text.config(state=DISABLED)
        else:
            messagebox.showinfo('message','Result is not found')
            
class profile_page:
    def __init__(self):
        self.profile_tk=Tk()
        self.profile_tk.config(bg='#EEDFF2')
        self.profile_tk.title('ISE Library Managment System')
        self.profile_tk.iconbitmap('lib-icon.ico')
        self.profile_tk.geometry('600x500+500+150')
        self.profile_tk.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.profile_tk,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.label2=Label(self.profile_tk,text='USN    :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label2.place(relx=0.2,rely=0.1,relwidth=0.1,relheight=0.07)
        self.profile_usn_var=StringVar()
        self.entry2=Entry(self.profile_tk,bd=5,textvariable=self.profile_usn_var)
        self.entry2.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.07)
        self.search_b = Button(self.profile_tk,text="Search", fg='black',font='Times 9 bold',command=self.profile_search)
        self.search_b.place(relx=0.7,rely=0.1, relwidth=0.15,relheight=0.07)
        self.submit = Button(self.profile_tk,text="Delete", fg='black',bd=3,font='Times 9 bold',command=self.profile_delete_command)
        self.submit.place(relx=0.1,rely=0.8, relwidth=0.15,relheight=0.07)
        self.cancel = Button(self.profile_tk,text="Cancel", fg='black',bd=3,font='Times 9 bold',command=self.profile_cancel)
        self.cancel.place(relx=0.75,rely=0.8, relwidth=0.15,relheight=0.07)
        self.result_text=Text(self.profile_tk,fg='white',bg='black')
        self.result_text.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.5) 
        self.profile_tk.mainloop()
    def profile_cancel(self):
        self.profile_tk.destroy()
        Menu_page()
    def profile_search(self):
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.config(state=DISABLED)
        usn_Regex=re.compile('\dDS\d\dIS\d\d\d')
        if usn_Regex.search(self.profile_usn_var.get())!=None:
            std_details=Login_page_function.get_details_by_usn(self.profile_usn_var.get())
            if std_details!=[]:
                self.result_text.config(state=NORMAL)
                self.result_text.delete(1.0,END)
                self.result_text.see(END)   
                self.result_text.insert(END,'Name :- {}\n'.format(std_details[0][0]))
                self.result_text.insert(END,'USN :- {}\n'.format(std_details[0][1]))
                self.result_text.insert(END,'E-mail :- {}\n'.format(std_details[0][2]))
                self.result_text.insert(END,'DOB :- {}\n'.format(std_details[0][3]))
                self.result_text.insert(END,'sem :- {}\n'.format(std_details[0][4]))
                self.result_text.insert(END,'sec :- {}\n'.format(std_details[0][5]))
                self.result_text.insert(END,'b1 :- {}\n'.format(std_details[0][6]))
                self.result_text.insert(END,'b2 :- {}\n'.format(std_details[0][7]))
                self.result_text.insert(END,'b3 :- {}\n'.format(std_details[0][8]))
                self.result_text.insert(END,'Fine :- {}\n'.format(std_details[0][9]))
                self.result_text.config(state=DISABLED)
                 
            else:
                messagebox.showinfo('Error','USN not registered')
        else:
            messagebox.showerror('Error','Invalid usn')
    def profile_delete_command(self):
        b_list=Login_page_function.get_b_by_usn(self.profile_usn_var.get())
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0,END)
        self.result_text.config(state=DISABLED)
        usn_Regex=re.compile('\dDS\d\dIS\d\d\d')
        if usn_Regex.search(self.profile_usn_var.get())!=None:
            std_details=Login_page_function.get_details_by_usn(self.profile_usn_var.get())
            if std_details!=[]:
                self.result_text.config(state=NORMAL)
                self.result_text.delete(1.0,END)
                self.result_text.see(END)   
                self.result_text.insert(END,'Name :- {}\n'.format(std_details[0][0]))
                self.result_text.insert(END,'USN :- {}\n'.format(std_details[0][1]))
                self.result_text.insert(END,'E-mail :- {}\n'.format(std_details[0][2]))
                self.result_text.insert(END,'DOB :- {}\n'.format(std_details[0][3]))
                self.result_text.insert(END,'sem :- {}\n'.format(std_details[0][4]))
                self.result_text.insert(END,'sec :- {}\n'.format(std_details[0][5]))
                self.result_text.insert(END,'b1 :- {}\n'.format(std_details[0][6]))
                self.result_text.insert(END,'b2 :- {}\n'.format(std_details[0][7]))
                self.result_text.insert(END,'b3 :- {}\n'.format(std_details[0][8]))
                self.result_text.insert(END,'Fine :- {}\n'.format(std_details[0][9]))
                self.result_text.config(state=DISABLED)
                b_list=Login_page_function.get_b_by_usn(self.profile_usn_var.get())
                if b_list[0]==(0,0,0):
                    Login_page_function.delete_std(self.profile_usn_var.get())
                    messagebox.showinfo('Message','Account with usn {}  is deleted '.format(self.profile_usn_var.get()))
                else:
                    messagebox.showerror('Error','Return your all books')
            else:
                messagebox.showinfo('Error','USN not registered')
        else:
            messagebox.showerror('Error','Invalid usn')

class fine_page:
    def __init__(self):
        self.fine_tk=Tk()
        self.fine_tk.config(bg='#EEDFF2')
        self.fine_tk.title('ISE Library Managment System')
        self.fine_tk.iconbitmap('lib-icon.ico')
        self.fine_tk.geometry('600x500+500+150')
        self.fine_tk.maxsize(800,700)
        self.bg_image=ImageTk.PhotoImage(Image.open('back_im.jpg'))
        self.canvas=Canvas(self.fine_tk,bg='#EEDFF2',width=600,height=500)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.create_image(0,0,image=self.bg_image,anchor=NW)
        self.entryFrame=Frame(self.fine_tk,bg='#8D9A99')
        self.entryFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.5)
        self.label1=Label(self.entryFrame,text='USN :',fg='white',bg='#1C797B',font='Times 10 bold')
        self.label1.place(relx=0.05,rely=0.1,relwidth=0.15,relheight=0.2)
        self.fine_usn_var=StringVar()
        self.entry1=Entry(self.entryFrame,bd=5,textvariable=self.fine_usn_var,font='Times 13 bold')
        self.entry1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.2)
        self.search = Button(self.entryFrame, text="Search", fg='black',bd=3,font='Times 9 bold',command=self.search_command)
        self.search.place(relx=0.75,rely=0.1, relwidth=0.2,relheight=0.2) 
        self.result_text=Text(self.entryFrame,font='Times 13 bold')
        self.result_text.place(relx=0.05,rely=0.4,relwidth=0.75,relheight=0.2) 
        self.label2=Label(self.entryFrame,text='Amount   :',fg='white',bg='#1C797B',font='Times 9 bold')
        self.label2.place(relx=0.05,rely=0.7,relwidth=0.15,relheight=0.2)
        self.fine_amount_var=StringVar()
        self.entry2=Entry(self.entryFrame,bd=5,textvariable=self.fine_amount_var,font='Times 13 bold')
        self.entry2.place(relx=0.2,rely=0.7,relwidth=0.6,relheight=0.2)
        self.submit = Button(self.fine_tk,text="Pay", fg='black',bd=3,font='Times 9 bold',command=self.pay_command)
        self.submit.place(relx=0.1,rely=0.8, relwidth=0.15,relheight=0.07)
        self.cancel = Button(self.fine_tk,text="Cancel", fg='black',bd=3,font='Times 9 bold',command=self.cancel_command)
        self.cancel.place(relx=0.75,rely=0.8, relwidth=0.15,relheight=0.07)  
        self.fine_tk.mainloop()
    def cancel_command(self):
        self.fine_tk.destroy()
        Menu_page()
    def search_command(self):
        usn_Regex=re.compile('\dDS\d\dIS\d\d\d')
        if usn_Regex.search(self.fine_usn_var.get())!=None:
            if Login_page_function.get_details_by_usn(self.fine_usn_var.get())!=[]:
                fine=Login_page_function.get_fine(self.fine_usn_var.get())
                self.result_text.config(state=NORMAL)
                self.result_text.delete(1.0,END)
                self.result_text.see(END)
                self.result_text.insert(END,'Total fine is {}'.format(fine))
                self.result_text.config(state=DISABLED)
            else:
                messagebox.showerror('Error','usn not registered')
        else:
            messagebox.showerror('Error','Invalid usn')
    def pay_command(self):
        usn_Regex=re.compile('\dDS\d\dIS\d\d\d')
        if usn_Regex.search(self.fine_usn_var.get())!=None:
            if Login_page_function.get_details_by_usn(self.fine_usn_var.get())!=[]:
                fine=Login_page_function.get_fine(self.fine_usn_var.get())
                if self.fine_amount_var.get().isdigit():
                    new_fine=fine-int(self.fine_amount_var.get())
                    Login_page_function.update_fine(self.fine_usn_var.get(),new_fine)
                    fine=Login_page_function.get_fine(self.fine_usn_var.get())
                    self.result_text.config(state=NORMAL)
                    self.result_text.delete(1.0,END)
                    self.result_text.see(END)
                    self.result_text.insert(END,'Total fine is {}'.format(fine))
                    self.result_text.config(state=DISABLED)
                else:
                    messagebox.showerror('Error','Invalid Amount') 
            else:
                messagebox.showerror('Error','usn not registered')
        else:
            messagebox.showerror('Error','Invalid usn')
        


root=Tk()
root.config(bg='#0067AD')
root.title('ISE Library Managment System')
root.iconbitmap('lib-icon.ico')
root.geometry('600x500+500+150')
root.maxsize(800,700)
start=home_page(root)
root.mainloop()