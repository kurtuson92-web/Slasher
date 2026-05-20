from tkinter import *
import random

bot_choice = ["Rock", "Paper" , "Scissor"]


window =Tk()

window.title("JACK EN POY")     #Dhayle Tabamo, Kurt Angel Uson, Infante Jaynard, Navarro Josell, Elijah Pineda, Suba Marian Sofie, Reyes Junel
window.geometry("450x400")


Game_title = Label(window,
    text = "Rock, Paper, Scissor"
)



def choices():
    bot_choice  = random.choice
    Enemy_Choice.config(text = "Computer Picked: {bot_choice}")



Enemy_Choice = Label(window,
                     text = "Computer Picked: ")

Rock_choice = Button(
    text="Rock",
    font=("Arial",10,"bold"),
    bg="LightGreen",
    command=choices
)


Game_title.pack()
Rock_choice.pack()
Enemy_Choice.pack()


window.mainloop()