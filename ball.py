from turtle import Turtle


class Ball(Turtle):     # Ball class inherited from Turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.x_move = 10    # set amount for the ball to move to X-axis
        self.y_move = 10    # set amount for the ball to move to y-axis
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1   # reverse the ball direction

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # increase speed once the ball bounces off the paddle

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1   # decrease the ball speed if the paddle is missed
        self.bounce_x()

