import qrcode, tkinter as tk
from tkinter import font

root = tk.Tk()
root.geometry("860x560")
root.configure(background="#00284d")
root.resizable(False,False)
tk.Wm.wm_title(root, "Hola")
text = tk.StringVar(root)
name = tk.StringVar(root)

def convert():
    img = qrcode.make(text.get())
    img.save(name.get()+".png")

def clean():
    text.set("")
    name.set("")

tk.Label(
    text="Type the text you want to convert to \nQR Code.You can write anything, \nincluding URL links.",
    bg="#005cb3",
    fg="White",
    font=("Courier", 25, "bold"),
    border=3,
    relief="solid"

    ).pack(fill=tk.BOTH)

tk.Label(
    text="TEXT:",
    bg="#005cb3",
    fg="White",
    font=("Courier", 30, "bold"),
    padx=10,
    pady=10,
    border=2,
    relief="solid"

    ).place(x=20,y=190)

tk.Label(
    text="FILE NAME:",
    bg="#005cb3",
    fg="White",
    font=("Courier", 30, "bold"),
    padx=10,
    pady=10,
    border=2,
    relief="solid"

    ).place(x=20,y=300)


txt_enter = tk.Entry(
    bg="#005cb3",
    fg="White",
    textvariable=text,
    font=("Courier", 15, "bold"),
    width=50,
    border=2,
    relief="solid",
    justify="center"

).place(x=210,y=190, height=70)

filename = tk.Entry(
    bg="#005cb3",
    fg="White",
    textvariable=name,
    font=("Courier", 15, "bold"),
    width=40,
    border=2,
    relief="solid",
    justify="center"

).place(x=330,y=300, height=70)

tk.Button(
    text="CONVERT",
    bg="#005cb3",
    fg="White",
    font=("Courier", 30, "bold"),
    border=5,
    relief="raised",
    justify="center",
    command=convert

).place(x=590,y=410)

tk.Button(
    text="CLEAN",
    bg="#005cb3",
    fg="White",
    font=("Courier", 30, "bold"),
    border=5,
    relief="raised",
    justify="center",
    command=clean

).place(x=360,y=410)

tk.mainloop()

