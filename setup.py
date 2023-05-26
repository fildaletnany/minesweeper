from tkinter import *
import random

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
    result  = 'from tkinter import *\n'
    result  += 'import os, sys\n'
    result  += 'root = Tk()\n'
    result  += 'mine_image = PhotoImage(file=r"" + os.getcwd() + "\mine.png")\n'
    result  += 'one_image = PhotoImage(file=r"" + os.getcwd() + "\_one.png")\n'
    result  += 'two_image = PhotoImage(file=r"" + os.getcwd() + "\_two.png")\n'
    result  += 'three_image = PhotoImage(file=r"" + os.getcwd() + "\_three.png")\n'
    result  += 'gridFrame = Frame(root).grid(row=0,column=0)\n'
    
    #dvourozmerny array vytvorenych min
    index = 0
    while(index <= mine_count):
        row_generated = random.randint(0,row_count)
        column_generated = random.randint(0,column_count)
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

        
        
        """for r in mines_coordinates:
            if(len(r) != 0):
                if(r[0] == row_generated and r[1] == column_generated):
                    print("same detected")
                else:                 
                    mines_coordinates[index].append(row_generated)
                    mines_coordinates[index].append(column_generated)
                    index  += 1
                    print("mine added inner")
            else:
                mines_coordinates[index].append(row_generated)
                mines_coordinates[index].append(column_generated)
                index  += 1
                print("mine added outer")
        print("done")"""

        
        """for r in mines_coordinates:
            if(len(r) >= 2):
                if(r[0] == row_generated and r[1] == column_generated):
                    already_generated = True
                else:
                    mines_coordinates[index].append(row_generated)
                    mines_coordinates[index].append(column_generated)
                    index  += 1
                    print("BBBBBBBBBBBBBBBBBBBBBB" + str(index))
                    #print("success, current mines_coordinates: " + mines_coordinates + " -- current index: " + index)
            else:
                mines_coordinates[index].append(row_generated)
                mines_coordinates[index].append(column_generated)
                index  += 1
                print("AAAAAAAAAAAAAAAAAA" + str(index))
                #print("success, current mines_coordinates: " + mines_coordinates + " -- current index: " + index)
    """

    for x in mines_coordinates:
        result += 'Button(gridFrame, width = "40",height = "40",command="mine").grid(row=' + str(x[0]) + ',column=' + str(x[1]) + ')\n'
    
    index_row = 0
    index_column = 0
    coords_taken_bool = False
    while(index_row <= row_count):
        while (index_column <= column_count):
            for a in mines_coordinates:
                if(index_row == a[0] and index_column == a[1]):
                    coords_taken_bool = True
            if(coords_taken_bool == False):
                result += 'Button(gridFrame, width = "40",height = "40",command="mine").grid(row=' + str(index_row) + ',column=' + str(index_column) + ')\n'
            else:
                print("coordinates already taken, skipping")

            index_column += 1
            coords_taken_bool = False
        index_row += 1
        #tam kde neni mina vygeneruj normalni policko

    result += "root.mainloop()"
    print(result)
    
    main = open("main.py","w")
    main.write(result)
    
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
