import turtle
import time
import random
from subprocess import call

# Function to display preparation text
def display_preparation_text():
    pen.clear()
    pen.color("white")
    pen.write("Welcome to Snake Game \n Press 'w' to start \n Press 'q' to exit.", align="center", font=("candara", 16, "bold"))


#Exit and Launcher Launch
def exit_game():
    wn.bye()
    # Call the launcher
    call(["python", "./gameLuncher.py"])

def fade_in_out():
    pen.clear()
    pen.color("white")
    pen.write("CONGRATULATIONS! YOU WON!", align="center", font=("candara", 24, "bold"))
    time.sleep(0.5)
    pen.clear()
    wn.ontimer(fade_in_out, 500)  # Schedule next fade

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

# The width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# Head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)

# Assigning key directions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# Function to start the game
def start_game():
    display_preparation_text()  # Display preparation text
    time.sleep(0.5)  # Pause for 3 seconds before starting the game
    move_snake()  # Start the game

# Function to move the snake
def move_snake():
    global score, high_score
    while True:
        wn.update()

        # Collision with walls
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            # Reset the game
            # Reset the snake's head position and direction
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

        # Collision with food
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            # Adding body to the snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            segments.append(new_segment)

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

        # Move the snake
        move()

        # Check for head collision with body segments
        for segment in segments:
            if segment.distance(head) < 20:
                # Reset the game
                # Reset the snake's head position and direction
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                segments.clear()

                # Reset the score
                score = 0
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

        # Delay for smoother gameplay
        time.sleep(0.1)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(exit_game, "q")


segments = []

# Initialization of score and high_score outside the game loop
score = 0
high_score = 0

# Start the game
start_game()
