from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.geometry("332x432")
root.configure(bg="#003366")
root.resizable(width=False, height=False)
root.iconbitmap("calculator_icon.ico")

equation = StringVar()
expression = ""

def button_click(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        add = ""
        add = str(eval(expression))
        equation.set(add)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def all_clear():
    global expression
    equation.set("0")
"""
def clear():
    global expression
    length = len(equation.get())
    e.delete(length - 1, "end")
"""
equation = StringVar()
equation.set("0")

e = Entry(root, borderwidth=3, justify="right", font=("arial", 20, "bold"), textvariable=equation)
e.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=22, pady=5)


button1 = Button(root, text="1", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(1))
button2 = Button(root, text="2", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(2))
button3 = Button(root, text="3", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(3))
button4 = Button(root, text="4", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(4))
button5 = Button(root, text="5", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(5))
button6 = Button(root, text="6", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(6))
button7 = Button(root, text="7", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(7))
button8 = Button(root, text="8", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(8))
button9 = Button(root, text="9", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(9))
button0 = Button(root, text="0", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click(0))
buttonDot = Button(root, text=".", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click("."))

buttonallClear = Button(root, text="AC", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=all_clear)
buttonEqual = Button(root, text="=", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=equal)
buttonPlus = Button(root, text="+", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click("+"))
buttonMinus = Button(root, text="-", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click("-"))
buttonMultiply = Button(root, text="*", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click("*"))
buttonDivide = Button(root, text="/", font=("times new roman",12), relief="ridge", bd=1, bg="#b3d9ff", width=8, height=3, command=lambda: button_click("/"))


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonDot.grid(row=4, column=2)

buttonPlus.grid(row=4, column=3)
buttonMinus.grid(row=3, column=3)
buttonMultiply.grid(row=2, column=3)
buttonDivide.grid(row=1, column=3)
buttonallClear.grid(row=4, column=1)
buttonEqual.grid(row=5, column=0, columnspan=4, ipadx=123)


root.mainloop()