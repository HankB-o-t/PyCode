import tkinter as tk
from tkinter import Frame, Label, Menu, Scrollbar, Text, ttk
from tkinter import font
from tkinter import filedialog
from tkinter.constants import BOTTOM, E, END, INSERT, RIGHT, X, Y
from tkcode import CodeEditor
code=input("Enter File Name (wihout the .py): ")

global open_status_name
open_status_name = False

root = tk.Tk()
root.title("PyCode - A Python-Based Code Editor!")
root.option_add("*tearOff", 0)

notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text=code+'.py')
notebook.pack(fill="both", expand=True)

code_editor = CodeEditor(
    tab_1,
    width=50,
    height=15,
    language="python",
    background="black",
    highlighter="azure",
    font="Arial",
    autofocus=True,
    blockcursor=False,
    insertofftime=0,
    padx=10,
    pady=15,
)
code_editor.pack(fill="both", expand=True)
code_editor.content = """print("Hello World!")"""

# Create Files Function
def new_file():
    code_editor.delete("1.0", END)
    root.title("New File - PyCode!")
    status_bar.config(text="New File        ")

    global open_status_name
    open_status_name = False

# Open Files Function
def open_file():
    # Delete Previous text
    code_editor.delete("1.0", END)
    # File Dialog
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("Text Files", "*.txt"), ("Python files", "*.py"), ("JavaScript files", "*.js"), ("HTML files", "*.html"), ("CSS files", "*.css"), ("Other files", "*.*")))
    
    # Check FileName
    if text_file:
        global open_status_name
        open_status_name = text_file

    # Update Status Bar
    name = text_file
    status_bar.config(text=f'{name}        ')
    name.replace("C:/", "")
    root.title(f'{name} - PyText!')

    # Open File
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # OPEN THE CONTENT OF THE FILE
    code_editor.insert(END, stuff)
    # Close the opened file
    text_file.close()

# Save As files
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save As", filetypes=(("Text Files", "*.txt"), ("Python files", "*.py"), ("JavaScript files", "*.js"), ("HTML files", "*.html"), ("CSS files", "*.css"), ("Other files", "*.*")))
    if text_file:
        # Update StatusBar
        name = text_file
        status_bar.config(text=f'Saved As: {name}        ')
        name = name.replace("C:/", "")
        root.title(f'{name} - PyText!')

        # save the file
        text_file = open(text_file, 'w')
        text_file.write(code_editor.get(1.0, END))
        # Close File
        text_file.close()

# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # save the file
        text_file = open(open_status_name, 'w')
        text_file.write(code_editor.get(1.0, END))
        # Close File
        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}        ')
    else:
        save_as_file()

# Cut Text
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if code_editor.selection_get():
            selected = code_editor.selection_get()
            code_editor.delete("sel.first", "sel.last")
            # Clear the clipboard and append
            root.clipboard_clear()
            root.clipboard_append(selected)

# Copy Text
def copy_text(e):
    global selected
    # Check if used keyboard shortcut
    if e:
        selected = root.clipboard_get()

    if code_editor.selection_get():
        selected = code_editor.selection_get()
        # Clear the clipboard and then append
        root.clipboard_clear()
        root.clipboard_append(selected)

# Paste Text
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = code_editor.index(INSERT)
            code_editor.insert(position, selected)



# Create Scrollbar
text_scroll = Scrollbar(tab_1)
text_scroll.pack(side=RIGHT, fill=Y)


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy            (Ctrl+C)", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste            (Ctrl+V)", command=lambda: paste_text(False))
edit_menu.add_command(label="Cut               (Ctrl+X)", command=lambda: cut_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Undo            (Ctrl+Z)", command=code_editor.edit_undo)
edit_menu.add_command(label="Redo            (Ctrl+Y)", command=code_editor.edit_redo)

# Add StatusBar to bottom of the APP
status_bar = Label(root, text="UnSaved File        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)


root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()