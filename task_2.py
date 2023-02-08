from turtle import speed, exitonclick, forward, left, penup, pendown

from random import randint

speed("fastest")
inflation_rate = 20


def column(inflation_rate):
    for _ in range(2):
        forward(10)
        left(90)
        forward(inflation_rate)
        left(90)
    penup()
    forward(20)
    pendown()


for _ in range(20):
    inflation_rate += randint(-10, 40)
    column(inflation_rate)

exitonclick()
