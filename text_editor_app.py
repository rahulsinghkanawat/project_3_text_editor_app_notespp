#3#text editor app 
#import tkinter for creating GUI
import tkinter as tk

from tkinter import filedialog, messagebox

#main window
root=tk.Tk()
root.title("Text Editor App")
root.geometry("800x600")

#creating a text widget for the text editor
text_area=tk.Text(root, wrap="word", font=("arial", 12))
text_area.pack(expand=True, fill="both")


#main logic starts here
#function1-to create a new file
def create_new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Text Editor App")


#function2- to open an existing file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text_area.insert(tk.END, file.read())



#function3. - save the file
def save_file():
    file_path= filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Documents", "*.txt"), ("ALL Files", "*,*")])
    
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

    messagebox.showinfo("save", "file saved successfully")


#fuction4- to exit the application
def exit_app():
    if messagebox.askokcancel("exit", "do you want to exit?"):
        root.destroy()

#creating a menu bar
menu=tk.Menu(root)
root.config(menu=menu)

filedialog_menu=tk.Menu(menu, tearoff=0)
filedialog_menu.add_command(label="New", command=create_new_file)
filedialog_menu.add_command(label="Open", command=open_file)
filedialog_menu.add_command(label="save", command=save_file)
filedialog_menu.add_cascade(label="exit", command=exit_app)
menu.add_cascade(label="file", menu=filedialog_menu)


#starts and keeps the window open until the user closes it
root.mainloop()

