from turtle import *
from random import randint


speed(0)
penup()
goto(-140, 140)


for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)


jim = Turtle()
jim.color('red')
jim.shape('turtle')

jim.penup()
jim.goto(-160, 100)
jim.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

james = Turtle()
james.color('yellow')
james.shape('turtle')

james.penup()
james.goto(-160, 40)
james.pendown()

masha = Turtle()
masha.color('green')
masha.shape('turtle')

masha.penup()
masha.goto(-160, 10)
masha.pendown()

for turn in range(100):
    jim.forward(randint(1, 5))


exitonclick()