from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(200,50)
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)


Miles = Label(text="Miles")
Miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

km_output = Label(text="0")
km_output.grid(row=1, column=1)

KM = Label(text="KM")
KM.grid(row=1, column=2)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

window.mainloop()
