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

#design frame
input_frame = Frame(root, bg=color)
output_frame = Frame(root, bg=color)
button_frame = Frame(root, bg=color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

root.mainloop()