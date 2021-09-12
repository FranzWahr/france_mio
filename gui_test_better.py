# Program to open a web page
import urllib.request
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

root = tk.Tk()
root.title("Postcoordination SNOMED Tool")
root.geometry('600x400+50+50')
root.attributes('-alpha', 0.5) #transparency setting
root.attributes('-topmost', 1) #window order setting

# setting the windows size
root.geometry("400x200")

# declaring string variable
# for storing name
name_var = tk.StringVar()

#weitere globale variable zum speichern
webpage = ""
#webpage = "https://www.python.org/"
#alt_wp = "https://www.wikipedia.org/"

def check_URL_syntax(URL):
    #TODO
    new_label = tk.Label(root, text="no syntax checked so far")
    new_label.grid(row=5, column=0)
    return True


def open_page():
    page_getter = name_var.get()
    if check_URL_syntax(page_getter) != True: raise Exception("Invalid URL")

    if len(page_getter) > 0:
        wp = name_var.get()
        new_label = tk.Label(root, text= "The website has been updated to : " + wp)
        new_label.grid(row=4,column=0)
    else :
        new_label = tk.Label(root, text="Website input is empty!")
        new_label.grid(row=1, column=1)
        wp = webpage
        #   raise Exception("No input. Type in a website... will be directed to " + webpage)

    print("The website is : " + wp)
    name_var.set("")

    try:
        driver = webdriver.Chrome()
        driver.get(wp)
    except :
        new_label = tk.Label(root, text='An error occured due to invalid input.\n Webpage "' + wp + '"could not be opened automatically')
        new_label.grid(row=4, column=0)

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
name_entry.grid(row=1, column=0)
wp_btn.grid(row=2,column=0)
info_label.grid(row=4,column=0)

# performing an infinite loop
# for the window to display
root.mainloop()
