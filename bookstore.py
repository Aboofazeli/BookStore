from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in backend.search(input1.get(),input2.get(),input3.get(),input4.get()):
        list1.insert(END,row)
def add_command():
    list1.delete(0,END)
    backend.insert(input1.get(),input2.get(),input3.get(),input4.get())
    list1.insert(END,(input1.get(),input2.get(),input3.get(),input4.get()))

def getrows(event):
    global selectedrow
    try:
        index=list1.curselection()[0]
        selectedrow=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selectedrow[1])
        e2.delete(0,END)
        e2.insert(END,selectedrow[2])
        e3.delete(0,END)
        e3.insert(END,selectedrow[3])
        e4.delete(0,END)
        e4.insert(END,selectedrow[4])
    except IndexError:
        pass
def delete_command():
    backend.delete(selectedrow[0])

def update_command():
    backend.update(selectedrow[0], input1.get(), input2.get(), input3.get(), input4.get())

window=Tk()
window.wm_title("Bookstore")
l1=Label(window, text="Title")
l1.grid(row=0, column=0)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)

input1=StringVar()
e1=Entry(window, textvariable=input1)
e1.grid(row=0, column=1)

input2=StringVar()
e2=Entry(window, textvariable=input2)
e2.grid(row=0, column=3)

input3=StringVar()
e3=Entry(window, textvariable=input3)
e3.grid(row=1, column=1)

input4=StringVar()
e4=Entry(window, textvariable=input4)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', getrows)

b1=Button(window, text="view all", width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="search entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="add entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window, text="update", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="delete", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="close", width=12, command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()
