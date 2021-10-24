from tkinter import *
import random
#to define the window
root=Tk()
root.geometry('500x500')
root.title("Rock, Paper, Scissors")
root.resizable(0,0)
root.config(bg="light pink")
Label(root,text="Come lets play Rock, Paper and Scissors").pack()

#to enter your choice
user_take = StringVar()
Label(root, text = " choose one out of rock, paper and scissors" , bg="cyan").place(x=125,y=80)
Entry(root, textvariable = user_take , bg="white").place(x=175,y=150)


#let's start the main game
Result = StringVar()
def play():
    choose=['rock','paper','scissor']
    computer_pick=random.choice(choose)
    user_pick=user_take.get()
    if(user_pick == computer_pick):
        Result.set("It's a tie, you both selected the same")
    elif(user_pick=="rock" and computer_pick=="paper"):
        Result.set("You lost!! computer chose paper")
    elif(user_pick=="paper" and computer_pick=="rock"):
        Result.set("You Won!! computer chose rock")
    elif(user_pick=="rock" and computer_pick=="scissors"):
        Result.set("You Won!! computer chose scissors")
    elif(user_pick=="scissors" and computer_pick=="rock"):
        Result.set("You lost!! computer chose rock")
    elif(user_pick=="scissors" and computer_pick=="paper"):
        Result.set("You won!! computer chose paper")
    elif(user_pick=="paper" and computer_pick=="scissors"):
        Result.set("You lost!! computer chose scissors")
    else:
        Result.set("invalid choice: choose any one from: rock, paper, scissors")

def Reset():
    Result.set("")
    user_take.set("")

    
def Exit():
    root.destroy()

Entry(root,textvariable=Result, bg="white", width=55).place(x=70,y=250)
Button(root,text="PLAY",command=play,padx=10).place(x=100,y=300)
Button(root,text="RESET",command=Reset,padx=10).place(x=200,y=300)
Button(root,text="EXIT",command=Exit,padx=10).place(x=300,y=300)
root.mainloop()
