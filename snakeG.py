import turtle
import time
import random

score = 0
high_score = 0


screen= turtle.Screen()
screen.title("Snake Game")
screen.bgpic('grassground.png')
screen.setup(width=800, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

fruit = turtle.Turtle()
fruit.speed(0)
screen.register_shape('apple.gif')
fruit.shape('apple.gif')
fruit.penup()
fruit.goto(80,0)

snake_body = []

scores = turtle.Turtle()
scores.speed(0)
scores.color("yellow")
scores.penup()
scores.hideturtle()
scores.goto(0, (screen.window_height()/2-50))
scores.write("Score: 0  High Score: 0", align="center", font="arial 24 bold")


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 21)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 21)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 21)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 21)

def game_over(high_score):
    fruit.hideturtle()
    fruit.clear()
    over=turtle.Turtle()
    over.penup()
    over.color('red')
    over.hideturtle()
    over.write('GAME OVER',align='center',font='arial 34 normal')

    time.sleep(2)

    over.clear()
    place_fruit()
    head.goto(0, 0)
    head.direction = "stop"

    # Hiding snake_body
    for i in snake_body:
        i.goto(1000, 1000)

    # Clear snake_body list
    snake_body.clear()
    score=0
    scores.clear()
    scores.write(f"Score: {score}  High Score: {high_score}", align="center", font="arial 24 bold")

def place_fruit():
    fruit.hideturtle()

    x = random.randint(-380,380)
    y = random.randint(-280,280)

    fruit.goto(x, y)

    fruit.showturtle()


# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


while True:
    screen.update()

    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 290 or head.ycor() < -290:
        game_over(high_score)
        score=0

    # snake head collision with the fruit
    if head.distance(fruit) < 20:
        place_fruit()
        col=['red','yellow','brown','grey','blue','pink','violet']
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color(random.choice(col))
        new_segment.penup()
        snake_body.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        scores.clear()
        scores.write(f"Score: {score}  High Score: {high_score}", align="center", font="arial 24 bold")

        # connecting all parts of snake body
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    # connecting head with snake body
    if len(snake_body) > 0:
        snake_body[0].goto(head.pos())

    move()

    # head collision with the body snake_body
    for i in snake_body:
        if i.distance(head) < 20:
            game_over(high_score)
            score=0

    time.sleep(.1)

screen.mainloop()
