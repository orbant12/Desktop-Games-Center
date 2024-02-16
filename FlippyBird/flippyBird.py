import pygame, sys
from pygame.locals import *
import random
import time

# Set up pygame
pygame.init()

# Set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Flippy Bird')

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139,69,19)
GOLD = (255,215,0)

# Set up the fonts
basicFont = pygame.font.SysFont(None, 48)
smallFont = pygame.font.SysFont(None, 36)

# Set up the bird
bird = pygame.Rect(50, 250, 30, 30)
birdColor = GOLD
birdSpeed = 5
birdY = 250
birdYChange = 0

# Set up the ground
ground = pygame.Rect(0, 550, 800, 50)
groundColor = RED

# Set up the pipes
pipeWidth = 50
pipeColor = GREEN
pipeSpeed = 5
pipeX = 800

# Initialize pipe1 and pipe2
pipe1 = pygame.Rect(pipeX, 0, pipeWidth, 0)
pipe2 = pygame.Rect(pipeX, 0, pipeWidth, 0)

# Function to generate random pipe heights
def generate_pipe_height():
    return random.randint(100, 400)

# Reset the pipes
def reset_pipes():
    global pipeX
    top_pipe_height = generate_pipe_height()
    pipe1 = pygame.Rect(pipeX, 0, pipeWidth, top_pipe_height)
    pipe2 = pygame.Rect(pipeX, top_pipe_height + 200, pipeWidth, WINDOWHEIGHT - top_pipe_height - 200)
    return pipe1, pipe2

pipe1, pipe2 = reset_pipes()

# Set up the score
score = 0 
scoreText = smallFont.render('Score: ' + str(score), True, WHITE)
scoreTextRect = scoreText.get_rect()
scoreTextRect.centerx = windowSurface.get_rect().centerx
scoreTextRect.centery = 50

# Set up the personal record
personalRecord = 0

# Load personal record from file
try:
    with open("GlobalRecords/personal_record_flippy.txt", "r") as file: 
        personalRecord = int(file.read())
except FileNotFoundError:
    pass

# Function to update personal record
def update_personal_record():
    global personalRecord, score
    if score > personalRecord:
        personalRecord = score
        with open("GlobalRecords/personal_record_flippy.txt", "w") as file:
            file.write(str(personalRecord))

# Run the game loop
while True:
    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                birdYChange = -10
        if event.type == KEYUP:
            if event.key == K_SPACE:
                birdYChange = 5

    # Move the bird
    birdY += birdYChange
    bird.y = birdY

    # Move the pipes
    pipeX -= pipeSpeed
    pipe1.x = pipeX
    pipe2.x = pipeX

    # Check for collision with the ground
    if bird.colliderect(ground):
        break

    # Check for collision with the pipes
    if bird.colliderect(pipe1) or bird.colliderect(pipe2):
        break

    # Check if the pipes have gone off the screen
    if pipe1.x < -pipeWidth:
        pipe1, pipe2 = reset_pipes()
        pipeX = WINDOWWIDTH
        score += 1
        update_personal_record()

    # Draw the background
    windowSurface.fill(BLACK)

    # Draw the bird
    pygame.draw.rect(windowSurface, birdColor, bird)

    # Draw the ground
    pygame.draw.rect(windowSurface, groundColor, ground)

    # Draw the pipes
    pygame.draw.rect(windowSurface, pipeColor, pipe1)
    pygame.draw.rect(windowSurface, pipeColor, pipe2)

    # Draw the score
    scoreText = smallFont.render('Score: ' + str(score), True, WHITE)
    windowSurface.blit(scoreText, scoreTextRect)

    # Draw the personal record
    personalRecordText = smallFont.render('Personal Record: ' + str(personalRecord), True, WHITE)
    personalRecordTextRect = personalRecordText.get_rect()
    personalRecordTextRect.centerx = windowSurface.get_rect().centerx
    personalRecordTextRect.centery = 100
    windowSurface.blit(personalRecordText, personalRecordTextRect)

    # Draw the game over text
    if bird.colliderect(ground) or bird.colliderect(pipe1) or bird.colliderect(pipe2):
        windowSurface.blit(gameOverText, gameOverTextRect)
        pygame.draw.rect(windowSurface, gameOverButtonColor, gameOverButton)
        windowSurface.blit(gameOverButtonText, gameOverButtonTextRect)

    # Draw the window onto the screen
    pygame.display.update()

    # Check for the game over event
    if bird.colliderect(ground) or bird.colliderect(pipe1) or bird.colliderect(pipe2):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if gameOverButton.collidepoint(event.pos):
                    # Reset the game
                    bird.y = 250
                    pipe1, pipe2 = reset_pipes()
                    pipeX = WINDOWWIDTH
                    score = 0
                    birdY = 0
                    birdYChange = 0
                    break
    
    # Update the display
    pygame.display.update()
    time.sleep(0.01)

# Quit the game   
pygame.quit()
