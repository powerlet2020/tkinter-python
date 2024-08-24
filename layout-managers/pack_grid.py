from  tkinter import *

window = Tk()
window.geometry('500x400')
window.title('Frames Two')
window.resizable(False,False)

label1 = Label(window,text='welcome powerlet',fg='blue', bg='gray')
label1.pack(side=LEFT)

label2 = Label(window,text='welcome power',fg='orange', font=15, bg='red')
label2.pack(side=RIGHT, ipadx=10, ipady=10)


window.mainloop()