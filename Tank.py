from tkinter import *

#left,top,right,bottom

window = Tk()
window.title("Simple Tank")
window.geometry("300x300")

canvas = Canvas(window, width=100, height=100, bg="gray")
canvas.pack()

# tank body
canvas.create_rectangle(25,15,40,85,fill="black")
canvas.create_rectangle(75,15,60,85,fill="black")
canvas.create_rectangle(30, 20, 70, 80, fill="darkGreen")
canvas.create_rectangle(37,30, 63, 70, fill="green")
canvas.create_rectangle(45, 10, 55,50, fill="lightgreen")



window.mainloop()
