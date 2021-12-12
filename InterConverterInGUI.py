# Using Tkinter

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('1200x700')
root.title('Interconverter')

# Variables
num = IntVar()
bin_num = StringVar()
octal_num = StringVar()
hexadeci_num = StringVar()

# Functions
def enter():
    number = num.get()
    bin = bin_num(number)
    bin_num.set(bin)

    oct = octal_num(number)
    octal_num.set(oct)

    hexa = hexadeci_num(number)
    hexadeci_num.set(hexa)

def clear():
    num.set('')
    bin_num.set('')
    octal_num.set('')
    hexadeci_num.set('')

def exit():
    alerter = messagebox.askyesno('Alert', 'Are you sure to exit?')

    if alerter > 0:
        root.destroy()

    
# The UI design
num_label = Label(root, text='Number', font='arial 25 bold', bg='green', fg='white').grid(row=0, column=0, padx=100, pady=10)
num_txt = Entry(root, width=30, bd=5, textvariable=num).grid(row=0, column=1, padx=10, pady=10)

num_label = Label(root, text='Binary Number', font='arial 25 bold', bg='green', fg='white').grid(row=2, column=0, padx=100, pady=10)
num_txt = Entry(root, width=30, bd=5, textvariable=bin_num).grid(row=2, column=1, padx=10, pady=10)

num_label = Label(root, text='Octal Number', font='arial 25 bold', bg='green', fg='white').grid(row=4, column=0, padx=100, pady=10)
num_txt = Entry(root, width=30, bd=5, textvariable=octal_num).grid(row=4, column=1, padx=10, pady=10)

num_label = Label(root, text='Hexa Decimal Number', font='arial 25 bold', bg='green', fg='white').grid(row=6, column=0, padx=100, pady=10)
num_txt = Entry(root, width=30, bd=5, textvariable=hexadeci_num).grid(row=6, column=1, padx=10, pady=10)

enterButt = Button(root, text=' Enter ', font='arial 20 bold', fg='blue', bg='gray', command = enter).grid(row=10, column=1, padx=10, pady=10)

clearButt = Button(root, text=' Clear ', font='arial 20 bold', fg='blue', bg='gray', command = clear).grid(row=14, column=1, padx=10, pady=10)

exitButt = Button(root, text=' Exit ', font='arial 20 bold', fg='blue', bg='gray', command = exit).grid(row=14, column=2, padx=10, pady=10)

root.mainloop()
