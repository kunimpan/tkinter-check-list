from tkinter import *

#root window
root=Tk()
root.title("CheckList Application")
root.iconbitmap("icon/check.ico")
root.geometry("400x400+500+100")
root.resizable(0,0)

#settings
font=("arial", 15)
color="purple"
root.config(bg=color)

def addItem():
    data = inputEntry.get()
    listbox.insert(END, data) # END is last order.(last index)
    inputEntry.delete(0, END)

def removeItem():
    listbox.delete(ANCHOR) # ANCHOR is item as selected by click.


#design frame
input_frame = Frame(root, bg=color)
output_frame = Frame(root, bg=color)
button_frame = Frame(root, bg=color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

#input widget
inputEntry=Entry(input_frame, width=25, font=font)
btnAdd = Button(input_frame, text="Add Item", font=font, command=addItem)
inputEntry.grid(row=0, column=0, padx=5, pady=5, ipady=6)
btnAdd.grid(row=0, column=1, padx=5, pady=5)

#output widget
listbox = Listbox(output_frame, width=35, height=12, font=font)
listbox.grid(row=0, column=0, padx=5, pady=5)

#button widget
btnRemove = Button(button_frame, text="Remove Item", font=font, command=removeItem)
btnClear = Button(button_frame, text="Clear Items", font=font)
btnQuit=Button(button_frame, text="Close", font=font, command=root.destroy)

btnRemove.grid(row=0, column=1, padx=2, pady=2, ipadx=10)
btnClear.grid(row=0, column=2, padx=2, pady=2, ipadx=10)
btnQuit.grid(row=0, column=3, padx=2, pady=2, ipadx=10)

root.mainloop()