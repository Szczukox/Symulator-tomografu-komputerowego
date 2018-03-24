from tkinter import *
from PIL import Image
from PIL import ImageTk
from tomo import *

# PARAMETRY:
WIDTH_WINDOW = 1250
HEIGHT_WINDOW = 700
WIDTH_IMAGE = 400
HEIGHT_IMAGE = 400

root = Tk()
root.title("Symulator tomografu komputerowego")
root.resizable(0, 0)

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()

x_position = (width_screen / 2) - (WIDTH_WINDOW / 2)
y_position = (height_screen / 2) - (HEIGHT_WINDOW / 2)

root.geometry('%dx%d+%d+%d' % (WIDTH_WINDOW, HEIGHT_WINDOW, x_position, y_position))

f = Canvas(root, width=WIDTH_WINDOW, height=HEIGHT_WINDOW)
f.pack()

'''button = Button(text="EXIT", width=20, height=2)
button.pack()
button.place(x=330, y=530)'''

label_step = Label(root, text="Krok:")
label_step.pack()
label_step.place(x=50, y=528)
scale_step = Scale(root, from_=1, to=90, orient=HORIZONTAL)
scale_step.pack()
scale_step.place(x=250, y=510)

label_detector = Label(root, text="Liczba rzutów na detektory:")
label_detector.pack()
label_detector.place(x=50, y=568)
scale_detector = Scale(root, from_=1, to=1000, orient=HORIZONTAL)
scale_detector.pack()
scale_detector.place(x=250, y=550)

label_beta = Label(root, text="Kąt rozwarcia:")
label_beta.pack()
label_beta.place(x=50, y=608)
scale_beta = Scale(root, from_=1, to=360, orient=HORIZONTAL)
scale_beta.pack()
scale_beta.place(x=250, y=590)

label_iterations = Label(root, text="Liczba iteracji:")
label_iterations.pack()
label_iterations.place(x=50, y=648)
scale_iterations = Scale(root, from_=1, to=(len(range(0, 360, step))), orient=HORIZONTAL)
scale_iterations.pack()
scale_iterations.place(x=250, y=630)

label_input_image = Label(root, text="Obraz wejściowy:")
label_input_image.pack()
label_input_image.place(x=165, y=50)
display_image = Image.fromarray(input_image)
resized = display_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_image = ImageTk.PhotoImage(resized)
f.create_image(212, 300, image=display_image)

label_sinogram = Label(root, text="Sinogram:")
label_sinogram.pack()
label_sinogram.place(x=595, y=50)
input_image2 = Image.fromarray(input_image)
resized2 = input_image2.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
input_image2 = ImageTk.PhotoImage(resized2)
f.create_image(624, 300, image=input_image2)

label_output_image = Label(root, text="Obraz wyjściowy:")
label_output_image.pack()
label_output_image.place(x=985, y=50)
input_image3 = Image.fromarray(input_image)
resized3 = input_image3.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
input_image3 = ImageTk.PhotoImage(resized3)
f.create_image(1036, 300, image=input_image3)

root.mainloop()
