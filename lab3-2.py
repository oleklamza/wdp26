# Szachownica

from turtle import *

speed("fastest")
hideturtle()

def polygon(a, n):
    for _ in range(n):
        fd(a)
        left(360 / n)
   
def square(a, c="black", fc="white", ps=1):
    pencolor(c)
    fillcolor(fc)
    pensize(ps)
    begin_fill()
    polygon(a, 4)
    end_fill()

a = 50

def square_black():
    square(a, fc="black")
    
def square_white():
    square(a)
    

goto(-200, 200)

for row in range(8):
    # narysowanie jednego wiersza
    for col in range(8):
        if col % 2 == row % 2: # pola i wiersze naprzemiennie: czarne i białe
            square_white()
        else:
            square_black()
        fd(a)
    # przestawienie żółwia na początek kolejnego
    penup()
    backward(8 * a)
    right(90)
    fd(a)
    left(90)
    pendown()
    
    
    
    