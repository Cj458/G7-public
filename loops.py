import turtle as t
import random


"""
1. Counting loop: Is a type of loop that help you repeat a piece
of code a certain number of time.
keyword for counting is 'for'
"""

# for  x in range(1000000):
#     print('HELLO WORLD')

# for -> keyword
# x -> counting variable

turtle = t.Turtle()
turtle.speed(10)
turtle.shape('turtle')



# first circle
for x in range(36):
    turtle.forward(18)
    turtle.right(10)


# second circle
for x in range(36):
    turtle.forward(14)
    turtle.left(10)


#third circle
turtle.penup()
turtle.goto(0, 160)
turtle.pendown()

for x in range(36):
    turtle.forward(10)
    turtle.left(10)


#eyes
turtle.penup()
turtle.goto(-30, 205)
turtle.pendown()
for x in range(36):
    turtle.forward(3)
    turtle.left(10)


turtle.penup()
turtle.goto(30, 205)
turtle.pendown()
for x in range(36):
    turtle.forward(3)
    turtle.left(10)

# mouth
turtle.penup()
turtle.goto(-10, 170)
turtle.pendown()
for x in range(18):
    turtle.forward(2)
    turtle.left(2)

# nose
turtle.penup()
turtle.goto(0, 203)
turtle.pendown()
turtle.right(90)
turtle.forward(10)
turtle.right(60)
turtle.forward(8)

# arms


turtle.hideturtle()

t.exitonclick()





"""
2. conditional loop or a while is a type of loop that runs as long as the condition is True

keyword: while
"""



number = random.randint(0, 100)

guess = int(input(" I'm thinking of a number from 0 to 100. What is it?  "))


while guess != number:
    pass




# exercise 2 -> a passwoord generator

adjectives = ['boring', 'exciting', 'red', 'wet', 'big', 'interesting','exhausting', 'fast', 'dry', 'thin', 'tremendous', 'luxurious']
nouns = ['cat', 'jenitor', 'teacher', 'gamer', 'bear', 'doggo', 'glasses']
uppers = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowers = list('abcdefghijklmnoprstuvwxyz')
characters = list(""""!@#$%^&*(_)+=][}{;:.<>?'""")

print('Welcome to password generator! We will help create a secure and strong password.')



while True:
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    upper = random.choice(uppers)
    lower = random.choice(lowers)
    char = random.choice(characters)
    number = random.randrange(0, 100)

    pwd = adj + noun + upper + lower + char + str(number)

    print(f"your password is: {pwd}")

    break
