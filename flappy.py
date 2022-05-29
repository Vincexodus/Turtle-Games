import random
import turtle

screen = turtle.Screen()
screen.title("Flappy Bird")
screen.bgcolor("lightblue")
screen.setup(width=500, height=700)

# player
bird = turtle.Turtle()
bird.speed(0)
bird.shape("turtle")
bird.color("red", "yellow")
bird.shapesize(2)
bird.penup()
bird.goto(-50, 0)

# platform
ground = turtle.Turtle()
ground.speed(0)
ground.shape("square")
ground.color("green", "yellow")
ground.shapesize(4, 30)
ground.penup()
ground.goto(0, -300)

# scoreboard
score = turtle.Turtle()
score.hideturtle()
score.speed(0)
score.color("black")
score.penup()
score.goto(0, -300)
score.write("Score : 0", align="center", font=("Courier", 14, "bold"))

# list to store all pipe turtle
total_pipe = []

# create pipe with x y coordinates
def spawn(x, y):
  low_pipe = turtle.Turtle()
  low_pipe.hideturtle()
  low_pipe.speed(0)
  low_pipe.shape("square")
  low_pipe.color("black", "green")
  low_pipe.shapesize(12 + y/10, 4) # stretch by 10 pixels
  low_pipe.penup()
  low_pipe.goto(x, y - 140)
  low_pipe.showturtle()

  high_pipe = turtle.Turtle()
  high_pipe.hideturtle()
  high_pipe.speed(0)
  high_pipe.shape("square")
  high_pipe.color("black", "green")
  high_pipe.shapesize(12 - y/10, 4)
  high_pipe.penup()
  high_pipe.goto(x, y + 240)
  high_pipe.showturtle()

  total_pipe.append(low_pipe)
  total_pipe.append(high_pipe)

# move pipe back to the front
def reposition(low_pipe, high_pipe, x, y):
  low_pipe.shapesize(12 + y/10, 4)
  low_pipe.goto(x, y - 140)
  high_pipe.shapesize(12 - y/10, 4)
  high_pipe.goto(x, y + 240)

# flap
def jump():
  bird.sety(bird.ycor() + 100)

# Keyboard bindings
screen.listen()
screen.onkeypress(jump, "space")

min_height, max_height = -80, 80
# initial 3 pipes spawn
for i in [200, 500, 800]:
  spawn(i, random.randint(min_height, max_height))

point = 0
playing = True

while playing:
  # player too low/high
  if(bird.ycor() < -220 or bird.ycor() > 350):
    playing = False
  for i in range(len(total_pipe)):
    # pipe comes within bird range
    if(total_pipe[i].xcor() < -10 and total_pipe[i].xcor() > -90):
      # lower pipe
      if i%2 == 0:
        # bottom of bird lower than upper level of lower pipe & head of bird more than pipe width
        if(bird.ycor() - 20 < total_pipe[i].ycor() + total_pipe[i].shapesize()[0]*10) and (bird.xcor() + 30 > total_pipe[i].xcor() - total_pipe[i].shapesize()[1]*10):
          playing = False
        # if bird ran past previous pole
        if (bird.xcor() - 60 > total_pipe[i].xcor() - total_pipe[i].shapesize()[1]*10):
          point += 1
          score.clear()
          score.write("Score : {}".format(point), align="center", font=("Courier", 14, "bold"))
      # higher pipe
      else:
        # top of bird higher than lower level of higher pipe
        if(bird.ycor() + 20 > total_pipe[i].ycor() - total_pipe[i].shapesize()[0]*10) and (bird.xcor() + 30 > total_pipe[i].xcor() - total_pipe[i].shapesize()[1]*10):
          playing = False
    # if pipe is out of line of sight
    if total_pipe[i].xcor() < -300:
      # move pipe back to front
      reposition(total_pipe[i], total_pipe[i+1], 600, random.randint(min_height, max_height))
    # move pipes
    total_pipe[i].backward(10)
  # simulate gravity
  bird.sety(bird.ycor() - 10)

# game over
if not playing:
  board = turtle.Turtle()
  board.hideturtle()
  board.speed(0)
  board.color("black")
  board.penup()
  board.write("Game Over", align="center", font=("Courier", 14, "bold"))

turtle.done()