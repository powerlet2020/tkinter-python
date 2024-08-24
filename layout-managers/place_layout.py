from  tkinter import *

window = Tk()
window.geometry('500x400')
window.title('Frames Two')
window.resizable(False,False)

label1 = Label(window,text='welcome powerlet',fg='blue', bg='gray')
label1.place(x=0, y=0)

label2 = Label(window,text='welcome power',fg='orange', font=15, bg='red')
label2.place(x=30, y=30)


window.mainloop()