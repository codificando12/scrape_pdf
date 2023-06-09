from tkinter import *
from tkinter import filedialog
from read_folder import read_dir


def search_path():
    folder_path = filedialog.askdirectory()
    path_label.configure(text=folder_path)

root = Tk()

root.geometry("500x500")
# root.resizable(False,False)

title_label = Label(root, text="Generate a txt or docxs with all the names file of \n specific folder")
title_label.grid(row=0, column=1)

folder_label = Label(root, text="Folder")
folder_label.grid(row=1, column=0, padx=2, pady=2)

path_label = Label(root, pady=2, bg="White", width=50)
path_label.grid(row=1, column=1)

browse_button = Button(root, text="Browse", command=search_path)
browse_button.grid(row=1, column=2, padx=6)


# def browse():
#     myLabel = Label(root, text="Look I am working well")
#     myLabel.pack()

# myButton = Button(root, text="Browse",command= browse)
# myButton.pack()


root.mainloop()