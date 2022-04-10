import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('Green')


screen.tracer(0)            

t = turtle.Turtle()
t.speed(0)
t.width(3)


t.hideturtle()            

def draw_square() :
    t.fillcolor("Orange")
    t.begin_fill()
    for side in range(4) :
        t.forward(100)
        t.left(90)
    t.end_fill()
t.penup()
t.goto(-350, 0)
t.pendown()

while True :
    t.clear()
    draw_square()
    
   
    screen.update()         
    t.forward(0.02)