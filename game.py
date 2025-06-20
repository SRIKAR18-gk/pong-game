import time
from turtle import Turtle, Screen
import random
screen = Screen()
screen.bgcolor("black")
we = Turtle()
we.color("white")
we.hideturtle()
we.write("Pong Game", align="center", font=("Arial", 40, "bold"))
time.sleep(2)

we.clear()
we.write("Press Space To Start", align="center", font=("Arial", 40, "bold"))
time.sleep(2)
we.clear()
we.write("For left user the controls are W  and S", align="center", font=("Arial", 28, "bold"))
we.penup()
we.setheading(270)
we.forward(150)
we.write("For right user the controls are I  and K", align="center", font=("Arial", 28, "bold"))
time.sleep(2)
we.clear()
screen.tracer(0)
scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.color("white")
scoreboard.goto(0, 300)
scoreboard.write(" 0       0", align="center", font=("Arial", 24, "bold"))

def update_score():
    scoreboard.clear()
    scoreboard.write(f" {score1}     {score2}", align="center", font=("Arial", 24, "bold"))

for i in range(-500,501,25):
    toy = Turtle()
    toy.penup()
    toy.color("white")
    toy.goto(0, i)
    toy.shapesize(0.3)
    toy.shape("square")
screen.update()
screen.setup(800, 800)
pos = [(380, 40), (380, 20), (380, 0), (380, -20)]
p = [(-380, 40), (-380, 20), (-380, 0), (-380, -20)]
point1 = 0
point2 = 0

tim1 = []
tim2 = []
game = True
for i in pos:
    toy = Turtle("square")
    toy.penup()
    toy.goto(i)
    toy.color("white")
    tim1.append(toy)
screen.update()
for i in p:
    toy = Turtle("square")
    toy.penup()
    toy.goto(i)
    toy.color("white")
    tim2.append(toy)
screen.update()

move_ball = False
moveup = True
movedown = True
moveup1 = True
movedown1 = True
num = 10
angle = []
for i in range(135, 225):
    angle.append(i)
for i in range(10, 45):
    angle.append(i)
for i in range(315, 350):
    angle.append(i)
angle.remove(180)
ba = Turtle("circle")
ba.speed(num)
ba.penup()
ba.shapesize(0.8)
score1 = 0
score2 = 0
an = random.choice(angle)
ba.color("white")
ba.setheading(an)

def reset_ball():
    ba.hideturtle()
    ba.goto(0, 0)
    ba.showturtle()
    ba.setheading(random.choice(angle))
    screen.update()
def pad():

    for i in range(0,len(tim1)):
        tim1[i].goto(pos[i])

    for i in range(0,len(tim2)):
        tim2[i].goto(p[i])

def ball():
    global move_ball, num, score1, score2, an, point1, point2, game
    if move_ball:

        hit = False
        screen.update()
        time.sleep(0.1)
        ba.speed(num)
        an = ba.heading()
        for i in tim1:
            if i.distance(ba) < 25:
                if ba.heading() > 0 and ba.heading() < 90:
                    an = 180 - an
                    ba.setheading(an)
                if ba.heading() > 270 and ba.heading() < 360:
                    an -= 270
                    an = 270 - an
                    ba.setheading(an)
                ba.forward(30)
                num += 2
                point1 += 1
                hit = True
                break

        for i in tim2:
            if i.distance(ba) < 25:
                if ba.heading() > 90 and ba.heading() < 180:
                    an = 180 - an
                    ba.setheading(an)
                if ba.heading() < 270 and ba.heading() > 180:
                    an = 270 - an
                    an += 270
                    ba.setheading(an)
                ba.forward(30)
                num += 2
                point2 += 1
                hit = True
                break
        if not hit:
            ba.forward(20)

        if ba.ycor() > 375:
            a = ba.heading()
            a -= 90
            a = 270 - a
            ba.setheading(a)
        elif ba.ycor() < -375:
            a = ba.heading()
            a = 270 - a
            a += 90
            ba.setheading(a)

        if ba.xcor() < -380:
            score2 += 1
            update_score()
            move_ball = False
            pad()
            reset_ball()
            return

        elif ba.xcor() > 380:
            score1 += 1
            update_score()
            move_ball = False
            pad()
            reset_ball()
            return

    if game:
        screen.ontimer(ball, 40)
    else:
        return

def start():
    global move_ball
    if not move_ball:
        move_ball = True
        ball()

def boom():
    if score1 >= 3 and score1 <= 5 or score2 >= 3:
        ba.forward(200)

def forward():
    global moveup, movedown
    screen.update()
    if moveup:
        for i in tim1:
            i.setheading(90)
            i.forward(20)
            i.speed(2)
    if tim1[0].ycor() > 370:
        moveup = False
        movedown = True
    else:
        moveup = True

def down():
    global movedown, moveup
    screen.update()
    if movedown:
        for i in tim1:
            i.setheading(270)
            i.forward(20)
            i.speed(2)
    if tim1[3].ycor() < -370:
        movedown = False
        moveup = True
    else:
        movedown = True

def front():
    global moveup1, movedown1
    screen.update()
    if moveup1:
        for i in tim2:
            i.setheading(90)
            i.forward(20)
            i.speed(2)
    if tim2[0].ycor() > 370:
        moveup1 = False
        movedown1 = True
    else:
        moveup1 = True

def downward():
    global movedown1, moveup1
    screen.update()
    if movedown1:
        for i in tim2:
            i.setheading(270)
            i.forward(20)
            i.speed(2)
    if tim2[3].ycor() < -380:
        movedown1 = False
        moveup1 = True
    else:
        movedown1 = True

screen.listen()
screen.onkey(key="i", fun=forward)
screen.onkey(key="k", fun=down)
screen.onkey(key="w", fun=front)
screen.onkey(key="s", fun=downward)
screen.onkey(key="space", fun=start)
screen.onkey(key="b", fun=boom)
screen.exitonclick()
