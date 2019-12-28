#ping pong
import turtle

wn = turtle.Screen()
wn.title('Ping Pong game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0) # 0 = to the max speed
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0) # 0 = to the max speed
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) # 0 = to the max speed
ball.shape('square')
ball.color('white')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)

# la siguente instruccion es para la velocidad de la bola
ball.dx = 0.15
ball.dy = 0.15


#Function
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

#Keyboard binding (evento que mueve los paddles)
wn.listen()
wn.onkeypress(paddleA_up, 'w')
wn.onkeypress(paddleA_down, 's')

wn.onkeypress(paddleB_up, 'p')
wn.onkeypress(paddleB_down, 'l')


#Main game loop
while True:
    wn.update()
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

