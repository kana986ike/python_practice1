import turtle
import math
import random


class Kame(turtle.Turtle):
    def __init__(self):
        super(Kame,self).__init__()
        self.shape('turtle')
        self.shapesize(2,2)

    def hit_wall(self):
        xx = self.getscreen().window_width() / 2.0
        yy = self.getscreen().window_width() / 2.0

class Line:
    def __init__(self,slp,x0,y0):
        self.slp = float(slp)
        self.x0 = float(x0)
        self.y0 = float(y0)

    def get_y(self,x):
        return self.slp * (x - self.x0) + self.y0

    def get_x(self,y):
        return self.x0 + (y - self.y0) / self.slp


    line = Line(math.tan(self.heading()),self.xcor(),self.ycor())
    rand_angle = matn.pi * random.random()

    if self.towards(-xx,yy)>self.heading() >= self.towards
