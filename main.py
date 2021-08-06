from tkinter import *
import random
import os

class notepad(Tk):
    def __init__(self,root):
        self.my_menu = Menu(root)
        root.config(menu=self.my_menu)

        #Menu configuration
        self.file_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.__new)
        self.file_menu.add_command(label="Save", command=self.__save)
        self.file_menu.add_command(label="Save as", command=self.__save_window)
        self.file_menu.add_command(label="Open", command=self.__open_window)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.__exit)

        self.note = Text(root)
        self.note.pack()
        self.fileName = ""

    # Notedpad functions


    def __new(self):
        self.note.delete("1.0",END)

    def __save(self):
        if self.fileName == "":
            self.__save_window()
            return
        file = open(self.fileName,"w")
        file.write(self.note.get("1.0",END))

    def __saveas(self,newName):
        if newName == "" or os.path.isfile(newName):
            return
        self.fileName = newName
        newfile = open(newName,"w")
        text_to_save = self.note.get("1.0",END)
        newfile.write(text_to_save)
        newfile.close()
        self.newWindow.destroy()

    def __save_window(self):
         self.newWindow = Toplevel()
         self.newWindow.grab_set()

         label = Label(self.newWindow, text="Enter a File name")
         label.pack(fill='x', padx=50, pady=5)

         newName = Entry(self.newWindow)
         newName.pack()

         button_enter = Button(self.newWindow, text="Enter", command=lambda : self.__saveas(newName.get()))
         button_enter.pack(fill='x')


    def __open(self,name):
        if name == "":
            return
        if os.path.isfile(name):
            self.fileName = name
            self.__new()
            with open(self.fileName,"r") as f:
                     self.note.insert("1.0",f.read())
            self.newWindow2.destroy()

    def __open_window(self):
        self.newWindow2 = Toplevel()

        label = Label(self.newWindow2, text="Enter a File name")
        label.pack(fill='x', padx=50, pady=5)

        name = Entry(self.newWindow2)
        name.pack()

        button_enter = Button(self.newWindow2, text="Enter", command=lambda: self.__open(name.get()))
        button_enter.pack(fill='x')


    def __exit(self):
        root.quit()



root = Tk()
np = notepad(root)
root.mainloop()
