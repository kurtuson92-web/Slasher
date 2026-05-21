from tkinter import *
import random


fg_colors = ["Blue", "Green", "Indigo", "Orange", "Red", "Violet", "Yellow"]
#Choices bot
choices = ["Rock", "Paper", "Scissors"]

window = Tk()

# title change color added
window.title("JACK EN POY") #Dhayle Tabamo, Kurt Angel Uson, Infante Jaynard, Navarro Josell, Elijah Pineda, Suba Marian Sofie, Reyes Junel
window.geometry("500x500")
window.config(bg="light gray")



#Title
Game_title = Label(
    window,
    text="Rock, Paper, Scissors",
    font=("Arial",30,"bold"),
    bg="light gray"
)

def change_colors():
    Game_title.config(fg=random.choice(fg_colors))
    Game_title.after(700, change_colors)

change_colors()

#Your Choice Label
Your_Choice = Label(
    window,
    text="You Picked: "
)

#Enemy Choice Label
Enemy_Choice = Label(
    window,
    text="Computer Picked: "
)

# result out put
#Result Label
Result = Label(
    window,
    text="Result: "
)

# Game Logic

# Game logic came from revised file from other team
# Logical operator (OR) is used to shorten blocks of codes
# instead of just 3 incomplete outputs from other team, optimized to DRAW,WIN and LOSE els ifs
# like on the other team you can see your choice and enemy choice
def GameFlow(player):

    enemy = random.choice(choices)

    Your_Choice.config(text=f"You Picked: {player}")

    Enemy_Choice.config(text=f"Computer Picked: {enemy}")

    #Draw
    if player == enemy:
        Result.config(text="Result: Draw!")

    # Win
    elif (
        (player == "Rock" and enemy == "Scissors") or
        (player == "Paper" and enemy == "Rock") or
        (player == "Scissors" and enemy == "Paper")
    ):
        Result.config(text="Result: You Win!")

    #Lose
    else:
        Result.config(text="Result: Computer Wins!")

#parameters of GameFlow are now from function then function is added to the button
# parameters (player) will determined by button choice

#Rock
def rock_button():
    GameFlow("Rock")

#Paper
def paper_button():
    GameFlow("Paper")

#Scissors
def scissors_button():
    GameFlow("Scissors")

#Rock Button
Rock_choice = Button(
    window,
    text="Rock",
    fg="white",
    bg="green",
    command=rock_button
)

#Paper Button
Paper_choice = Button(
    window,
    text="Paper",
    fg="white",
    bg="green",
    command=paper_button
)

#Scissors Button
Scissor_choice = Button(
    window,
    text="Scissors",
    fg="white",
    bg="green",
    command=scissors_button
)


Game_title.pack()

Your_Choice.pack()

Enemy_Choice.pack()

Result.pack()


# just relativity positions of button
# more like a cartician plane function of X and Y axis of the window
Rock_choice.pack()
Rock_choice.place(relx=0.2,rely=0.5)

Paper_choice.pack()
Paper_choice.place(relx=0.45,rely=0.5)

Scissor_choice.pack()
Scissor_choice.place(relx=0.70,rely=0.5)

window.mainloop()