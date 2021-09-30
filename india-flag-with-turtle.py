import turtle
t = turtle.Turtle()

def rectangle(color, length, bredth, angle, solid=True):
    t.color(color)
    if solid:
        t.fillcolor(color)
        t.begin_fill()
        
    for _ in range(2):
        t.forward(length)
        t.right(angle)
        t.forward(bredth)
        t.right(angle)
    if solid:
        t.end_fill()


def ashokchakra_spokes(color, radius, number=24):
    for _ in range(number):
        t.right(360/number)
        t.forward(50)
        t.backward(50)
    

t.pensize(3)
t.penup()

t.goto(-150,200)
t.pendown()
rectangle("orange", 300, 100, 90)
t.penup()


t.goto(-150,100)
t.pendown()
rectangle("blue", 300, 100, 90, solid=False)
t.penup()

t.goto(0,50)
t.pendown()
ashokchakra_spokes("blue",50)
t.goto(0,0)
t.circle(50)
t.penup()

    
t.goto(-150,0)
t.pendown()
rectangle("green", 300, 100, 90)
t.penup()

