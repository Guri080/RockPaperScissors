from tkinter import *
import random as rnd

## Basic window settings (size, color, title, etc) ##
window = Tk()  # instantiate an instance of a window
window.geometry("800x650")
window.title("Rock Paper Scissors")
window.resizable(0, 0)
window.config(bg="#F5DEB3")

## Variables ##
playerScore = 0
compScore = 0
x = IntVar()

## Images (rock, paper, scissors)
rock_img = PhotoImage(file='images/rock1.png')
paper_img = PhotoImage(file='images/paper1.png')
scissors_img = PhotoImage(file='images/scissors1.png')

big_rock_img = PhotoImage(file='images/rock.png')
big_paper_img = PhotoImage(file='images/paper.png')
big_scissors_img = PhotoImage(file='images/scissors.png')

user_pick = ["Rock", "Paper", "Scissors"]
game_img = [rock_img, paper_img, scissors_img]
game_img_big = [big_rock_img, big_paper_img, big_scissors_img]


def getCompPick():  # computer's pick
    global comp_pick_num
    if comp_pick_num == 0:
        compPick = "rock"
    elif comp_pick_num == 1:
        compPick = "paper"
    else:
        compPick = "scissors"

    return compPick


def play():
    global playerScore
    global compScore
    global comp_pick_num
    comp_pick_num = rnd.randint(0, 2)

    comp_pick = getCompPick()
    user_throw = user_pick[x.get()].lower()
    if user_throw == comp_pick:
        Result.config(text='tie,you both select same')
    elif user_throw == 'rock' and comp_pick == 'paper':
        Result.config(text='you lose,computer selected paper')
        compScore += 1
    elif user_throw == 'rock' and comp_pick == 'scissors':
        Result.config(text='you win,computer selected scissors')
        playerScore += 1
    elif user_throw == 'paper' and comp_pick == 'scissors':
        Result.config(text='you lose,computer selected scissors')
        compScore += 1
    elif user_throw == 'paper' and comp_pick == 'rock':
        Result.config(text='you win,computer selected rock')
        playerScore += 1
    elif user_throw == 'scissors' and comp_pick == 'rock':
        Result.config(text='you lose,computer selected rock')
        compScore += 1
    elif user_throw == 'scissors' and comp_pick == 'paper':
        Result.config(text='you win ,computer selected paper')
        playerScore += 1
    else:
        Result.config(text='invalid: choose any one -- rock, paper, scissors')

    score.config(text="Player " + str(playerScore) + ":" + str(compScore) + " Computer")  # Update the player vs computer Score

    display_img_comp.config(image=game_img_big[comp_pick_num])
    print("you pressed play: " + user_pick[comp_pick_num])


def selected():  # This method represents the selected indicator in the radio buttons
    display_image.config(image=game_img_big[x.get()])  # Update an image when an indicator is selected


## All the widgets ##
# Score
score = Label(window,
              text="Player 0:0 Computer",
              bg="#F5DEB3",
              font=20,
              pady=10)
score.pack()

# display image for user's choice and the computer's choice
display_image = Label(window,  # user's choice
                      image=game_img_big[x.get()],
                      bg="#F5DEB3")  # display selected indicator image

display_image.place(x=40, y=300)

display_img_comp = Label(window,  # user's choice
                         bg="#F5DEB3")  # display selected indicator image

display_img_comp.place(x=470, y=280)

# choice label for user and computer
Label(window,  # User's choose label
      text="Choose rock paper or scissors: ",
      bg="#F5DEB3",
      font=10,
      pady=5,
      padx=10).place(x=5, y=55)

Label(window,  # Computer's choose label
      text="Computer chose: ",
      bg="#F5DEB3",
      font=10,
      pady=5,
      padx=10).place(x=470, y=55)

# radio buttons (select rock, paper or scissors)
for index in range(len(user_pick)):
    Radiobutton(window,
                text=user_pick[index],
                variable=x,
                value=index,
                image=game_img[index],
                bg='#F5DEB3',
                padx=15,
                compound='left',
                command=selected,
                font=10).place(x=10, y=120 + index * 50)

# play button
Button(window,
       text="Play",
       bg="#b57e17",
       font=20,
       command=play).place(x=380, y=550)

# result button
Result = Label(window,
               text="",
               bg="#F5DEB3",
               font=7)
Result.place(x=260, y=615)

window.mainloop()
