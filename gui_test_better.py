# Program to open a web page
import urllib.request
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name
name_var = tk.StringVar()

#weitere globale variable zum speichern
webpage = "https://www.python.org/"
#alt_wp = "https://www.wikipedia.org/"

def open_page():
    page_getter = name_var.get()
    #if len(page_getter)==0:
    #   raise Exception("No input. Type in a website... will be directed to " + webpage)
    if len(page_getter) > 0:
        wp = name_var.get()
        new_label = tk.Label(root, text= "The website has been updated to : " + wp)
        new_label.grid(row=5,column=0)
    else :
        print("Empty input default website is : " + webpage)
        wp = webpage


    print("The website is : " + wp)
    name_var.set("")

    driver = webdriver.Chrome()
    driver.get(wp)

"""
    #get page content
    page = urllib.request.urlopen(webpage)
    print(page.read())
"""


# creating a label for
# name using widget Label
name_label = tk.Label(root, text='Webpage link', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

#button for webpage opening
wp_btn = tk.Button(root, text='Open web page',command=lambda: open_page())

info_label = tk.Label(root, text = "By default the webage is set to : " + webpage)
#Input_textfield = tk.Text(root, height = 5, width = 52)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
wp_btn.grid(row=3,column=1)
info_label.grid(row=4,column=0)
#Input_textfield.grid(row=4, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
