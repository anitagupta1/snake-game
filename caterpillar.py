import  turtle
import random as rd


s=turtle.Screen()
s.setup(800,600)
s.title('caterpillar game')
s.bgcolor('yellow')

cat=turtle.Turtle()
cat.shape('circle')
cat.color('black')
cat.speed(0)
cat.hideturtle()

leaf=turtle.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
# registering leaf shape
s.register_shape('itsleaf',leaf_shape)
leaf.shape('itsleaf')
leaf.color("green")
leaf.penup()
leaf.speed(0)
leaf.goto(0,100)
leaf.hideturtle()

text_turtle=turtle.Turtle()
text_turtle.write('PRESS W TO START',align='center',font='arial 17 bold')
text_turtle.color('red')
text_turtle.speed(0)
text_turtle.hideturtle()

score_turtle=turtle.Turtle()
score_turtle.speed(0)
score_turtle.hideturtle()

# setting boundary limits
def outside_wall():
    left_wall=-s.window_width()/2
    right_wall=s.window_width()/2
    top_wall=s.window_height()/2
    bottom_wall=-s.window_height()/2
    (x,y)=cat.pos()
    outside=right_wall<x or x<left_wall or  top_wall<y or y<bottom_wall
    return  outside

def place_leaf():
     leaf.hideturtle()
     leaf.setx(rd.randint(-300,300))
     leaf.sety(rd.randint(-200,200))
     leaf.showturtle()

def game_over():
     cat.hideturtle()
     leaf.hideturtle()
     t=turtle.Turtle()
     t.penup()
     t.hideturtle()
     t.color('red')
     t.write("GAME OVER",align='center',font='arial 40 bold')

def display_score(score):
    score_turtle.clear()
    score_turtle.penup()
    x=(s.window_width()/2)-50
    y=(s.window_height()/2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(f'Score:{score}',align='right',font='arial 40 italic')


def move_up():
    if cat.heading()==0 or cat.heading()==180:
        cat.setheading(90)
def move_down():
    if cat.heading()==0 or cat.heading()==180:
        cat.setheading(270)
def move_left():
    if cat.heading()==90 or cat.heading()==270:
        cat.setheading(180)
def move_right():
    if cat.heading()==90 or cat.heading()==270:
        cat.setheading(0)

def start_game():
        score=0
        text_turtle.clear()
        cat_speed=2
        cat_length=2

        cat.shapesize(1,cat_length,1)
        cat.showturtle()
        display_score(score)
        place_leaf()
        cat.penup()
        while True:
            cat.forward(cat_speed)
            if cat.distance(leaf)<20:
                place_leaf()
                cat_length+=1
                # increasing caterpillar body size
                cat.shapesize(1,cat_length,1)

                cat_speed+=0.5
                score+=10
                display_score(score)
            if outside_wall():
                game_over()
                break

# keyboard bindings
s.listen()
s.onkey(start_game,'w')
s.onkey(move_up,'Up')
s.onkey(move_down,'Down')
s.onkey(move_left,'Left')
s.onkey(move_right,'Right')


s.mainloop()
