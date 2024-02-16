import turtle
from subprocess import call

# Global variable to track the current state
current_state = "Launcher"

# Function to clear the screen
def clear_screen():
    turtle.clear()

# Function to go back to the Launcher menu
def back_to_launcher():
    global current_state
    current_state = "Launcher"
    clear_screen()
    show_launcher_menu()

# Function to show the Launcher menu
def show_launcher_menu():
    menu_options = {
        "1": ("Snake Game", game_snake),
        "2": ("Cookie Clicker", game_cookie),
        "3": ("Flippy Bird", game_flippy_bird),
        "4": ("Leaderboard", game_leaderboard),
        "5": ("Exit", exit_game)
    }
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Welcome to Game Launcher", align="center", font=("candara", 24, "bold"))

    y_position = 150
    for key, (label, _) in menu_options.items():
        pen.goto(0, y_position)
        pen.write(f"{key}. {label}", align="center", font=("candara", 24, "bold"))
        y_position -= 50

    return menu_options

# Keyboard bindings
def keyboard_bindings(menu_options):
    wn.listen()
    for key in menu_options.keys():
        wn.onkeypress(menu_options[key][1], key)

# Menu for Snake Game
def game_snake():
    global current_state
    current_state = "SnakeGame"
    wn.bye()
    call(["python", "./SnakeGame/snake.py"])

# Menu for Cookie Clicker Game
def game_cookie():
    global current_state
    current_state = "CookieClicker"
    wn.bye()
    call(["python", "./CookieClicker/cookieClicker.py"])


# Menu for Flippy Bird Game
def game_flippy_bird():
    global current_state
    current_state = "FlippyBird"
    wn.bye()
    call(["python", "./FlippyBird/flippyBird.py"])


# Menu for Leaderboard
def game_leaderboard():
    global current_state
    current_state = "Leaderboard"
    wn.bye()
    call(["python", "./GlobalRecordsLeaderboard/leaderBoard.py"])


# Menu for Exit
def exit_game():
    wn.bye()

# Creating a window screen
wn = turtle.Screen()
wn.title("Game Launcher")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Initial setup
menu_options = show_launcher_menu()
keyboard_bindings(menu_options)

# Launcher loop
while True:
    wn.update()
