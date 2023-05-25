from tkinter import *
import time

class timerxd:
    def __init__(self,master):
        self.master = master
        self.timer_label = Label(self.master, text = "00:00", fg = "blue", font = ("Arial", 30), bg = "gray", padx = 20, pady = 10)
        self.timer_label.pack()
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        timer_string = "{:1d}:{:1d}".format(minutes, seconds)
        self.timer_label.config(text = timer_string)
        self.master.after(1000, self.update_timer)
        
root = Tk()

timer_app = timerxd(root)

mainloop()        
        
        
