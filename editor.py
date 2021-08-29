import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkcode import CodeEditor
code=input("Enter File Name (wihout the .js): ")

root = tk.Tk()
root.title("PyCode - A Python-Based Code Editor for JavaScript!")
root.option_add("*tearOff", 0)

notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text=code+'.js')
notebook.pack(fill="both", expand=True)

code_editor = CodeEditor(
    tab_1,
    width=50,
    height=15,
    language="javascript",
    background="black",
    highlighter="dracula",
    font="Arial",
    autofocus=True,
    blockcursor=False,
    insertofftime=0,
    padx=10,
    pady=10,
)
code_editor.pack(fill="both", expand=True)
code_editor.content = """console.log("First Text using PyText + JavaScript!")"""
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()