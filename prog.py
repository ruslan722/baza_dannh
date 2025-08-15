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

y_posihion = 100

for i in mat:
    stroka = Label(root, bg='#BBD9B2', width= 108, height= 7)
    stroka.place(x=20, y= y_posihion)
    text_type = Label(stroka, text=f'{i.type}', bg = '#BBD9B2', font=('Gabriolla', 12))
    text_type.place(x=5, y= 5)
    text_name = Label(stroka, text=f'| {i.name}' , bg = '#BBD9B2', font=('Gabriolla', 12))
    text_name.place(x= 70, y=5)
    text_min_core = Label(stroka, text=f'Минимальное количество: {i.min_core}',
                          bg= '#BBD9B2', font=('Gabriolla', 9))
    text_min_core.place(x=5, y=25)
    y_posihion += 130

root.mainloop()
