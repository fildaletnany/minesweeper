from tkinter import *

def zobraz_vstup():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

root = Tk()
frame = Frame(root)
frame.pack()

Label(frame, text="počet řádků").pack(anchor="center")
e1 = Entry(frame)
e1.pack()

Label(frame, text="počet sloupců").pack(anchor="center")
e2 = Entry(frame)
e2.pack()

Label(frame, text="počet min").pack(anchor="center")
e3 = Entry(frame)
e3.pack()

Button(root, text="vytvořit", command=zobraz_vstup).pack(anchor="center")

mainloop()
