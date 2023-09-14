from tkinter import *
import numpy as np
import tkinter as tk
from tkinter import ttk
import re

class dot2:
    def __init__(self, window):
        self.lover = 0
        self.lovers = 0
        self.window = window
        self.mainframe = Frame(self.window)
        self.mainframe.pack()
        
        self.title = Label(self.mainframe, text="Welcome to Inverse Matrix", font=("Arial", 14, "bold"))
        self.title.pack()
        self.label1_part1 = Label(self.mainframe, text="Type the shape of the first matrix", font=("Arial", 14, "bold"))
        self.label1_part1.pack(side="left")
        self.entry1_part1 = Entry(self.mainframe)
        self.entry1_part1.pack(side="left")
        self.label2_part1 = Label(self.mainframe, text="X")
        self.label2_part1.pack(side="left")
        self.entry2_part1 = Entry(self.mainframe)
        self.entry2_part1.pack(side="left")
        
        self.frame2 = Frame(self.window)
        self.frame2.pack()
        
        self.herewego = 0
        
        self.button1_part1 = Button(self.frame2, text="Retry", command=self.Clear)
        self.button1_part1.pack(side="left")
        self.button2_part1 = Button(self.frame2, text="Summit", command=self.Summit)
        self.button2_part1.pack(side="left")

        
    def Clear(self):
        self.entry1_part1.delete(0, END)
        self.entry2_part1.delete(0, END)
        self.button2_part1["state"] = NORMAL
        
    def Summit(self):
        self.row = self.entry1_part1.get()
        self.col = self.entry2_part1.get()
        if self.row == self.col:
            if self.lovers == 1:
                self.loves.destroy()
                
            if (str(self.row).isdigit()) and (str(self.col).isdigit()):
                if self.lover == 1:
                    self.love.destroy()
                    
                self.button2_part1["state"] = DISABLED
                self.button1_part1["state"] = DISABLED
                global list1
                global all1
                all1 = []
                list1 = []
                number = 0
                for i in range(int(self.row)):
                    x = f"frame{i}"
                    x = Frame(self.window)
                    list1.append(x)
                    list1[i].pack()
                    for j in range(int(self.col)):
                        y = f"hello {i}{j}"
                        all1.append(y)
                        all1[number] = Entry(list1[i])
                        all1[number].pack(side="left")
                        number += 1     
                self.frame_1 = Frame(self.window)
                self.frame_1.pack()
                self.button1_part2 = Button(self.frame_1, text="Clear Value", command=self.Clear2)
                self.button1_part2.pack(side="left")
                self.button2_part2 = Button(self.frame_1, text="Solve", command=self.Solve)
                self.button2_part2.pack(side="left")
                self.button3_part2 = Button(self.frame_1, text="Back to top", command=self.Backtotop)
                self.button3_part2.pack(side="left")
            else:
                if self.lover == 0:
                    self.love = Label(self.frame2, text="Type integer", fg="red")
                    self.love.pack(side="right")
                    self.lover = 1
                elif self.lover == 1:
                    self.love.destroy()
                    self.love = Label(self.frame2, text="Type integer", fg="red")
                    self.love.pack(side="right")
                elif self.lovers == 1:
                    self.loves.destroy()
                    self.love = Label(self.frame2, text="Type integer", fg="red")
                    self.love.pack(side="right")
             
        else:
            if self.lovers == 0:
                self.loves = Label(self.frame2, text="Type singular matrix. Ex: 3x3 or 2x2", fg="red")
                self.loves.pack(side="right")
                self.lovers = 1
            elif self.lovers == 1:
                self.loves.destroy()
                self.loves = Label(self.frame2, text="Type singular matrix. Ex: 3x3 or 2x2", fg="red")
                self.loves.pack(side="right")
            elif self.lover == 1:
                self.love.destroy()
                self.loves = Label(self.frame2, text="Type singular matrix. Ex: 3x3 or 2x2", fg="red")
                self.loves.pack(side="right")
            
        
    def Clear2(self):
        self.button2_part2["state"] = NORMAL
        self.button3_part2["state"] = NORMAL
        for i in range(len(all1)):
            all1[i].delete(0, END)
            
    
    def Solve(self):
        global list22
        global list222
        list22 = []
        for i in range(len(all1)):
            x = all1[i].get()
            list22.append(x)
            list222 = [True if re.sub("[.-]","",i).isdigit() == True else False for i in list22]
            
        if sum(list222) == len(list22):
            list2 = [float(i) for i in list22]
            self.button2_part2["state"] = DISABLED
            self.button3_part2["state"] = DISABLED
            self.button1_part2["state"] = DISABLED
            list2_array = np.array(list2).reshape(int(self.row), int(self.col))
            
            if np.linalg.det(list2_array) != 0:
                if self.herewego == 1:
                    self.warning2.destroy()
                    
                list2_inverse = np.linalg.inv(list2_array).reshape(1, int(self.row) * int(self.col)).tolist()
                self.final_list2 = [j for i in list2_inverse for j in i]
                global list3
                list3 = []
                yy = 0
                for i in range(int(self.row)):
                    xx = f"frame_2 {i}"
                    list3.append(xx)
                    list3[i] = Frame(self.window)
                    list3[i].pack()
                    for j in range(int(self.col)):
                        self.entry_part3 = Entry(list3[i])
                        self.entry_part3.insert(0, self.final_list2[yy])
                        self.entry_part3.pack(side="left")
                        yy += 1
                        
                self.frame_3 = Frame(self.window)
                self.frame_3.pack()
                self.button3_part4 = Button(self.frame_3, text="Back to top", command=self.Clean)
                self.button3_part4.pack()
            else:
                self.bigframe = Frame(self.window)
                self.bigframe.pack()
                self.biglabel = Label(self.bigframe, text="It is singular matrix", font=("Arial", 23, "bold"))
                self.biglabel.pack(side="top")
                self.bigbutton = Button(self.bigframe, text="Back to top", command=self.Cleans)
                self.bigbutton.pack(side="bottom")
        else:
            self.warning2 = Label(self.frame_1, text="Recheck value inside the matrix", fg="red")
            self.warning2.pack(side="right")
            self.herewego = 1
            
        
        
        
    def Backtotop(self):
        for i in range(len(list1)):
            list1[i].destroy()
        self.frame_1.destroy()
        self.button1_part1["state"] = NORMAL
        
    def Clean(self):
        dot2.Backtotop(self)    
        for i in range(len(list3)):
            list3[i].destroy()
        self.frame_3.destroy()
        self.button1_part1["state"] = NORMAL
    
    def Cleans(self):
        dot2.Backtotop(self)
        self.button1_part1["state"] = NORMAL
        self.bigframe.destroy()
    
    
    
    
    
    