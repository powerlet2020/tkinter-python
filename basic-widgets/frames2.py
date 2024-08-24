from  tkinter import *

window = Tk()
window.geometry('500x400')
window.title('Frames Two')
window.resizable(False,False)

frame1 = Frame(window, width=100, highlightbackground='red',highlightthickness=3)
frame1.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)

l1= Label(frame1,text='Enter the dollar:', fg='blue',font=15)
l1.grid(row=0, column=0,padx=10,pady=10)

textbox = Entry(frame1,fg='green',font=16)
textbox.grid(row=0,column=1, padx=10, pady=10)

button1= Button(frame1,text='Convert to Cedi',fg='blue',font=16)
button1.grid(row=1,column=1,sticky=N)




window.mainloop()