import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()   # create screen object from Screen() class
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)    # turn off the animation

r_paddle = Paddle((350, 0))     # pass position as argument
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")   # onKey(function, key)
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()     # turn on animation
    ball.move()

screen.exitonclick()
