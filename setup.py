from tkinter import *
import random

def zobraz_vstup():
    global e1
    global e2
    global e3

    row_count = int(e1.get())
    column_count = int(e2.get())
    mine_count = int(e3.get())

    mines_coordinates = []
    global already_generated
    global result
    result  = 'from tkinter import *'
    result  += 'import os, sys'
    result  += 'root = Tk()'
    result  += 'mine_image = PhotoImage(file=r"" + os.getcwd() + "\mine.png")'
    result  += 'one_image = PhotoImage(file=r"" + os.getcwd() + "\_one.png")'
    result  += 'two_image = PhotoImage(file=r"" + os.getcwd() + "\_two.png")'
    result  += 'three_image = PhotoImage(file=r"" + os.getcwd() + "\_three.png")'
    result  += 'gridFrame = Frame(root).grid(row=0,column=0)'
    
    #dvourozmerny array vytvorenych min
    index = 0
    while(index <= mine_count):
        row_generated = random.randint(0,row_count)
        column_generated = random.randint(0,column_count)
        mines_coordinates.append([])
        print(index)
        print(mines_coordinates)
        
        for r in mines_coordinates:
            if(len(r) >= 2):
                if(r[0] == row_generated and r[1] == column_generated):
                    already_generated = True
                else:
                    mines_coordinates[index].append(row_generated)
                    mines_coordinates[index].append(column_generated)
                    index  += 1
                    print("success, current mines_coordinates: " + mines_coordinates + " -- current index: " + index)
            else:
                mines_coordinates[index].append(row_generated)
                mines_coordinates[index].append(column_generated)
                index  += 1
                print("success, current mines_coordinates: " + mines_coordinates + " -- current index: " + index)
    for x in mines_coordinates:
        
        result += 'Button(gridFrame, width = "40",height = "40",command="mine").grid(row=' + str(x[0]) + ',column=' + str(x[1]) + ')'

    print(result)
    #dva generatory cisel, jeden pro column, druhy pro  row
    #check jestli uz takovy souradnice nejsou zabrany 
    #Button(gridFrame, width = "40",height = "40",command="mine").grid(row=row_generated,column=column_generated)
    
    
    #main = open("main.py","x")
    
    #root.destroy()

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
