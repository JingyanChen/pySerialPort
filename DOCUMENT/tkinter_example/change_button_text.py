import tkinter as tk

root = tk.Tk()

def update_btn_text():
    btn_text.set("b")

btn_text = tk.StringVar()
btn = tk.Button(root, textvariable=btn_text, command=update_btn_text)
btn_text.set("a")

btn.pack()

root.mainloop()