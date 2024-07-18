from turtle import *

def drawKochCurve(size, level):
    if (level == 0):
        t.forward(size)
    else:
        drawKochCurve(size/3, level-1)
        t.left(60)
        drawKochCurve(size/3, level-1)
        t.right(120)
        drawKochCurve(size/3, level-1)
        t.left(60)
        drawKochCurve(size/3, level-1)

def drawKochHex(size, level):
    drawKochCurve(size, level)
    t.right(120)
    drawKochCurve(size, level)
    t.right(120)
    drawKochCurve(size, level)
        

def drawYTree(size, angle, scale, level):
    if (level >= 0):
        t.forward(size)
        t.right(angle)
        drawYTree(size*scale, angle, scale, level-1)
        t.left(angle*2)
        drawYTree(size*scale, angle, scale, level-1)
        t.right(angle)
        t.backward(size)

# Initialize turtle on window
t = Turtle()    
t.speed(0)
t.penup()
#t.goto(-250, 150)
t.goto(0, -250)
t.pendown()

#drawKochCurve(500, 0)
#drawKochHex(500, 3)
t.left(90)
drawYTree(100, 50, 0.8, 10)
