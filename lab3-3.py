# Zabawy w generowanie grafiki

from turtle import *

speed("fastest")
hideturtle()

def wachlarz():
    colors = ["#FF1C2D", "#FF6213", "#FE9704", "#A3B02D", "#005B42"]
    k = 180 // 5
    pensize(2)
    for i in range(180):
        pencolor(colors[i // k])
        fd(300)
        left(0.1)
        bk(300)
        left(1)

wachlarz()


def serwetka():
    begin_fill()
    for i in range(18):
        fd(300)
        left(100)
    end_fill()

#serwetka()
