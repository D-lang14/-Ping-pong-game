import turtle as t

player = 0

win = t.Screen()
win.title('Pong Game')
win.bgcolor('black')
win.setup(width=900, height=700)
win.tracer(0)

# Creating a paddle
paddle = t.Turtle()
paddle.speed(6)
paddle.shape('square')
paddle.color('lightgreen')
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0,-300)

# Creating Ball
ball = t.Turtle()
ball.speed(6)
ball.shape('circle')
ball.color('skyblue')
ball.penup()
ball.goto(0,-330)
balldx = 0.2
balldy = 0.2

# Score board
pen = t.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('score', align='center', font=('Arial', 24, 'normal'))

# Moving paddle
def paddleRight():
    pad = paddle.xcor()
    pad += 20
    paddle.setx(pad)

def paddleLeft():
    pad = paddle.xcor()
    pad -= 20
    paddle.setx(pad)

# Assign keys
win.listen()
win.onkeypress(paddleRight,'Right')
win.onkeypress(paddleLeft,'Left')

# Game Loop
while True:
    win.update()

    # Moving ball
    ball.setx(ball.xcor()+balldx)
    ball.sety(ball.ycor()+balldy)

    # Setting Borders
    if ball.ycor()>390:
        ball.sety(390)
        balldy *= -1

    if ball.xcor()>450:
        ball.setx(450)
        balldx *= -1

    if ball.xcor()<-450:
        ball.setx(-450)
        balldx *= -1

    if ball.ycor()<-390:
        ball.goto(0,0)
        balldy *= -1
        player += 1
        pen.clear()
        pen.write('Player:{}'.format(player),align='center', font=('Arial',24,'normal'))

    # Handling collisions
    if (ball.ycor()<-280) and (ball.ycor()>-290) and (ball.xcor() > paddle.xcor()-40 and ball.xcor() < paddle.xcor()+40):
        ball.sety(-280)
        balldy *= -1

