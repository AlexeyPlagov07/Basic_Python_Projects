import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from datetime import date
gui = Tk(className='Library')
first_name = tk.StringVar()
last_name = tk.StringVar()
book_name1 = tk.StringVar()
Author1 = tk.StringVar()
ISBN1 = tk.IntVar()
# set window size
gui.geometry("400x300")
gui.configure(bg='lightblue')
list_var=tk.StringVar()

e1 = Entry(gui,textvariable=list_var).grid(row=0, column=0)
list_items = []
conn = sqlite3.connect("ua_library.db")
output_str = tk.StringVar()
cursor = conn.cursor()
#cursor.execute("CREATE TABLE checkout (ID INT, book TEXT, ISBN INT, author TEXT, check_inout TEXT, name TEXT, time INT)")
#cursor.execute("CREATE TABLE library (book TEXT, ISBN INT, author TEXT, availability TEXT)")
#cursor.execute("INSERT INTO library VALUES ('Catcher and the Rye', 35879656, 'Harry', 'yes')")
#conn.commit()
#cursor.execute("UPDATE library SET availability='no' WHERE ISBN=346234823;")
#conn.commit()

  

def spec_item():
  cursor.execute("SELECT * FROM library WHERE ISBN="+list_var.get())
  result = cursor.fetchall()
  Label(gui, text = "Book" + " | " + "ISBN" + " | " + "Author" + " | " + "Availability", bg='lightblue').grid(row=(1))
  i = list(result[0])
  output_str.set(i[0] + " | " + str(i[1]) + " | " + i[2] + " | " + i[3])
  Label(gui, textvariable=output_str, bg='lightblue').grid(row=2)

  checkout_button = Button(gui, text="Check IN/OUT", command=checkoutwindow).grid(row=4)

def checkout1(name):
  
  cursor.execute("SELECT * FROM library WHERE ISBN="+list_var.get())
  result = cursor.fetchall()
  print(name)
  i = list(result[0])
  if i[3] == "yes":
    check_inout = ("Checked Out")
    cursor.execute("UPDATE library SET availability='no' WHERE ISBN="+list_var.get())
  if i[3] == "no":
    check_inout = ("Checked In")
    cursor.execute("UPDATE library SET availability='yes' WHERE ISBN="+list_var.get())
  print(check_inout,"<")
  cursor.execute("SELECT Count(*) FROM checkout")
  length = (list(cursor.fetchall()[0]))[0]
  sql_query = "INSERT INTO checkout VALUES (?, ?, ?, ?, ?, ?, ?)"
  cursor.execute(sql_query, ((length + 1), i[0], i[1], i[2], str(check_inout), str(name), date.today()))
  
  conn.commit()
  

  
def checkoutwindow():
  cursor.execute("SELECT * FROM library WHERE ISBN="+list_var.get())
  result = cursor.fetchall()
  i = list(result[0])
  checkout = tk.Toplevel(gui)
  checkout.title("Checkout")
  checkout.geometry("300x200")
  if i[3] == "yes":
    Label(checkout, text="First Name").grid(row=0, column=0)
    f_n = Entry(checkout, textvariable=first_name).grid(row=0,column=1)
    Label(checkout, text="Last Name").grid(row=1, column=0)
    l_n = Entry(checkout, textvariable=last_name).grid(row=1,column=1)
    Button(checkout, text="Check out", command=lambda: [checkout1(get_name()), checkout.destroy()]).grid(row=2,column=0)
  elif i[3] == "no":
    cursor.execute("SELECT name FROM checkout WHERE check_inout='Checked Out' ORDER BY ID DESC LIMIT 1 ") 
    result2 = list(cursor.fetchall()[0])[0]
    Button(checkout, text="Check in", command=lambda: [checkout1(result2), checkout.destroy()]).grid(row=2,column=0)
  def get_name():
    name1 = (first_name.get() + " " + last_name.get())
    return name1
  
    
  
  
def openNewWindow():
  newWindow = Toplevel(gui)
  newWindow.title("New Window")
  newWindow.geometry("460x200")
  listbox = Listbox(newWindow, width=50)
  listbox.grid(row=1)
  

  scrollbar = Scrollbar(newWindow)
  

  scrollbar.grid(row=1, column=1)
  
  cursor.execute("SELECT * FROM library")
  result = (cursor.fetchall())
  Label(newWindow, text = "Book" + " | " + "ISBN" + " | " + "Author" + " | " + "Availability", bg='white').grid(row=0, column=0)
  
  
  
  for i in range(len(result)):
    j = list(result[i])
    x = (j[0] + " | " + str(j[1]) + " | " + j[2] + " | " + j[3])
    listbox.insert(END, x)
      

  listbox.config(yscrollcommand = scrollbar.set)
  
  edit = Button(newWindow, text="edit", command=edit_window).grid(row=0, column=1)

  scrollbar.config(command = listbox.yview)
def edit_window():
  
  editw = Toplevel(gui)
  editw.title("Edit List")
  editw.geometry("300x200")
  Label(editw, text="Book Name").grid(row=0,column=0)
  book_name = Entry(editw, textvariable=book_name1).grid(row=0,column=1)
  Label(editw, text="Author Name").grid(row=1,column=0)
  Author = Entry(editw, textvariable=Author1).grid(row=1,column=1)
  Label(editw, text="ISBN").grid(row=2,column=0)
  ISBN = Entry(editw, textvariable=ISBN1).grid(row=2,column=1)
  Button(editw, text="Add Book", command=lambda: [add_book(book_name1.get(), Author1.get(), ISBN1.get()), editw.destroy()]).grid(row=3)

def add_book(book_name1, Author1, ISBN1):
  sql_values = ("INSERT INTO library VALUES (?, ?, ?, ?)")
  cursor.execute(sql_values, (book_name1, ISBN1, Author1, "yes"))
  conn.commit()
def log_window():
  log_window = tk.Toplevel(gui)
  log_window.title("Log")
  log_window.geometry("300x200")
  log_listbox = Listbox(log_window, width=100)
  log_listbox.grid(row=1)
  scrollbar_log = Scrollbar(log_window)
  scrollbar_log.grid(row=1,column=1)
  cursor.execute("SELECT * FROM checkout")
  result1 = cursor.fetchall()
  Label(log_window,text= "ID|Book|ISBN|Author|Checked In/Out|Name|Date").grid(row=0)
  for i in range(len(result1)):
    j = list(result1[i])
    x = (str(j[0]) + " | " + j[1] + " | " + str(j[2]) + " | " + j[3] + " | " + j[4] + " | " + j[5] + " | " + j[6])
    log_listbox.insert(END, x)
  log_listbox.config(yscrollcommand = scrollbar_log.set)
  scrollbar_log.config(command = log_listbox.yview)
button = tk.Button(gui, text="Enter ISBN", command = spec_item).grid(row=0, column=1)
button1 = tk.Button(gui, text = "Show Full List", command = openNewWindow).grid(row=1, column=1)
button2 = tk.Button(gui, text = "View Log", command = log_window).grid(row=2,column=1)
mainloop()
