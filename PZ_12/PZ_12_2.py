# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# Программа взята из ПЗ_7-2
# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти количество слов в строке
import tkinter as tk

def words():
        text1 = str(text.get())
        textLen = len(text1)
        num = 0
        if textLen > 0:
            for i in range(1, textLen):
                if (text1[i]) == ' ' and text1[i - 1] != ' ':
                    num += 1
        qq.config(text="Количество слов в строке: {}".format(num + 1))

root = tk.Tk()
root.geometry('200x80')
text = tk.Entry(root, width = 30)
text.pack()
qq = tk.Label(root, text="Введите слова")
qq.pack()
button = tk.Button(root, text='Нажать', command=words)
button.pack()
root.mainloop()