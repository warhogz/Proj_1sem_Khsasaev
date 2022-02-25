#В соответствии с номером варианта перейти по ссылке на прототип.
#Реализовать его в IDE PyCharm Community с применением пакета tk.
#Получить интерфейс максимально приближенный к оригиналу
#https://pbs.twimg.com/media/CWgn_1CUAAAVQP4.png:large

from tkinter import *

root = Tk()
root.title("delivery")
root.geometry('450x450')
root.configure(bg='#d3d3d3')

Label(text='Регион', width=65, height=3, fg='black',bg='#d3d3d3', font='arial 12').place(x=-220, y=5)
Label(text='Район', width=65, height=3, fg='black', bg='#d3d3d3',font='arial 12').place(x=-220, y=60)
Label(text='Город', width=65, height=3, fg='black', bg='#d3d3d3', font='arial 12').place(x=-220, y=110)
Label(text='Улица', width=65, height=3, fg='black', bg='#d3d3d3',font='arial 12').place(x=-220, y=160)
Label(text='Дом', width=65, height=3, fg='black', bg='#d3d3d3',font='arial 12').place(x=-225, y=230)
Entry(width=9, font='arial 12').place(x=130, y=250)
Label(text='Стр./вл.', width=65, height=3, fg='black', bg='#d3d3d3', font='arial 12').place(x=-215, y=280)
Entry(width=9, font='arial 12').place(x=130, y=300)
Label(text='Корпус', width=10, height=3, fg='black', bg='#d3d3d3',font='arial 12').place(x=220, y=230)
Entry(width=9, font='arial 12').place(x=320, y=250)
Label(text='Кв./Офис', width=10, height=3, fg='black',bg='#d3d3d3', font='arial 12').place(x=220, y=280)
Entry(width=9, font='arial 12').place(x=320, y=300)
Button(root, width=6, text='OK',  bg=('#e3e1df'), fg='#3fa6da', font=("Arial Bold", 20)).place(x=100, y=350)
Button(root, width=7, text='ОТМЕНА',bg=('#e3e1df'),  fg='#3fa6da', font=("Arial Bold", 20)).place(x=250, y=350)
from tkinter.ttk import *
combo = Combobox(root, width = 55)
combo['values']= ("[ не выбранo ]", "Ростовская область", "Рязанская область", "Республика Дагестан", "Чеченская Республика", "Волгоградская область")
combo.current(0) #Элемент выбранный по умолчанию
combo.place(x=50, y=50)

combo = Combobox(root, width = 55)
combo['values']= ( "Выберите район", "Матвеево-Курганский район",  "Пронский район",  "Кизилюртовский район",  "Ачхой-Мартановский район",  "Кумылженский район")
combo.current(0) #Элемент выбранный по умолчанию
combo.place(x=50, y=100)

combo = Combobox(root, width = 55)
combo['values']= ("Выберите город", "Шахты", "Рязань", "Кизилюрт", "Ачхой-Мартан", "Волжский")
combo.current(0) #Элемент выбранный по умолчанию
combo.place(x=50, y=150)

combo = Combobox(root, width = 55)
combo['values']= ("Выберите улицу", "ул. Текучева", "ул. Новая", "ул. Салютина", "ул. Почтовая", "ул. Космическая")
combo.current(0) #Элемент выбранный по умолчанию
combo.place(x=50, y=200)



root.mainloop()