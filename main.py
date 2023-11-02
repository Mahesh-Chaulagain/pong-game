import turtle
from turtle import Screen
from paddle import Paddle

screen = Screen()   # create screen object from Screen() class
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)    # turn off the animation

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")   # onKey(function, key)
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
