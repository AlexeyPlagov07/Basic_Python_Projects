import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
gui = Tk(className='Library')
# set window size
gui.geometry("400x300")
gui.configure(bg='lightblue')
list_var=tk.StringVar()
e1 = Entry(gui,textvariable=list_var).grid(row=0, column=0)
list_items = []
conn = sqlite3.connect("ua_library.db")
output_str = tk.StringVar()
cursor = conn.cursor()

#cursor.execute("CREATE TABLE library (book TEXT, ISBN INT, author TEXT, availability TEXT)")
cursor.execute("INSERT INTO library VALUES ('Catcher and the Rye', 35879656, 'Harry', 'no')")
conn.commit()
#cursor.execute("UPDATE library SET availability='no' WHERE ISBN=346234823;")
#conn.commit()
#def full_list():
  

def spec_item():
  cursor.execute("SELECT * FROM library WHERE ISBN="+list_var.get())
  result = cursor.fetchall()
  Label(gui, text = "Book" + " | " + "ISBN" + " | " + "Author" + " | " + "Availability", bg='lightblue').grid(row=(1))
  i = list(result[0])
  Label(gui, text=i[0] + " | " + str(i[1]) + " | " + i[2] + " | " + i[3], bg='lightblue').grid(row=(2))

def openNewWindow():
  newWindow = Toplevel(gui)
  newWindow.title("New Window")
  newWindow.geometry("600x200")
  listbox = Listbox(newWindow, width=100)
  listbox.grid(row=1)
  

  scrollbar = Scrollbar(newWindow)
  

  scrollbar.grid(row=1, column=1)
  
  cursor.execute("SELECT * FROM library")
  result = (cursor.fetchall())
  Label(newWindow, text = "Book" + " | " + "ISBN" + " | " + "Author" + " | " + "Availability", bg='white').grid(row=0)
  
  
  
  for i in range(len(result)):
    j = list(result[i])
    x = (j[0] + " | " + str(j[1]) + " | " + j[2] + " | " + j[3])
    listbox.insert(END, x)
      

  listbox.config(yscrollcommand = scrollbar.set)
  

  scrollbar.config(command = listbox.yview)  

button = tk.Button(gui, text="Enter ISBN", command = spec_item).grid(row=0, column=1)
button1 = tk.Button(gui, text = "Show Full List", command = openNewWindow).grid(row=1, column=1)
mainloop()
