'''Окно материалов для приложения на Tkinter'''
import tkinter as tk
from tkinter import Label
from company import Materials
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title('Материалы')

square = Label(root, text='Материалы', font=('Constantia', 20), bg='#1D476B', fg='white', width= 75)

square.place(x=0, y=0)

root.mainloop()
