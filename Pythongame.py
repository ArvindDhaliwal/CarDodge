# Example file showing a basic pygame "game loop"
import pygame as py
import random
import math
# pygame setup constructer/initilize
py.init()

# Background
background = py.image.load('background.png')

#create screen
screen=py.display.set_mode((800,385))

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

#enemies

rock = py.image.load('rock.png')
car= py.image.load('enemy.png')

enimies= []
X=[]
Y=[]
ac=[]
accel=0
num=10

for i in range(num):
    accel-=0.1
    # if i%2==0:
    #     enimies.append(rock)        
    # else:
    #      enimies.append(car)
    X.append(700)
    Y.append(random.randint(10,375))
    ac.append(accel)
    
def moveRock(x,y):
    screen.blit(rock, (x,y))
def movecar(x,y):
    screen.blit(car, (x,y))
def isCollision(enemyX, enemyY, userX, userY):
    distance = math.sqrt(math.pow(enemyX - userX, 2) + (math.pow(enemyY - userY, 2)))
    if distance < 27:
        return True
    else:
        return False
def show_lives(x, y):
    score = font.render("Lives : " + str(lives), True, (255, 255, 255))
    screen.blit(score, (x, y))

#text lives
lives=3
font = py.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10


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
    for i in enimies:
        print(enimies)
        X[i]+=ac[i]
        movecar(X[i],Y[i])

        # moveRock(X[i],Y[i])
        c=isCollision(X[i],Y[i],playerX,playerY)

        if c:
            lives-=1
            X[i]=-10
            Y[i]=-10

    if playerX <= 0:
        playerX = 0
    elif playerX >= 738:
        playerX = 738
    if playerY <= -10:
        playerY = -10
    elif playerY >= 345:
        playerY = 345
    


  
    player(playerX,playerY)

    show_lives(textX,testY)
    py.display.update()
  
    


