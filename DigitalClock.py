from tkinter import *
from time import strftime

root = Tk()
root.title('Digital Clock')
root.geometry('600x130')

def display_time():
    c_time = strftime('%I:%M:%S %p')
    label_time.config(text=c_time)
    label_time.after(1000, display_time)

label_time = Label(root, text='Time', font=('Arial', 60), bg='darkgreen', fg='white')
label_time.pack()

display_time()

root.mainloop()