from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
import tkinter as tk

window = Tk()
window.title("Акимов Алексей Сергеевич")
window.geometry("300x300")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1 , text="Калькулятор")
tab_control.add(tab2,text="Чекбоксы")
tab_control.add(tab3,text="Текст")

lbl1 = Label(tab1, text="1")
lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text="2")
lbl2.grid(column=0, row=0)

lbl3 = Label(tab3, text="3")
lbl3.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

rad1 = Radiobutton(lbl2, text="первый",value=1)
rad2 = Radiobutton(lbl2, text="воторой",value=2)
rad3 = Radiobutton(lbl2, text="третий",value=3)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

def clicked():
    messagebox.showinfo("Выбор", "Выбран чекбокс")
btn = Button(lbl2, text="Выбор", command=clicked)
btn.grid(column=0, row=1)

def readFile():
   file =  open('file').read()
   messagebox.showinfo("файл открыт", file)

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = combo_op.get()
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Ошибка: введите числа")

entry_num1 = tk.Entry(tab1)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

combo_op = ttk.Combobox(tab1, values=["+", "-", "*"], width=3)
combo_op.current(0)
combo_op.grid(row=0, column=1, padx=5, pady=5)

entry_num2 = tk.Entry(tab1)
entry_num2.grid(row=0, column=2, padx=5, pady=5)

btn_calc = tk.Button(tab1, text="Вычислить", command=calculate)
btn_calc.grid(row=0, column=3, padx=5, pady=5)

label_result = tk.Label(tab1, text="Результат:")
label_result.grid(row=1, column=0, columnspan=4)

window.mainloop()







