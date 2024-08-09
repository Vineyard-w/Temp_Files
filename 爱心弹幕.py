from math import sqrt
from turtle import *
from random import randint
from random import random

# 心心代码
width, height = 800, 600
screen = Screen()  # 创建窗口对象
screen.setup(width, height)  # 设置窗口的宽高
screen.delay(0)  # 设置无延时绘画
screen.bgcolor('pink')  # 设置背景颜色为粉色


class Heart:
    def __init__(self, x, y, size):
        self.size = size
        self.speed = size
        t = Turtle(visible=False, shape='circle')
        t.shapesize(size, size)
        color = (1, 1 - size / 4, 1 - size / 4)
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        self.circle1 = t.clone()
        self.circle1.goto(x - sqrt(size * size * 160) / 2, y)
        self.circle2 = t.clone()
        self.circle2.goto(x + sqrt(size * size * 160) / 2, y)
        self.square = t.clone()
        self.square.shape("square")
        self.square.setheading(45)
        self.square.goto(x, y - sqrt(size * size * 160) / 2)
        self.circle1.showturtle()
        self.circle2.showturtle()
        self.square.showturtle()

    def move(self):
        self.circle1.setx(self.circle1.xcor() - self.speed)
        self.square.setx(self.square.xcor() - self.speed)
        self.circle2.setx(self.circle2.xcor() - self.speed)

    def moveTo(self, x, y):
        self.circle1.hideturtle()
        self.circle2.hideturtle()
        self.square.hideturtle()
        self.circle1.goto(x - sqrt(self.size * self.size * 160) / 2, y)
        self.circle2.goto(x + sqrt(self.size * self.size * 160) / 2, y)
        self.square.goto(x, y - sqrt(self.size * self.size * 160) / 2)
        self.circle1.showturtle()
        self.circle2.showturtle()
        self.square.showturtle()


loves = []
for i in range(50):
    love = Heart(width / 2 + randint(1, width), randint(-height / 2, height / 2), random() * 3)
    loves.append(love)

# while True:
#     for love in loves:
#         love.move()


while True:
    for love in loves:
        love.move()
        if love.square.xcor() < -width / 2:
            love.moveTo(width / 2 + randint(1, width), randint(-height / 2, height / 2))