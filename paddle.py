from turtle import Turtle


class Paddle(Turtle):   # Paddle class inherited from Turtle class
    def __init__(self, position):   # position as a parameter
        super().__init__()
        # self represents the object that has been created from the class
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)