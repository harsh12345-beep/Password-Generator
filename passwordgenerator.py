from tkinter import *
import random, string
import pyperclip
root = Tk()
root.geometry("400x400")
root.config(bg="lightblue")
root.maxsize(400,400)
root.title(" PASSWORD GENERATOR")
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold',bg="lightblue").pack(fill="x")
Label(root, text ='Created by Harsh', font ='arial 15 bold').pack(side = BOTTOM)
label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
len = IntVar()
length = Spinbox(root, from_= 8, to_ = 32 , textvariable = len , width = 15).pack()
str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    str.set(password)
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = str).pack()
def Copypassword():
    pyperclip.copy(str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copypassword).pack(pady=5)
root.mainloop()
