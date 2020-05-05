 # -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:30:27 2020

@author: shashank
"""

import sqlite3
from datetime import date,timedelta


def insert_new_book(title,bid,author,subject,isbn,status):
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("INSERT INTO all_books VALUES (?,?,?,?,?,?)",(title,bid,author,subject,isbn,status,))
    conn.commit()
    conn.close()

def get_book_from_id(bid):
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT * FROM all_books WHERE bid=?",(bid,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_book_from_title(title):
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT * FROM all_books WHERE title=?",(title,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_book_from_author(author):
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT * FROM all_books WHERE author=?",(author,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_book_from_subject(sub):
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT * FROM all_books WHERE subject=?",(sub,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_all_title():
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT DISTINCT title FROM all_books")
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_all_author():
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT DISTINCT author FROM all_books")
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_all_subject():
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT DISTINCT subject FROM all_books")
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)




def view_book():
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT *  FROM all_books")
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_status(bid):
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS all_books(title TEXT,bid INTEGER,author TEXT,subject TEXT,isbn TEXT,status TEXT)")
    cur.execute("SELECT DISTINCT status FROM all_books WHERE bid=?",(bid,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b[0][0])

def update_status(status,bid):
    conn=sqlite3.connect('book.db')
    cur=conn.cursor()
    cur.execute("UPDATE all_books SET status=? WHERE bid=?",(status,bid,))
    conn.commit()
    conn.close()
    




    
def student_details(name,usn,email,dob,sem,sec,b1,b2,b3,fine):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS std (name TEXT,usn TEXT,email TEXT,dob TEXT,sem INTEGER,sec TEXT,b1 INTEGER,b2 INTEGER,b3 INTEGER,fine INTEGER)")
    cur.execute("INSERT INTO std VALUES (?,?,?,?,?,?,?,?,?,?)",(name,usn,email,dob,sem,sec,b1,b2,b3,fine,))
    conn.commit()
    conn.close()

def get_details_by_usn(usn):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS std (name TEXT,usn TEXT,email TEXT,dob TEXT,sem INTEGER,sec TEXT,b1 INTEGER,b2 INTEGER,b3 INTEGER,fine INTEGER)")
    cur.execute("SELECT * FROM std WHERE usn=?",(usn,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_details_by_email(email):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS std (name TEXT,usn TEXT,email TEXT,dob TEXT,sem INTEGER,sec TEXT,b1 INTEGER,b2 INTEGER,b3 INTEGER,fine INTEGER)")
    cur.execute("SELECT * FROM std WHERE email=?",(email,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def get_b_by_usn(usn):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS std (name TEXT,usn TEXT,email TEXT,dob TEXT,sem INTEGER,sec TEXT0000,b1 INTEGER,b2 INTEGER,b3 INTEGER,fine INTEGER)")
    cur.execute("SELECT DISTINCT b1,b2,b3 FROM std WHERE usn=?",(usn,))
    b=cur.fetchall()
    conn.commit()
    conn.close()
    return(b)

def update_b1(usn,b1):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("UPDATE std SET b1=? WHERE usn=?",(b1,usn,))
    conn.commit()
    conn.close()

def update_b2(usn,b2):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("UPDATE std SET b2=? WHERE usn=?",(b2,usn,))
    conn.commit()
    conn.close()

def update_b3(usn,b3):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("UPDATE std SET b3=? WHERE usn=?",(b3,usn,))
    conn.commit()
    conn.close()
def update_fine(usn,f):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("UPDATE std SET fine=? WHERE usn=?",(f,usn,))
    conn.commit()
    conn.close()
def get_fine(usn):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT fine FROM std WHERE usn=?",(usn,))
    row=cur.fetchall()
    conn.commit()
    conn.close()
    return(row[0][0])

def delete_std(usn):
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM std WHERE usn=?",(usn,))
    conn.commit()
    conn.close()
    
    
def issue_details(dt1,dt2,bid,usn):
    conn=sqlite3.connect('issue.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS issue_details (issue_date TEXT,due_date TEXT,id INTEGER,usn TEXT)")
    cur.execute("INSERT INTO issue_details VALUES (?,?,?,?)",(dt1,dt2,bid,usn,))
    conn.commit()
    conn.close()
    
def get_issue_details(bid):
    conn=sqlite3.connect('issue.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM issue_details WHERE id=?",(bid,))
    row=cur.fetchall()
    conn.commit()
    conn.close()  
    return(row)
def update_date(dt1,dt2,bid):
    conn=sqlite3.connect('issue.db')
    cur=conn.cursor()
    cur.execute("UPDATE issue_details SET issue_date=?,due_date=? WHERE id=?",(dt1,dt2,bid,))
    conn.commit()
    conn.close()
    
def delete_issue(bid):
    conn=sqlite3.connect('issue.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM issue_details WHERE id=?",(bid,))
    conn.commit()
    conn.close()    
    
    
def history_insert(bid,usn,status):
    conn=sqlite3.connect('history.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS history (issue_date TEXT,id TEXT,usn TEXT,status TEXT)")
    cur.execute("INSERT INTO history VALUES (?,?,?,?)",(str(date.today()),bid,usn,status,))
    conn.commit()
    conn.close()
    
def history_get_all(dt):
    conn=sqlite3.connect('history.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM history where issue_date=?",(dt,))
    row=cur.fetchall()
    conn.close()
    return(row)

def history_get_date():
    conn=sqlite3.connect('history.db')
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT issue_date FROM history")
    row=cur.fetchall()
    conn.close()
    return(row)