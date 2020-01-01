import turtle
import levels
import random
import os


##Statics
wrongPainted = 0
correctPainted = 0
score = 0
levelcount = 0
painterSound = "aplay sounds/painter.wav&"
clearSound = "aplay sounds/clear.wav&"
booSound = "aplay sounds/boo.wav&"
cheerSound = "aplay sounds/cheer.wav&"
restartSound = "aplay sounds/restart.wav&"

##Game Size and Squares
witdh = 600
height = 600
n = levels.randomLevelSquareCount(levelcount)
##Screen Size
screenWitdh = 1000
screenHeight = 600

##Level Correction
correction = levels.randomLevelCorrection(levelcount)

##Screen size, background and background
screen = turtle.getscreen()
screen.bgcolor("black")
screen.title("Paint it up!")
screen.setup(screenWitdh,screenHeight)

##Level turtle setting
level=turtle.Turtle()
level.pencolor("white")
level.speed(1000)
level.pensize(1)
level.up()
level.hideturtle()


##Menu turtle setting
menu = turtle.Turtle()
menu.pencolor("grey")
menu.speed(1000)
menu.pensize(1)
menu.up()
menu.hideturtle()

##Level info
image = turtle.Turtle()
info = turtle.Screen()

##Scoreboard turtle setting
scoreboard = turtle.Turtle()
scoreboard.pencolor("white")
scoreboard.speed(1000)
scoreboard.pensize(1)
scoreboard.up()
scoreboard.hideturtle()

##Painter turtle setting
painter=turtle.Turtle()
painter.pencolor("white")
painter.speed(1000)
painter.pensize(1)
painter.up()
painter.hideturtle()
painted = []
for i in range(n*n):
    painted.append(0)

def randomLevel():
    global levelcount
    levelcount = random.randint(0,levels.randCounter()-1)

def levelImage():
    photo = levels.randomLevelImage(levelcount)
    info.addshape(photo)
    image.goto(300,110)
    image.shape(photo)

def paintBlock(x,y,square):
    os.system(painterSound)
    painter.setheading(90)
    painter.goto(x,y)
    if(painted[square] == 1):
        painter.fillcolor('black')
        painted[square] = 0
    else:
        painter.fillcolor('white')
        painted[square] = 1
    painter.begin_fill()
    for i in range(4):
        painter.forward((witdh//n)-1)
        painter.left(90)
    painter.end_fill()
def drawButtonWithTitle(x,y,title):
    menu.down()
    for i in range(4):
        if(i%2==0):
            menu.forward(250)
            menu.right(90)
        else:
            menu.forward(40)
            menu.right(90)
    menu.up()
    menu.forward(x)
    menu.right(90)
    menu.forward(y)
    menu.left(90)
    menu.write(title,font=("Ariel", 14, "normal"))
        
def drawButton():
    for i in range(4):
        menu.down()
        if(i%2==0):
            menu.forward(250)
            menu.right(90)
        else:
            menu.forward(40)
            menu.right(90)
        menu.up()


def inGameMenu():
    menu.goto(170,-100)
    drawButtonWithTitle(100,30,"Check")
    menu.goto(170,-150)
    drawButtonWithTitle(100,30,"Clear")
    menu.goto(170,-200)
    drawButtonWithTitle(100,30,"Restart")
    
    

def drawLevel():
    
    level.pencolor("grey")
    x=-screenWitdh//2
    y=-screenHeight//2
    k=float(witdh//n)
    for i in range(n+1):
        level.setheading(0)
        level.goto(x,y+(k*i))
        level.down()
        level.forward(witdh)
        level.up()
    level.goto(0,0)
    for i in range(n+1):
        level.setheading(90)
        level.goto(x+(k*i),y)
        level.down()
        level.forward(height)
        level.up()
    levelImage()
    inGameMenu()
    scoreBoard()
    
def paintedCounter():
    paintedcount = 0
    for i in range(n*n):
        if (painted[i] == 1):
            paintedcount +=1
    return paintedcount
def clearLevel():
    painter.clear()
    for i in range(n*n):
        painted[i] = 0
def restartGame():
    global score
    global n
    global painted
    global correction
    clearLevel()
    score = 0
    print(score)
    
    level.clear()
    menu.clear()
    scoreboard.clear()
    randomLevel()
    n = levels.randomLevelSquareCount(levelcount)
    correction = levels.randomLevelCorrection(levelcount)
    painted = []
    for i in range(n*n):
        painted.append(0)
    drawLevel()

def levelCheck():
    global correctPainted
    global wrongPainted
    global score
    global n
    global painted
    global correction
    
    if (paintedCounter() !=0):
        os.system(cheerSound)
        for i in range(n*n):
            if (painted[i] == correction[i]):
                correctPainted += 1
            else:
                wrongPainted += 1
        score += (correctPainted*10)-(wrongPainted*10)
        print(wrongPainted)
        print(correctPainted)
    else:
        os.system(booSound)
        score -= (n*n)*10
    print(score,"/",n*n*10)
    wrongPainted = 0
    correctPainted = 0
    clearLevel()
    
    level.clear()
    menu.clear()
    scoreboard.clear()
    randomLevel()
    n = levels.randomLevelSquareCount(levelcount)
    correction = levels.randomLevelCorrection(levelcount)
    painted = []
    for i in range(n*n):
        painted.append(0)
    drawLevel()
    
def scoreBoard():
    global score
    scoreboard.setposition(250,-280)
    scoreboard.down()
    scoreboard.write("Score: {}".format(score),font=("Ariel", 14, "normal"))
    scoreboard.up()
    
def clicked(x,y):
    a = x+(screenWitdh//2)
    b = y+(screenHeight//2)
    
    column =  a // (witdh//n)
    row = b // (height//n)
    square = int(column + row*n)
    
    
    paint_x = ((column+1)*(witdh//n))-(screenWitdh//2)
    paint_y  = ((row)*(height//n))-(screenHeight//2) 
    if(a<witdh and a>0 and b<height and b>0):
        paintBlock(paint_x,paint_y,square)
    elif(a>671 and a<923):
        if(b>157 and b<197):
            ##Check Button
            levelCheck()
        elif(b>107 and b<147):
            ##Clear Button
            os.system(clearSound)
            clearLevel()
        elif(b>57 and b<97):
            ##Restart Button
            os.system(restartSound)
            restartGame()
drawLevel()
screen.onscreenclick(clicked)
