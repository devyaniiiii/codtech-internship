from tkinter import *

def convert():
    value = float(entry.get())
    result = value * 1000
    result_label.config(text=f"{result} meters")

root = Tk()
root.title("Unit Converter")

Label(root, text="Kilometers").pack()

entry = Entry(root)
entry.pack()

Button(root, text="Convert to Meters", command=convert).pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
