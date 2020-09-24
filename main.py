from tkinter import *

root = Tk()

root.title("Calcuator")
root.geometry("400x380")
root.iconbitmap('calc_icon.ico')

def calc_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def calc_clear():
    e.delete(0, END)

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def calc_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def calc_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":    
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

def calc_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def calc_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def calc_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)
    
button_1  = Button(root, text="1", padx=40, pady=20, command=lambda: calc_click(1))
button_2  = Button(root, text="2", padx=40, pady=20, command=lambda: calc_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: calc_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: calc_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: calc_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: calc_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: calc_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: calc_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: calc_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: calc_click(0))
button_equal = Button(root, text="=", padx=40, pady=20, command=calc_equal)
button_clear = Button(root, text="C", padx=40, pady=20, command=calc_clear)
button_add = Button(root, text="+", padx=40, pady=20, command=calc_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=calc_subtract)
button_multiply = Button(root, text="X", padx=40, pady=20, command=calc_multiply)
button_divide = Button(root, text="÷", padx=40, pady=20, command=calc_divide)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)

button_equal.grid(row=5, column=2)
button_clear.grid(row=5, column=0)
button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=5, column=3)

root.mainloop()
