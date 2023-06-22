from tkinter import *
import random
import subprocess

mines_coordinates = NONE
row_count = 0
column_count = 0
mine_count = 0
result = NONE

mines_coordinates = NONE
row_count = 0
column_count = 0
mine_count = 0
result = NONE

def check_for_duplicates ():
    for x in mines_coordinates:
        for y in mines_coordinates:
            if(x[0] == y[0] and x[1] == y[1]):
                x[0] = random.randint(0,row_count)
                x[1] = random.randint(0,column_count) 


def zobraz_vstup():
    global e1
    global e2
    global e3

    row_count = int(e1.get())
    column_count = int(e2.get())
    mine_count = int(e3.get())

    mines_coordinates = []
    result = 'from tkinter import *\n'
    result += 'import os, sys\n'
    result += 'root = Tk()\n'
    result += 'mine_image = PhotoImage(file=r"" + os.getcwd() + "\mine.png")\n'
    result += 'blank_image = PhotoImage(file=r"" + os.getcwd() + "\_blank.png")\n'
    result += 'default_image = PhotoImage(file=r"" + os.getcwd() + "\_empty.png")\n'
    result += 'one_image = PhotoImage(file=r"" + os.getcwd() + "\_one.png")\n'
    result += 'two_image = PhotoImage(file=r"" + os.getcwd() + "\_two.png")\n'
    result += 'three_image = PhotoImage(file=r"" + os.getcwd() + "\_three.png")\n'
    result += 'four_image = PhotoImage(file=r"" + os.getcwd() + "\_four.png")\n'
    result += 'five_image = PhotoImage(file=r"" + os.getcwd() + "\_five.png")\n'
    result += 'six_image = PhotoImage(file=r"" + os.getcwd() + "\_six.png")\n'
    result += 'seven_image = PhotoImage(file=r"" + os.getcwd() + "\_seven.png")\n'
    result += 'eight_image = PhotoImage(file=r"" + os.getcwd() + "\_eight.png")\n'
    result += 'gridFrame = Frame(root).grid(row=0,column=0)\n'
    result += 'def mine(button_reference):\n'
    result += ' globals()[button_reference].config(image=mine_image)\n'
    result += ' print("bum")\n'
    result += 'def safe(value, button_reference):\n'
    result += ' if(value == "0"):\n'
    result += '     print("0")\n'
    result += '     globals()[button_reference].config(image=blank_image)\n'
    result += ' elif(value == "1"):\n'
    result += '     print("1")\n'
    result += '     globals()[button_reference].config(image=one_image)\n'
    result += ' elif((value == "2")):\n'
    result += '     print("2")\n'
    result += '     globals()[button_reference].config(image=two_image)\n'
    result += ' elif((value == "3")):\n'
    result += '     print("3")\n'
    result += '     globals()[button_reference].config(image=three_image)\n'
    result += ' elif((value == "4")):\n'
    result += '     print("4")\n'
    result += '     globals()[button_reference].config(image=four_image)\n'
    result += ' elif((value == "5")):\n'
    result += '     print("5")\n'
    result += '     globals()[button_reference].config(image=five_image)\n'
    result += ' elif((value == "6")):\n'
    result += '     print("6")\n'
    result += '     globals()[button_reference].config(image=six_image)\n'
    result += ' elif((value == "7")):\n'
    result += '     print("7")\n'
    result += '     globals()[button_reference].config(image=seven_image)\n'
    result += ' elif((value == "8")):\n'
    result += '     print("8")\n'
    result += '     globals()[button_reference].config(image=eight_image)\n'

    #dvourozmerny array vytvorenych min
    index = 0
    while(index < mine_count):
        row_generated = random.randint(0,row_count-1)
        column_generated = random.randint(0,column_count-1)
        #nova prazdna mina
        mines_coordinates.append([])
        print(row_generated)
        print(column_generated)
        print(index)
        #vsechny miny 
        print(mines_coordinates)
        
        mines_coordinates[index].append(row_generated)
        mines_coordinates[index].append(column_generated)
        mines_coordinates[index].append(index)
        index  += 1

    button_count = 0
    for x in mines_coordinates:
        result += 'button_mine_' + str(button_count) + ' = Button(gridFrame, width = "40",height = "40", image=default_image)\n'
        result += 'button_mine_' + str(button_count) + '.grid(row=' + str(x[0]) + ',column=' + str(x[1]) + ')\n'
        result += 'button_mine_' + str(button_count) + '.config(command = lambda: mine("button_mine_' + str(button_count) + '"))\n'
        button_count += 1

    index_row = 0
    index_column = 0
    global coord_taken
    coord_taken = False
    button_count = 0

    while(index_row < row_count):
        while(index_column < column_count):
            for a in mines_coordinates:
                if(a[0] == index_row and a[1] == index_column):
                    coord_taken = True
            if(coord_taken == False):
                result += 'button_' + str(button_count) + ' = Button(gridFrame, width = "40",height = "40", image=default_image)\n'
                result += 'button_' + str(button_count) + '.grid(row=' + str(index_row) + ',column=' + str(index_column) + ')\n'
            else:
                print("taken, skipping")

            index_column += 1
            button_count += 1
            coord_taken = False
        index_column = 0
        index_row += 1
    
    index_row = 0
    index_column = 0
    coord_taken = False
    button_count = 0
    mines_near = 0

    while(index_row < row_count):
        while(index_column < column_count):
            for a in mines_coordinates:
                if(a[0] == index_row and a[1] == index_column):
                    coord_taken = True
                if(a[0] == index_row - 1 and a[1] == index_column - 1):
                    mines_near += 1
                if(a[0] == index_row - 1 and a[1] == index_column):
                    mines_near += 1
                if(a[0] == index_row - 1 and a[1] == index_column + 1):
                    mines_near += 1
                if(a[0] == index_row and a[1] == index_column - 1):
                    mines_near += 1
                if(a[0] == index_row and a[1] == index_column + 1):
                    mines_near += 1
                if(a[0] == index_row + 1 and a[1] == index_column - 1):
                    mines_near += 1
                if(a[0] == index_row + 1 and a[1] == index_column):
                    mines_near += 1
                if(a[0] == index_row + 1 and a[1] == index_column + 1):
                    mines_near += 1
            if(coord_taken == False):
                result += 'button_' + str(button_count) + '.config(command = lambda: safe("' + str(mines_near) + '", "button_' + str(button_count) + '"))\n'
            else:
                print("taken, skipping")

            index_column += 1
            button_count += 1
            mines_near = 0
            coord_taken = False
        index_column = 0
        index_row += 1

    result += "root.mainloop()"
    print(result)
    
    main = open("main.py","w")
    main.write(result)
    subprocess.run(["python", "main.py"])
    
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
