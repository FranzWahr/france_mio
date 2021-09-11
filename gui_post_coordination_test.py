import urllib.request

import tkinter as tk
from tkinter import ttk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#todo continue tutorial here: https://www.pythontutorial.net/tkinter/tkinter-event-binding/
#todo research connection python browser

root = tk.Tk()
root.title("Postcoordination SNOMED Tool")
root.geometry('600x400+50+50')
root.attributes('-alpha', 0.5) #transparency setting
root.attributes('-topmost', 1) #window order setting

# declaring string variable
# for storing page to be accessed
webpage_var=tk.StringVar()


# defining a function that will
# get the webpage_var and
# print them on the screen
def submit():
    wp_name = webpage_var.get()
    print("The name is : " + wp_name)
    webpage_var.set("")


def button_clicked():
    print('Button clicked')

def select(option):
    print(option)

def open_page(pagename):
    driver = webdriver.Chrome()
    driver.get(pagename)
    page = urllib.request.urlopen(pagename)
    print(page.read())

ttk.Label(root, text='Themed Label').pack()

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()
# ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
# ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
# ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()
 ttk.Button(root, text='Open web page : "http://www.python.org"', command=lambda: open_page('http://www.python.org')).pack()


# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=webpage_var, font=('calibre', 10, 'normal'))


# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()

