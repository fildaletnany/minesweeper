from tkinter import *
import os, sys
import subprocess
global root
root = Tk()
global is_dead
is_dead = False
mine_image = PhotoImage(file=r"" + os.getcwd() + "\mine.png")
blank_image = PhotoImage(file=r"" + os.getcwd() + "\_blank.png")
default_image = PhotoImage(file=r"" + os.getcwd() + "\_empty.png")
one_image = PhotoImage(file=r"" + os.getcwd() + "\_one.png")
two_image = PhotoImage(file=r"" + os.getcwd() + "\_two.png")
three_image = PhotoImage(file=r"" + os.getcwd() + "\_three.png")
four_image = PhotoImage(file=r"" + os.getcwd() + "\_four.png")
five_image = PhotoImage(file=r"" + os.getcwd() + "\_five.png")
six_image = PhotoImage(file=r"" + os.getcwd() + "\_six.png")
seven_image = PhotoImage(file=r"" + os.getcwd() + "\_seven.png")
eight_image = PhotoImage(file=r"" + os.getcwd() + "\_eight.png")
gridFrame = Frame(root).grid(row=0,column=0)
def mine(button_reference):
 globals()[button_reference].config(image=mine_image)
 print("bum")
 globals()[is_dead] = True
 subprocess.run(["python", "gameOver.py"])
def safe(value, button_reference):
 print(is_dead)
 if(is_dead == False):
  if(value == "0"):
      print("0")
      globals()[button_reference].config(image=blank_image)
  elif(value == "1"):
      print("1")
      globals()[button_reference].config(image=one_image)
  elif((value == "2")):
      print("2")
      globals()[button_reference].config(image=two_image)
  elif((value == "3")):
      print("3")
      globals()[button_reference].config(image=three_image)
  elif((value == "4")):
      print("4")
      globals()[button_reference].config(image=four_image)
  elif((value == "5")):
      print("5")
      globals()[button_reference].config(image=five_image)
  elif((value == "6")):
      print("6")
      globals()[button_reference].config(image=six_image)
  elif((value == "7")):
      print("7")
      globals()[button_reference].config(image=seven_image)
  elif((value == "8")):
      print("8")
      globals()[button_reference].config(image=eight_image)
button_mine_0 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_0.grid(row=6,column=3)
button_mine_0.config(command = lambda: mine("button_mine_0"))
button_mine_1 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_1.grid(row=1,column=3)
button_mine_1.config(command = lambda: mine("button_mine_1"))
button_mine_2 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_2.grid(row=1,column=2)
button_mine_2.config(command = lambda: mine("button_mine_2"))
button_mine_3 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_3.grid(row=4,column=4)
button_mine_3.config(command = lambda: mine("button_mine_3"))
button_mine_4 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_4.grid(row=6,column=4)
button_mine_4.config(command = lambda: mine("button_mine_4"))
button_mine_5 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_5.grid(row=8,column=0)
button_mine_5.config(command = lambda: mine("button_mine_5"))
button_mine_6 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_6.grid(row=3,column=9)
button_mine_6.config(command = lambda: mine("button_mine_6"))
button_mine_7 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_7.grid(row=6,column=4)
button_mine_7.config(command = lambda: mine("button_mine_7"))
button_mine_8 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_8.grid(row=0,column=9)
button_mine_8.config(command = lambda: mine("button_mine_8"))
button_mine_9 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_9.grid(row=1,column=9)
button_mine_9.config(command = lambda: mine("button_mine_9"))
button_mine_10 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_10.grid(row=7,column=2)
button_mine_10.config(command = lambda: mine("button_mine_10"))
button_mine_11 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_11.grid(row=6,column=3)
button_mine_11.config(command = lambda: mine("button_mine_11"))
button_mine_12 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_12.grid(row=9,column=1)
button_mine_12.config(command = lambda: mine("button_mine_12"))
button_mine_13 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_13.grid(row=5,column=3)
button_mine_13.config(command = lambda: mine("button_mine_13"))
button_mine_14 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_14.grid(row=4,column=4)
button_mine_14.config(command = lambda: mine("button_mine_14"))
button_mine_15 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_15.grid(row=1,column=5)
button_mine_15.config(command = lambda: mine("button_mine_15"))
button_mine_16 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_16.grid(row=0,column=3)
button_mine_16.config(command = lambda: mine("button_mine_16"))
button_mine_17 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_17.grid(row=9,column=3)
button_mine_17.config(command = lambda: mine("button_mine_17"))
button_mine_18 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_18.grid(row=1,column=4)
button_mine_18.config(command = lambda: mine("button_mine_18"))
button_mine_19 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_mine_19.grid(row=3,column=3)
button_mine_19.config(command = lambda: mine("button_mine_19"))
button_0 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_0.grid(row=0,column=0)
button_1 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_1.grid(row=0,column=1)
button_2 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_2.grid(row=0,column=2)
button_4 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_4.grid(row=0,column=4)
button_5 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_5.grid(row=0,column=5)
button_6 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_6.grid(row=0,column=6)
button_7 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_7.grid(row=0,column=7)
button_8 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_8.grid(row=0,column=8)
button_10 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_10.grid(row=1,column=0)
button_11 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_11.grid(row=1,column=1)
button_16 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_16.grid(row=1,column=6)
button_17 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_17.grid(row=1,column=7)
button_18 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_18.grid(row=1,column=8)
button_20 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_20.grid(row=2,column=0)
button_21 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_21.grid(row=2,column=1)
button_22 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_22.grid(row=2,column=2)
button_23 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_23.grid(row=2,column=3)
button_24 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_24.grid(row=2,column=4)
button_25 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_25.grid(row=2,column=5)
button_26 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_26.grid(row=2,column=6)
button_27 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_27.grid(row=2,column=7)
button_28 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_28.grid(row=2,column=8)
button_29 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_29.grid(row=2,column=9)
button_30 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_30.grid(row=3,column=0)
button_31 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_31.grid(row=3,column=1)
button_32 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_32.grid(row=3,column=2)
button_34 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_34.grid(row=3,column=4)
button_35 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_35.grid(row=3,column=5)
button_36 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_36.grid(row=3,column=6)
button_37 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_37.grid(row=3,column=7)
button_38 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_38.grid(row=3,column=8)
button_40 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_40.grid(row=4,column=0)
button_41 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_41.grid(row=4,column=1)
button_42 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_42.grid(row=4,column=2)
button_43 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_43.grid(row=4,column=3)
button_45 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_45.grid(row=4,column=5)
button_46 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_46.grid(row=4,column=6)
button_47 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_47.grid(row=4,column=7)
button_48 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_48.grid(row=4,column=8)
button_49 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_49.grid(row=4,column=9)
button_50 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_50.grid(row=5,column=0)
button_51 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_51.grid(row=5,column=1)
button_52 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_52.grid(row=5,column=2)
button_54 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_54.grid(row=5,column=4)
button_55 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_55.grid(row=5,column=5)
button_56 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_56.grid(row=5,column=6)
button_57 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_57.grid(row=5,column=7)
button_58 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_58.grid(row=5,column=8)
button_59 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_59.grid(row=5,column=9)
button_60 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_60.grid(row=6,column=0)
button_61 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_61.grid(row=6,column=1)
button_62 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_62.grid(row=6,column=2)
button_65 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_65.grid(row=6,column=5)
button_66 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_66.grid(row=6,column=6)
button_67 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_67.grid(row=6,column=7)
button_68 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_68.grid(row=6,column=8)
button_69 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_69.grid(row=6,column=9)
button_70 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_70.grid(row=7,column=0)
button_71 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_71.grid(row=7,column=1)
button_73 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_73.grid(row=7,column=3)
button_74 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_74.grid(row=7,column=4)
button_75 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_75.grid(row=7,column=5)
button_76 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_76.grid(row=7,column=6)
button_77 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_77.grid(row=7,column=7)
button_78 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_78.grid(row=7,column=8)
button_79 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_79.grid(row=7,column=9)
button_81 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_81.grid(row=8,column=1)
button_82 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_82.grid(row=8,column=2)
button_83 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_83.grid(row=8,column=3)
button_84 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_84.grid(row=8,column=4)
button_85 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_85.grid(row=8,column=5)
button_86 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_86.grid(row=8,column=6)
button_87 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_87.grid(row=8,column=7)
button_88 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_88.grid(row=8,column=8)
button_89 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_89.grid(row=8,column=9)
button_90 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_90.grid(row=9,column=0)
button_92 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_92.grid(row=9,column=2)
button_94 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_94.grid(row=9,column=4)
button_95 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_95.grid(row=9,column=5)
button_96 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_96.grid(row=9,column=6)
button_97 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_97.grid(row=9,column=7)
button_98 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_98.grid(row=9,column=8)
button_99 = Button(gridFrame, width = "40",height = "40", image=default_image)
button_99.grid(row=9,column=9)
button_0.config(command = lambda: safe("0", "button_0"))
button_1.config(command = lambda: safe("1", "button_1"))
button_2.config(command = lambda: safe("3", "button_2"))
button_4.config(command = lambda: safe("4", "button_4"))
button_5.config(command = lambda: safe("2", "button_5"))
button_6.config(command = lambda: safe("1", "button_6"))
button_7.config(command = lambda: safe("0", "button_7"))
button_8.config(command = lambda: safe("2", "button_8"))
button_10.config(command = lambda: safe("0", "button_10"))
button_11.config(command = lambda: safe("1", "button_11"))
button_16.config(command = lambda: safe("1", "button_16"))
button_17.config(command = lambda: safe("0", "button_17"))
button_18.config(command = lambda: safe("2", "button_18"))
button_20.config(command = lambda: safe("0", "button_20"))
button_21.config(command = lambda: safe("1", "button_21"))
button_22.config(command = lambda: safe("3", "button_22"))
button_23.config(command = lambda: safe("4", "button_23"))
button_24.config(command = lambda: safe("4", "button_24"))
button_25.config(command = lambda: safe("2", "button_25"))
button_26.config(command = lambda: safe("1", "button_26"))
button_27.config(command = lambda: safe("0", "button_27"))
button_28.config(command = lambda: safe("2", "button_28"))
button_29.config(command = lambda: safe("2", "button_29"))
button_30.config(command = lambda: safe("0", "button_30"))
button_31.config(command = lambda: safe("0", "button_31"))
button_32.config(command = lambda: safe("1", "button_32"))
button_34.config(command = lambda: safe("3", "button_34"))
button_35.config(command = lambda: safe("2", "button_35"))
button_36.config(command = lambda: safe("0", "button_36"))
button_37.config(command = lambda: safe("0", "button_37"))
button_38.config(command = lambda: safe("1", "button_38"))
button_40.config(command = lambda: safe("0", "button_40"))
button_41.config(command = lambda: safe("0", "button_41"))
button_42.config(command = lambda: safe("2", "button_42"))
button_43.config(command = lambda: safe("4", "button_43"))
button_45.config(command = lambda: safe("2", "button_45"))
button_46.config(command = lambda: safe("0", "button_46"))
button_47.config(command = lambda: safe("0", "button_47"))
button_48.config(command = lambda: safe("1", "button_48"))
button_49.config(command = lambda: safe("1", "button_49"))
button_50.config(command = lambda: safe("0", "button_50"))
button_51.config(command = lambda: safe("0", "button_51"))
button_52.config(command = lambda: safe("3", "button_52"))
button_54.config(command = lambda: safe("7", "button_54"))
button_55.config(command = lambda: safe("4", "button_55"))
button_56.config(command = lambda: safe("0", "button_56"))
button_57.config(command = lambda: safe("0", "button_57"))
button_58.config(command = lambda: safe("0", "button_58"))
button_59.config(command = lambda: safe("0", "button_59"))
button_60.config(command = lambda: safe("0", "button_60"))
button_61.config(command = lambda: safe("1", "button_61"))
button_62.config(command = lambda: safe("4", "button_62"))
button_65.config(command = lambda: safe("2", "button_65"))
button_66.config(command = lambda: safe("0", "button_66"))
button_67.config(command = lambda: safe("0", "button_67"))
button_68.config(command = lambda: safe("0", "button_68"))
button_69.config(command = lambda: safe("0", "button_69"))
button_70.config(command = lambda: safe("1", "button_70"))
button_71.config(command = lambda: safe("2", "button_71"))
button_73.config(command = lambda: safe("5", "button_73"))
button_74.config(command = lambda: safe("4", "button_74"))
button_75.config(command = lambda: safe("2", "button_75"))
button_76.config(command = lambda: safe("0", "button_76"))
button_77.config(command = lambda: safe("0", "button_77"))
button_78.config(command = lambda: safe("0", "button_78"))
button_79.config(command = lambda: safe("0", "button_79"))
button_81.config(command = lambda: safe("3", "button_81"))
button_82.config(command = lambda: safe("3", "button_82"))
button_83.config(command = lambda: safe("2", "button_83"))
button_84.config(command = lambda: safe("1", "button_84"))
button_85.config(command = lambda: safe("0", "button_85"))
button_86.config(command = lambda: safe("0", "button_86"))
button_87.config(command = lambda: safe("0", "button_87"))
button_88.config(command = lambda: safe("0", "button_88"))
button_89.config(command = lambda: safe("0", "button_89"))
button_90.config(command = lambda: safe("2", "button_90"))
button_92.config(command = lambda: safe("2", "button_92"))
button_94.config(command = lambda: safe("1", "button_94"))
button_95.config(command = lambda: safe("0", "button_95"))
button_96.config(command = lambda: safe("0", "button_96"))
button_97.config(command = lambda: safe("0", "button_97"))
button_98.config(command = lambda: safe("0", "button_98"))
button_99.config(command = lambda: safe("0", "button_99"))
root.mainloop()