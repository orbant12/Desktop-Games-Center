import turtle
from subprocess import call

current_state = "Leaderboard"

# Creating a window screen
wn = turtle.Screen()
wn.title("Leaderboard")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Function to clear the screen
def clear_screen():
    #restart the app
    wn.clear()
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)



    

# Snake Game Leaderboard
def snakeLeaderboard():
    clear_screen()
    try:
        with open("GlobalRecords/personal_record_snake.txt", "r") as file:
            personalRecord = int(file.read())
    except FileNotFoundError:
        pass
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Snake Game Leaderboard", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -50)
    pen.write("Personal Record: " + str(personalRecord), align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -100)
    pen.write("Press 'q' to go back", align="center", font=("Courier", 24, "normal"))
    wn.onkeypress(launchLeaderboard, "q")

# Flippy Bird Leaderboard
def flippyBirdLeaderboard():
    clear_screen()
    try:
        with open("GlobalRecords/personal_record_flippy.txt", "r") as file:
            personalRecord = int(file.read())
    except FileNotFoundError:
        pass
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Flippy Bird Leaderboard", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -50)
    pen.write("Personal Record: " + str(personalRecord), align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -100)
    pen.write("Press 'q' to go back", align="center", font=("Courier", 24, "normal"))
    wn.onkeypress(launchLeaderboard, "q")

# Cookie Clicker Leaderboard
def cookieClickerLeaderboard():
    clear_screen()
    try:
        with open("GlobalRecords/personal_record_cookie.txt", "r") as file:
            personalRecord = int(file.read())
    except FileNotFoundError:
        pass
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Cookie Clicker Leaderboard", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -50)
    pen.write("Personal Record: " + str(personalRecord), align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -100)
    pen.write("Press 'q' to go back", align="center", font=("Courier", 24, "normal"))
    wn.onkeypress(launchLeaderboard, "q")


#Back to Launcher
def backToLauncher():
    #Clsoe this window only
    wn.bye()
    #Call the launcher
    call(["python", "./gameLuncher.py"])


# Launch the Leaderboard
def launchLeaderboard():
    clear_screen()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Leaderboard", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, 100)
    pen.write("1. Snake Game", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, 50)
    pen.write("2. Flippy Bird", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, 0)
    pen.write("3. Cookie Clicker", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -50)
    pen.write("4. Exit", align="center", font=("Courier", 24, "normal"))
    wn.onkeypress(snakeLeaderboard, "1")
    wn.onkeypress(flippyBirdLeaderboard, "2")
    wn.onkeypress(cookieClickerLeaderboard, "3")
    wn.onkeypress(backToLauncher, "4")

# Loop
launchLeaderboard()
wn.listen()  # Listen for events
wn.mainloop()
