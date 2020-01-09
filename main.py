import turtle
import system

screenWitdh = 1000
screenHeight = 600
gameTitle = "Pixel It!"

##Screen size, background and background
screen = turtle.getscreen()
screen.bgcolor("black")
screen.title("Pixel it!")
screen.setup(screenWitdh,screenHeight)

menudrawer = turtle.Turtle()
menudrawer.hideturtle()
menudrawer.color("grey")
menudrawer.speed(1000)
menudrawer.up()
menudrawer.setposition(-150,0)


menutitle = turtle.Turtle()
menutitle.hideturtle()
menutitle.color("grey")
menutitle.speed(1000)
menutitle.up()
menutitle.setposition(10,-50)


title = turtle.Turtle()
title.hideturtle()
title.color("white")
title.speed(1000)
title.up()
title.setposition(0,100)
title.write(gameTitle, align="center", font=("Ariel",50,"italic"))


def drawMenu():
    for j in range(2):
        menudrawer.down()
        for i in range(4):
            if(i%2==0):
                menudrawer.forward(300)
            else:
                menudrawer.forward(75)    
            menudrawer.right(90)
        menudrawer.up()
        menudrawer.setposition(-150,menudrawer.ycor()-100)
    menutitle.write("Play Game", align="center", font=("Ariel",20,"normal"))
    menutitle.setposition(10,-150)
    menutitle.write("Exit", align="center", font=("Ariel",20,"normal"))


def startgame():
    menutitle.clear()
    menudrawer.clear()
    title.clear()
    import game

def clicked(x,y):
    if(x<150 and x>-150):
        if(y<0 and y>-75):
            system.sound("sounds/restart.wav")
            startgame()
        elif(y<-100 and y>-175):
            turtle.bye()
            system.sound("sounds/clear.wav")

    
drawMenu()
screen.onscreenclick(clicked)
turtle.mainloop()
