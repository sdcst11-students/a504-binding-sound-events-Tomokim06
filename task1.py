import playsound
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("500x100")


def b1sound():
    playsound.playsound("Minecraft.mp3",block=False)
def b2sound():
    playsound.playsound("Wedonotcare.mp3",block=False)
def b3sound():
    playsound.playsound("Catmeow.mp3",block=False)
def b4sound():
    playsound.playsound("Android.mp3",block=False)
def b5sound():
    playsound.playsound("Ding.mp3",block=False)
def b6sound():
    playsound.playsound("Noooooo.mp3",block=False)
def b7sound():
    playsound.playsound("Tyler1.mp3",block=False)
def b8sound():
    playsound.playsound("Yeet.mp3",block=False)

label = Label(win, text="Press Buttons for Sound!")

b1 = Button(win, text="Minecraft Click", width=15, command = b1sound)
b2 = Button(win, text='"We do not care"',width=15, command = b2sound)
b3 = Button(win, text="Cat meow",width=15, command = b3sound)
b4 = Button(win, text="Android sound",width=15, command = b4sound)
b5 = Button(win, text="ding",width=15, command = b5sound)
b6 = Button(win, text='"noooooo"',width=15, command = b6sound)
b7 = Button(win, text="Tyler1 machine gun",width=15, command = b7sound)
b8 = Button(win, text='"Yeet"',width=15, command = b8sound)

b1.place(x=10,y=30)
b2.place(x=130,y=30)
b3.place(x=250,y=30)
b4.place(x=370,y=30)
b5.place(x=10,y=60)
b6.place(x=130,y=60)
b7.place(x=250,y=60)
b8.place(x=370,y=60)
label.place(x=185,y=1)

win.mainloop()