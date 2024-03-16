'''
Write a full Python script that creates a Tkinter window with the text "Python rocks!".
'''
import tkinter as tk
window = tk.Tk()

label = tk.Label(text="Python rocks!")
label.pack()

window.mainloop()