from tkinter import *
import numpy as np
import pandas as pd
import re
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import (
    #FigureCanvasTkAgg,
    #NavigationToolbar2Tk
#)

class dot3(tk.Tk):
    global dict1
    dict1 = {}
    def __init__(self, window):
        self.window = window
        
        self.frame1 = Frame(self.window)
        self.label1 = Label(self.frame1, text="Welcome to data visualization.", font=("Arial", 15, "bold"), bg="black", fg="white")
        self.frame1.pack(pady=10)
        self.label1.pack()
        
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        self.frame4 = Frame(self.window)
        self.frame5 = Frame(self.window)
        self.frame6 = Frame(self.window)
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.name = Label(self.frame2, text="Student's name:", font=("Arial", 14, "bold"))
        self.name.pack(side="left")
        self.name_entry = Entry(self.frame2)
        self.name_entry.pack(side="left")
        
        self.first = Label(self.frame3, text="First exam grade:", font=("Arial", 14, "bold"))
        self.first.pack(side="left")
        self.first_entry = Entry(self.frame3)
        self.first_entry.pack(side="left")
        
        self.second = Label(self.frame4, text="Second exam grade:", font=("Arial", 14, "bold"))
        self.second.pack(side="left")
        self.second_entry = Entry(self.frame4)
        self.second_entry.pack(side="left")
        
        self.final = Label(self.frame5, text="Final exam grade:", font=("Arial", 14, "bold"))
        self.final.pack(side="left")
        self.final_entry = Entry(self.frame5)
        self.final_entry.pack(side="left")
        
        self.button1 = Button(self.frame6, text="Add", command=self.Add)
        self.button1.pack(side="left")
        
        self.button2 = Button(self.frame6, text="Bar Chart", command=self.Finish)
        self.button2.pack(side="left")
        
        self.button_3 = Button(self.frame6, text="H Bar Chart", command=self.Hbar)
        self.button_3.pack(side="left")
        
        self.button_4 = Button(self.frame6, text="Line Plots", command=self.Line)
        self.button_4.pack(side="left")
        
        self.button_5 = Button(self.frame6, text="Restart", command=self.Restart)
        self.button_5.pack(side="left")
        
        self.warning = Label(self.frame6, text="", fg="red")
        self.warning.pack(side="right")
        
        self.button2["state"] = DISABLED
        self.button_3["state"] = DISABLED
        self.button_4["state"] = DISABLED
        self.button_5["state"] = DISABLED
        
    def Add(self):
        if re.sub("[.-]", "", str(self.name_entry.get())).isdigit():
            self.warning.config(text="Please recheck student's name")
        else:
            if (str(self.first_entry.get()).replace(".", "").isdigit()) and (str(self.second_entry.get()).replace(".", "").isdigit()) and (str(self.final_entry.get()).replace(".", "").isdigit()):
                self.warning.config(text=f"")
                self.button2["state"] = NORMAL
                self.button_3["state"] = NORMAL
                self.button_4["state"] = NORMAL
                
                dict1[str(self.name_entry.get())] = [self.first_entry.get(), self.second_entry.get(), self.final_entry.get()]
                self.name_entry.delete(0, END)
                self.first_entry.delete(0, END)
                self.second_entry.delete(0, END)
                self.final_entry.delete(0, END)
            else:
                self.warning.config(text="Please recheck student's grade")
                
        
    def Finish(self):
        self.frame9 = Frame(self.window)
        self.frame9.pack()
        self.Hay = 1
        self.button1["state"] = DISABLED
        self.button2["state"] = DISABLED
        self.button_3["state"] = DISABLED
        self.button_4["state"] = DISABLED
        self.button_5["state"] = NORMAL
        for key in dict1:
            dict1[key] = [float(i) for i in dict1[key]]
        x = pd.DataFrame(dict1, index=["Exam1", "Exam2", "Exam3"])
        languages = dict1.values()
        popularity = dict1.keys()
        
        figure = Figure(figsize=(5,4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, self.frame9)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self.frame9)

        # create axes
        axes = figure.add_subplot(2,1,1)
        
        x.plot.bar(ax=axes)
        # create the barchart
        #axes.bar(languages, popularity)
        #axes.set_title('Top 5 Programming Languages')
        #axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def Hbar(self):
        self.frame9 = Frame(self.window)
        self.frame9.pack()
        self.Hay = 2
        self.button1["state"] = DISABLED
        self.button2["state"] = DISABLED
        self.button_3["state"] = DISABLED
        self.button_4["state"] = DISABLED
        self.button_5["state"] = NORMAL
        for key in dict1:
            dict1[key] = [float(i) for i in dict1[key]]
        x = pd.DataFrame(dict1, index=["Exam1", "Exam2", "Exam3"])
        languages = dict1.values()
        popularity = dict1.keys()
        
        figure = Figure(figsize=(5,4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, self.frame9)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self.frame9)

        # create axes
        axes = figure.add_subplot(2,1,1)
        
        x.plot.barh(ax=axes)
        # create the barchart
        #axes.bar(languages, popularity)
        #axes.set_title('Top 5 Programming Languages')
        #axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        
    def Line(self):
        self.frame9 = Frame(self.window)
        self.frame9.pack()
        self.Hay = 3
        self.button1["state"] = DISABLED
        self.button2["state"] = DISABLED
        self.button_3["state"] = DISABLED
        self.button_4["state"] = DISABLED
        self.button_5["state"] = NORMAL
        for key in dict1:
            dict1[key] = [float(i) for i in dict1[key]]
        x = pd.DataFrame(dict1, index=["Exam1", "Exam2", "Exam3"])
        languages = dict1.values()
        popularity = dict1.keys()
        
        self.figure = Figure(figsize=(5,4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(self.figure, self.frame9)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self.frame9)

        # create axes
        self.axes = self.figure.add_subplot(2,1,1)
        
        x.plot(ax=self.axes)
        # create the barchart
        #axes.bar(languages, popularity)
        #axes.set_title('Top 5 Programming Languages')
        #axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def Restart(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame5.destroy()
        self.frame6.destroy()
        self.frame9.destroy()
        dict1.clear()
        dot3.__init__(self, self.window)
      
        
        
        