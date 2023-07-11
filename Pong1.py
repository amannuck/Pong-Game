import turtle
wn = turtle.Screen()
wn.title("Pong by Aman Nuckchady")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) #speedup game


#Paddle A
paddle_a = turtle.Turtle() #Turtle class object
paddle_a.speed(0) #speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0) #speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.1 #delta/change ==> x speed
ball.dy = -0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 PlayerB: 0",align ="center",font=("Courier",24,"normal"))

#Score
score_a = 0
score_b = 0
#FUNCTIONS
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 290:
        y += 20
    else:
        y = y
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -290:
        y -= 20
    else:
        y = y
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 290:
     y += 20
    else:
     y = y
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -290:
        y -= 20
    else:
       y = y
    paddle_b.sety(y)



    #Keyboard Binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#Main Game Loop
while True:
    wn.update() #every time loop runs it updates screen
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle & Ball Collisions
    if ball.xcor() > 340 and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1


