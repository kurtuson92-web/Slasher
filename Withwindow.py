from tkinter import *
import random

bg_colors = ["Yellow","Blue","Green","Orange","Red","Indigo","Violet"]
number = 0


window = Tk()

window.title("TANK BLAST")
window.geometry("500x500")

window.config(
    bg="Gray"
)

#GAME NAME
Game_name = Label(window,
    text="Welcome",
    font=("Arial",40,"bold"),
    bg="Gray"
)
def change_colors():
    Game_name.config(fg=random.choice(bg_colors))
    Game_name.after(700, change_colors)

change_colors()

#ENTER Game



def entering():
    Game_name.config(text="TANK BLAST",)

def show():
    Game_fun.pack()
    Add_num.pack()
    
    Add_num.place(relx=0.5,rely=0.4,anchor=("s"))


def both():
    show()
    entering()

Enter_game = Button(
    text="Enter Game",
    font=("Arial",10,"bold"),
    bg="LightGreen",
    command=both
)



def add_one():
    global number
    number += 1
    Game_fun.config(text=f"ADD {number}",)

Add_num = Button(
    text="Add",
    font=("Arial",10,"bold"),
    bg="LightGreen",
    command=add_one
)

Game_fun = Label(
    text="ADD "
)

Game_name.pack()
Game_name.place(relx=0.5,rely=0.1,anchor=("center"))
Enter_game.pack()
Enter_game.place(relx=0.5,rely=0.5,anchor=("center"))


window.mainloop()