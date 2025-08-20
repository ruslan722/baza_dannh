'''ПРОГРАММА'''
import tkinter as tk
from tkinter import Label, PhotoImage, messagebox
from company import Materials2

root = tk.Tk()
root.title('Программа на tkinter')
root.geometry('800x600')
root.resizable(False, False)
root.configure(bg='#FFFFFF')

def first_window(event=None):
    '''Функционал окна '''

    shapla = Label(root, text='Первое окно', bg='#2D6033', fg ='white',
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
        stroka = Label(root, bg='#BBD9B2', width= 108, height= 5)
        stroka.place(x=20, y= y_posihion)
        text_type = Label(stroka, text=f'{i.type}', bg = '#BBD9B2', font=('Gabriolla', 12))
        text_type.place(x=5, y= 5)
        text_name = Label(stroka, text=f'| {i.name}' , bg = '#BBD9B2', font=('Gabriolla', 12))
        text_name.place(x= 70, y=5)
        text_min_core = Label(stroka, text=f'Минимальное количество: {i.min_core}',
                            bg= '#BBD9B2', font=('Gabriolla', 9))
        text_min_core.place(x=5, y=25)

        text_core = Label(stroka, text=f'Количество на складе: {i.core}' ,
                        bg= '#BBD9B2',  font=('Gabriolla', 9))
        text_core.place(x=5, y=40)
        text_price = Label(stroka,
                            text= f'Цена: {i.edinisa} /единица измерения | {i.core_ypakovka} ',
                        bg= '#BBD9B2',  font=('Gabriolla', 9))
        text_price.place(x=5, y=55)
        text_tr_core = Label(stroka, text=f'Требуемое количество: {i.tr_core}',
                            bg = '#BBD9B2', font=('Gabriolla', 12))
        text_tr_core.place(x=500, y= 5)

        y_posihion += 90


def two_window(event=None):
    '''Функционал окна '''

    shapla = Label(root, text='Второе окно', bg='#2D6033', fg ='white',
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
        stroka = Label(root, bg='#BBD9B2', width= 108, height= 5)
        stroka.place(x=20, y= y_posihion)
        text_type = Label(stroka, text=f'{i.type}', bg = '#BBD9B2', font=('Gabriolla', 12))
        text_type.place(x=5, y= 5)
        text_name = Label(stroka, text=f'| {i.name}' , bg = '#BBD9B2', font=('Gabriolla', 12))
        text_name.place(x= 70, y=5)
        text_min_core = Label(stroka, text=f'Минимальное количество: {i.min_core}',
                            bg= '#BBD9B2', font=('Gabriolla', 9))
        text_min_core.place(x=5, y=25)

        text_core = Label(stroka, text=f'Количество на складе: {i.core}' ,
                        bg= '#BBD9B2',  font=('Gabriolla', 9))
        text_core.place(x=5, y=40)
        text_price = Label(stroka,
                            text= f'Цена: {i.edinisa} /единица измерения | {i.core_ypakovka} ',
                        bg= '#BBD9B2',  font=('Gabriolla', 9))
        text_price.place(x=5, y=55)
        text_tr_core = Label(stroka, text=f'Требуемое количество: {i.tr_core}',
                            bg = '#BBD9B2', font=('Gabriolla', 12))
        text_tr_core.place(x=500, y= 5)

        y_posihion += 90

    messagebox.showerror('ОШИБКА! ', 'Данные не обновились')
    messagebox.showwarning('ВНИМАНИЕ! ', 'Ошибка соединения ')
    messagebox.showinfo('Успешно', 'Соединение восстановлено, данные обновлены')

button_back = Label(root, text='Назад', bg = "#2D6033",
                     fg= 'white', width=15,
                     font=('Gabriolla', 9))
button_back.place(x=220, y=550)
button_back.bind('<Button-1>', lambda e: first_window())

button_forward = Label(root, text='Вперёд', bg = "#2D6033",
                     fg= 'white', width=15,  font=('Gabriolla', 9))
button_forward.place(x=450, y=550)
button_forward.bind('<Button-1>', lambda e: two_window())
first_window()

root.mainloop()
