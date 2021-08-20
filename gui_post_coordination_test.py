import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Postcoordination SNOMED Tool")
root.geometry('600x400+50+50')
root.attributes('-alpha', 0.5) #transparency setting
root.attributes('-topmost', 1) #window order setting

def button_clicked():
    print('Button clicked')

def select(option):
    print(option)


ttk.Label(root, text='Themed Label').pack()

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()


ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()

