#Cookie Clicker Game 

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
pygame.display.set_caption('Cookie Clicker')

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

# Set up the text
text = basicFont.render('Cookie Clicker', True, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Set up the buttons
cookieButton = pygame.Rect(300, 350, 200, 200)
cookieButtonColor = BROWN
cookieButtonTextColor = WHITE
#border radius and custom cursor
pygame.draw.rect(windowSurface, cookieButtonColor, cookieButton, 10, border_radius=50)
pygame.mouse.set_cursor(*pygame.cursors.diamond)
pygame.mouse.set_cursor(*pygame.cursors.tri_left)
pygame.mouse.set_cursor(*pygame.cursors.tri_right)
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

pygame.draw.rect(windowSurface, cookieButtonColor, cookieButton, 10)

# Set up the cookie button text
cookieButtonText = smallFont.render('Cookie', True, cookieButtonTextColor)
cookieButtonTextRect = cookieButtonText.get_rect()
cookieButtonTextRect.centerx = cookieButton.centerx
cookieButtonTextRect.centery = cookieButton.centery

# Set up the cookie counter
cookieCounter = 0
cookieCounterText = smallFont.render('Cookies: ' + str(cookieCounter), True, WHITE)
cookieCounterTextRect = cookieCounterText.get_rect()
cookieCounterTextRect.centerx = windowSurface.get_rect().centerx
cookieCounterTextRect.centery = 100

# Set up the cookie per second counter
cps = 0
cpsText = smallFont.render('CPS: ' + str(cps), True, WHITE)
cpsTextRect = cpsText.get_rect()
cpsTextRect.centerx = windowSurface.get_rect().right - 100
cpsTextRect.centery = 50

# Set up the cookie per click counter
cpc = 1
cpcText = smallFont.render('CPC: ' + str(cpc), True, WHITE)
cpcTextRect = cpcText.get_rect()
cpcTextRect.centerx = windowSurface.get_rect().left + 100
cpcTextRect.centery = 50

# Set up the cookie per click cost counter
cpcCost = 10
cpcCostText = smallFont.render('Cost: ' + str(cpcCost), True, WHITE)
cpcCostTextRect = cpcCostText.get_rect()
cpcCostTextRect.centerx = windowSurface.get_rect().left + 100
cpcCostTextRect.centery = 25

# Set up the cookie per second cost counter
cpsCost = 100
cpsCostText = smallFont.render('Cost: ' + str(cpsCost), True, WHITE)
cpsCostTextRect = cpsCostText.get_rect()
cpsCostTextRect.centerx = windowSurface.get_rect().right - 100
cpsCostTextRect.centery = 25

# Set up the cookie per second button
cpsButton = pygame.Rect(650, 100, 100, 100)
cpsButtonColor = GOLD
cpsButtonTextColor = BLACK
cpsButtonText = smallFont.render('CPS', True, cpsButtonTextColor)
cpsButtonTextRect = cpsButtonText.get_rect()
cpsButtonTextRect.centerx = cpsButton.centerx
cpsButtonTextRect.centery = cpsButton.centery

# Set up the cookie per click button
cpcButton = pygame.Rect(50, 100, 100, 100)
cpcButtonColor = GOLD
cpcButtonTextColor = BLACK
cpcButtonText = smallFont.render('CPC', True, cpcButtonTextColor)
cpcButtonTextRect = cpcButtonText.get_rect()
cpcButtonTextRect.centerx = cpcButton.centerx
cpcButtonTextRect.centery = cpcButton.centery

# Set up the main loop
while True:
    # Draw the window onto the screen
    windowSurface.fill(BLACK)
    windowSurface.blit(text, textRect)
    pygame.draw.rect(windowSurface, cookieButtonColor, cookieButton)
    windowSurface.blit(cookieButtonText, cookieButtonTextRect)
    windowSurface.blit(cookieCounterText, cookieCounterTextRect)
    windowSurface.blit(cpsText, cpsTextRect)
    windowSurface.blit(cpcText, cpcTextRect)
    windowSurface.blit(cpcCostText, cpcCostTextRect)
    windowSurface.blit(cpsCostText, cpsCostTextRect)
    pygame.draw.rect(windowSurface, cpsButtonColor, cpsButton)
    windowSurface.blit(cpsButtonText, cpsButtonTextRect)
    pygame.draw.rect(windowSurface, cpcButtonColor, cpcButton)
    windowSurface.blit(cpcButtonText, cpcButtonTextRect)

    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            if cookieButton.collidepoint(mousex, mousey):
                cookieCounter += cpc
            if cpsButton.collidepoint(mousex, mousey):
                if cookieCounter >= cpsCost:
                    cookieCounter -= cpsCost
                    cps += 1
                    cpsCost += 100
                    cpsCostText = smallFont.render('Cost: ' + str(cpsCost), True, WHITE)
                    cpsText = smallFont.render('CPS: ' + str(cps), True, WHITE)
            if cpcButton.collidepoint(mousex, mousey):
                if cookieCounter >= cpcCost:
                    cookieCounter -= cpcCost
                    cpc += 1
                    cpcCost += 10
                    cpcCostText = smallFont.render('Cost: ' + str(cpcCost), True, WHITE)
                    cpcText = smallFont.render('CPC: ' + str(cpc), True, WHITE)

    # Update the cookie counter
    cookieCounterText = smallFont.render('Cookies: ' + str(cookieCounter), True, WHITE)

    # Update the display
    pygame.display.update()
    time.sleep(0.01)



