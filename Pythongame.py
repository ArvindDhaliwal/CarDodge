# Example file showing a basic pygame "game loop"
import pygame as py
import random
import math
# pygame setup constructer/initilize
py.init()

# Background
background = py.image.load('backround.png')

#create screen
screen=py.display.set_mode((800,385))

py.display.set_caption("2 Player Racing")
icon = py.image.load('car.png')



# Player
playerImg = py.image.load('user.png')

playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

#enemies 
rock = py.image.load('rock.png')
rockX = 700
rockY = random.randint(10,375)
rockX_change=-1
def moveRock(x):
    screen.blit(rock, (x,rockY))

car= py.image.load('enemy.png')
carX = 700
carY = random.randint(10,375)
carX_change=-1
def movecar(x):
    screen.blit(car, (x,carY))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
#how to change colour
# screen.fill((255,0,0))
# py.display.update()

py.display.set_icon(icon)
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))


    for event in py.event.get():
        if event.type== py.QUIT:
            running=False

        #if keystroke is pressed check if right or left
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                playerX_change=-1
            if event.key == py.K_RIGHT:
                playerX_change=1
            if event.key == py.K_UP:
                playerY_change= -1
            if event.key == py.K_DOWN:
                playerY_change= 1
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                playerX_change=0
            if  event.key == py.K_UP or event.key == py.K_DOWN:
                playerY_change=0
    playerX+=playerX_change
    playerY+=playerY_change
    rockX+=rockX_change
    carX+=carX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 738:
        playerX = 738
    if playerY <= -10:
        playerY = -10
    elif playerY >= 345:
        playerY = 345
    player(playerX,playerY)
    moveRock(rockX)
    movecar(carX)
    py.display.update()
    


