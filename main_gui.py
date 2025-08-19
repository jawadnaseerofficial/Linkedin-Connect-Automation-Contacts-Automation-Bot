import tkinter as tk
import subprocess

def run_notebook():
    subprocess.run([
        "jupyter", "nbconvert", 
        "--to", "notebook", 
        "--execute", 
        "--inplace", 
        "Linkedin Connect Automation Contacts Automation Bot.ipynb"
    ])

root = tk.Tk()
root.title("LinkedIn Bot")
root.geometry("300x150")

button = tk.Button(root, text="Run LinkedIn Bot", command=run_notebook)
button.pack(pady=40)

root.mainloop()
