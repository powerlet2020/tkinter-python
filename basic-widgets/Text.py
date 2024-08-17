from tkinter import *

def get_text():
    print(text.get(1.0, 'end'))

def insert_text():
    text.insert(1.0, 'hello powerlet')

def delete_text():
    text.delete(1.0, 'end')

window = Tk()
window.geometry('600x400')
window.title('Text Widget')

# creating the text
text = Text(window, width=15,height=8, font=('arial, 15'))
text.pack()

get_button = Button(window,text='get text', command=get_text)
get_button.pack()

insert_button = Button(window, text='insert text', command=insert_text)
insert_button.pack()

delete_button = Button(window, text='delete text', command= delete_text)
delete_button.pack()



window.mainloop()