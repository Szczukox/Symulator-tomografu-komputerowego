from tkinter import *

root = Tk()
root.title("Symulator tomografu komputerowego")
root.resizable(0, 0)


def callback(event):
    print("clicked at", event.x, event.y)


f = Frame(root, height=600, width=800)
f.pack()

button = Button(text="EXIT", width=20, height=2)
button.pack()
button.place(x=330, y=530)

scale1 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale1.pack()
scale1.place(x=120, y=300)

scale2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale2.pack()
scale2.place(x=350, y=300)

scale3 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
scale3.pack()
scale3.place(x=570, y=300)

root.mainloop()
