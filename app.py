# This code was written by Shreharan for the Youtube Channel Stark Intelligence
import pyautogui        # importing module
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)     # creating a window
canvas.pack()


def takeScreenshot():       # creating a function
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)


myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='yellow', fg='black', font=10)      # creating a button
canvas.create_window(150, 150, window=myButton)

root.mainloop()
