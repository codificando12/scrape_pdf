from tkinter import *
from tkinter import filedialog
from read_folder import read_dir

"""This function will open the folder browser for the user to choose the folder that he/she
wants to scan"""
def search_path():
    global folder_path
    folder_path = filedialog.askdirectory()
    path_label.configure(text=folder_path) #this will save the folder path in a label

def start_scan():

    file_list = read_dir(folder_path)
    

    
folder_path = "" #save the folder path that search_path() function returns


root = Tk() #start tkinter

root.geometry("500x500") # set the window dimension
# root.resizable(False,False)

title_label = Label(root, text="Generate a txt or docxs with all the names file of \n specific folder")
title_label.grid(row=0, column=1)

folder_label = Label(root, text="Folder")
folder_label.grid(row=1, column=0, padx=2, pady=2)

path_label = Label(root, bg="White", width=50)
path_label.grid(row=1, column=1)

browse_button = Button(root, text="Browse", command=search_path)
browse_button.grid(row=1, column=2, padx=6)

check_folder = Button(root, text='Scan', command=start_scan)
check_folder.grid(row = 2, column = 2)


root.mainloop()