import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
#sets the window#
gui = Tk(className='My List')
# set window size
gui.geometry("400x300")

#set window color

gui.configure(bg='lightblue')

#sets variable#
list_var=tk.StringVar()

Label(gui, text='What would you like to add?', bg='lightblue').grid(row=0)
e1 = Entry(gui,textvariable=list_var).grid(row=0, column=1)
list_items = []








##################add items to list################################
def add_item():
  list_items.append(list_var.get())
  var1 = Variable(value=list_items)
  
  listbox = Listbox(gui, height = 10,width = 15,bg = "grey",activestyle = 'dotbox',font = "Helvetica",fg = "yellow",listvariable=var1, selectmode=tk.EXTENDED)
  listbox.grid(row=3, column=0)

  

#############################delete items from list##################
def delete_item():
  list_items.remove(list_var.get())
  var2 = Variable(value=list_items)
  listbox = Listbox(gui, height = 10,width = 15,bg = "grey",activestyle = 'dotbox',font = "Helvetica",fg = "yellow",listvariable=var2)
  listbox.grid(row=3, column=0)
####################Clear items from list##########################
def clear_list():
  list_items.clear()
  var3 = Variable(value=list_items)
  listbox = Listbox(gui, height = 10,width = 15,bg = "grey",activestyle = 'dotbox',font = "Helvetica",fg = "yellow",listvariable=var3)
  listbox.grid(row=3, column=0)
###################################################################



######################Buttons#######################################
button = tk.Button(gui,text='Add Item', command=add_item).grid(row=1)
button1 = tk.Button(gui, text='Delete Item', command=delete_item).grid(row=1, column=1)
button2 = tk.Button(gui, text='Clear List', command=clear_list).grid(row=2, column=0)
###################################################################










mainloop()

######################################################################
