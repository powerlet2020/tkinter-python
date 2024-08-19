from tkinter import *

window = Tk()
window.geometry('600x400')
window.title('Frames Frames')

frame = LabelFrame(window, bg="yellow", text='section one' ,padx=10, pady=10 )
frame.pack()

button = Button(frame, text='click me')
button.pack()

button2 = Button(frame, text=' Dont click me')
button2.pack(padx=10, pady= 10)

frame1 = LabelFrame(window, bg='red', text='section two', padx=20, pady=20)
frame1.pack()

button3 = Button(frame1, text='1')
button3.grid(row = 0 , column=0)

button4 = Button(frame1, text= 2)
button4.grid(row=1, column=0)



window.mainloop()