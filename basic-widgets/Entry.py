from tkinter import *

def button_command():
    print('powerlet')

def show_text():
    text = Entry2.get()
    print(text)

def my_function():
    text = 'my practice'
    entry3.insert(0, text)

window = Tk()
window.geometry('600x400')
window.title('Basic Entry Practice')

Entry1 = Entry(window,width=15)
Entry1.pack()

button1 = Button(window,text='click me', command=button_command, bg='gold')
button1.pack()

Entry2 = Entry(window, width=20)
Entry2.pack()

button2 = Button(window, text='Sign in', bg='red', fg='gray', command= show_text)
button2.pack()

entry3 = Entry(window, width=25)
entry3.pack()

button3 = Button(window, text='sing up', bg='#766685', fg='white', command=my_function )
button3.pack()




window.mainloop()
