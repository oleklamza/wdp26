# Wielokąty i funkcje

from turtle import *

speed("fast")

# definicja funkcji rysującej dowolny wielokąt foremny
def polygon(a, n):
    for _ in range(n):
        fd(a)
        left(360 / n)
   
# funkcja rysująca kwadrat 
def square(a, c="black", fc="white", ps=1):
    pencolor(c)
    fillcolor(fc)
    pensize(ps)
    begin_fill()
    polygon(a, 4)  # wywołwanie funkcji rysującej wielokąt
    end_fill()

# test funkcji rysującej kwadrat
square(100, ps=6, fc="red")
penup()
goto(-300, -200)
pendown()
square(50, "green", ps=3)

# test funkcji rysującej wielokąt
penup()
goto(300, 0)
pendown()
polygon(70, 7)