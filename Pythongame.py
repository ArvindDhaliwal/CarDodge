import pygame as py
from pygame import mixer
import random
import math
# pygame setup constructer/initilize
py.init()
# Background
background = py.image.load('background.png')

# create screen
screen = py.display.set_mode((800, 385))

py.display.set_caption("Racing")
icon = py.image.load('car.png')


# Player
playerImg = py.image.load('user.png')

playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

# enemies


rock = py.image.load('rock.png')
car = py.image.load('enemy.png')

enimies = []
X = []
Y = []
ac = []
accel = 0
num = 7
score=0
for i in range(num):
    accel -= 0.2
    # if i%2==0:
    #     enimies.append(rock)
    # else:
    #      enimies.append(car)
    X.append(700)
    Y.append(random.randint(10, 375))
    ac.append(accel)


def moveRock(x, y):
    screen.blit(rock, (x, y))


def movecar(x, y):
    screen.blit(car, (x, y))


def isCollision(enemyX, enemyY, userX, userY):
    distance = math.sqrt(math.pow(enemyX - userX, 2) +
                         (math.pow(enemyY - userY, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_lives(x, y):
    sc = font.render("Lives : " + str(lives) +" Score: "+str(score), True, (255, 255, 255))
    screen.blit(sc, (x, y))


def game_over_text():

    over_text = over_font.render("GAME OVER ", True, (255, 255, 255))
    screen.blit(over_text, (192, 250))
    over_text = over_font.render("Score:"+str(score), True, (255, 255, 255))
    screen.blit(over_text, (192, 100))



# text lives
lives = 3
font = py.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
over_font = py.font.Font('freesansbold.ttf', 64)

py.display.set_icon(icon)
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in py.event.get():

        if event.type == py.QUIT:
            running = False

        # if keystroke is pressed check if right or left
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                playerX_change = -1.2
            if event.key == py.K_RIGHT:
                playerX_change = 1.2
            if event.key == py.K_UP:
                playerY_change = -1.2
            if event.key == py.K_DOWN:
                playerY_change = 1.2

        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                playerX_change = 0
            if event.key == py.K_UP or event.key == py.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    k = 0

    for k in range(num):
        if lives <= 0:
            game_over_text()
            break
        ac[k] -= 0.001
        X[k] += ac[k]

        # if(k%2==0):
        #     movecar(X[k],Y[k])
        # else:
        #     moveRock(X[i],Y[i])
        c = isCollision(X[k], Y[k], playerX, playerY)

        if c:
            lives -= 1
            if lives==0:
                sound1 = mixer.Sound("end.mp3")
                sound1.play()
            sound = mixer.Sound("CarCrash.mp3")
            sound.play()
            X[k] = 800
            Y[k] = random.randint(10, 375)
        movecar(X[k], Y[k])
        if X[k] < -10:
            X[k] = 800
            Y[k] = random.randint(10, 375)
            score+=1

    if playerX <= 0:
        playerX = 0
    elif playerX >= 738:
        playerX = 738
    if playerY <= -10:
        playerY = -10
    elif playerY >= 345:
        playerY = 345

    player(playerX, playerY)

    show_lives(textX, textY)
    py.display.update()