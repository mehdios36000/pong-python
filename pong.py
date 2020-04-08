#simple pong game by Alami idrissi mehdi



import turtle
from playsound import playsound




window=turtle.Screen()
window.title("pong game is fun")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)
#score
score_1=0
score_2=0
#paddle 1
paddle_1=turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)
#paddle 2
paddle_2=turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

#ball 
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.08
ball.dy=0.08


#score panel
panel=turtle.Turtle()
panel.speed()
panel.color("white")
panel.penup()
panel.hideturtle()
panel.goto(0,260)
panel.write("player 1: 0  player 2: 0",align="center",font=("Courier",24,"normal"))


#function for moving the paddle
def paddle_1_up():
    y=paddle_1.ycor()
    y+=20
    paddle_1.sety(y)

def paddle_1_down():
    y=paddle_1.ycor()
    y-=20
    paddle_1.sety(y)


def paddle_2_up():
    y=paddle_2.ycor()
    y+=20
    paddle_2.sety(y)

def paddle_2_down():
    y=paddle_2.ycor()
    y-=20
    paddle_2.sety(y)




#keyboard listening
window.listen()
window.onkeypress(paddle_1_up,"w")
window.onkeypress(paddle_1_down,"s")
window.onkeypress(paddle_2_up,"Up")
window.onkeypress(paddle_2_down,"Down")






#main game loop
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_1+=1
        panel.clear()
        panel.write("player 1: {}  player 2: {} ".format(score_1,score_2),align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_2+=1
        panel.clear()
        panel.write("player 1: {}  player 2: {} ".format(score_1,score_2),align="center",font=("Courier",24,"normal"))

    if paddle_1.ycor()<-200:
        paddle_1.sety(-200) 
    if paddle_1.ycor()>200:
        paddle_1.sety(200)
    if paddle_2.ycor()<-200:
        paddle_2.sety(-200) 
    if paddle_2.ycor()>200:
        paddle_2.sety(200)
    #paddle and ball collisions
    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_2.ycor()+40 and ball.ycor()>paddle_2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_1.ycor()+40 and ball.ycor()>paddle_1.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1

        
    
        
