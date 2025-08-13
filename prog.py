'''ПРОГРАММА'''
import tkinter as tk
from tkinter import Label, PhotoImage
from company import Materials2

root = tk.Tk()
root.title('Программа на tkinter')
root.geometry('800x600')
root.resizable(False, False)
root.configure(bg='#FFFFFF')
shapla = Label(root, text='шапка', bg='#2D6033', fg ='white',
               font=('Gabriolla', 20), width=50, height=2)
shapla.place(x=0, y=15)

image = PhotoImage(file='icon.png')
image = image.subsample(25)  # Уменьшаем изображение в 25 раз
image_label = Label(shapla, image=image, bg='#2D6033')
image_label.place(x=5, y=10)

def get_materials():
    '''вывод данных из таблицы '''
    materials = Materials2.select()
    return materials

mat = get_materials()
print(mat)

root.mainloop()
