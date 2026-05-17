from tkinter import *
import random

bg_colors = ["Yellow","Blue","Green","Orange","Red","Indigo","Violet"]


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
    Game_name.after(400, change_colors)

change_colors()

#ENTER Game
def entering():
    Game_name.config(text="TANK BLAST",)

Enter_game = Button(
    text="Enter Game",
    font=("Arial",10,"bold"),
    bg="LightGreen",
    command=entering
)


Game_name.pack()
Enter_game.pack()
Enter_game.place(relx=0.5,rely=0.5,anchor=("center"))

window.mainloop()