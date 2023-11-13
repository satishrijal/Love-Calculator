from tkinter import *
import random

window = Tk()

def calculate_love():
    # value will contain digits between 0-9
    st = '0123456789'
    # result will be in double digits
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text = temp)





window.title("LOVE CALCULATOR BY SATISH")
window.geometry("420x420")
window.config(bg="yellow")

tile_label =Label(window,
                  text="LOVE CALCULATOR",
                  font=("Courier Bold", 30),
                  bg="#00FF00",
                  fg="black",
                  highlightthickness=4,
                  highlightbackground="blue"
                  )
tile_label.place(x=110, y=10)

name1 = Label(window,
              text = "Enter Your Name 😇:",
              font=("Courier New Bold",16),
              bg= "#FFFF00",
              fg="black",
              )
name1.place(x=130,y=80)
entry_box1 = Entry(window,
                   font=("Courier New",16),
                   bg="black",
                   fg="white",
                   highlightbackground="white")
entry_box1.place(x=130,y=110)

name2 =Label(window,
             text = "Enter Your Lovers Name 😘:",
             font=("Courier New Bold",16),
             bg= "#FFFF00",
             fg="black",
             )
name2.place(x=130,y=180)
entry_box2 = Entry(window,
                   font=("Courier New",16),
                   bg="black",
                   fg="white",
                   #relief=SOLID,
                   highlightbackground="white"
                   )
entry_box2.place(x=130,y=210)

button = Button(window,
                text= "Click Here To Check",
                bg="green",
                fg="green",
                highlightcolor="yellow",
                highlightbackground="yellow",
                command =  calculate_love
                )
button.place(x=160,y=250)

result = Label(window,
               bg="yellow",
               fg="black"

)
result.place(x=240,y=280)

window.mainloop()
