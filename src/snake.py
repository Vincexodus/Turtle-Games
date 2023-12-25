import random
import turtle
from time import sleep

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=800, height=800)

# available food positions
total_cords = []
pos= -380
for i in range(39):
  total_cords.append(pos)
  pos += 20

# food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(random.choice(total_cords), random.choice(total_cords))

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()

# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()

# input events
def left():
  if snake.heading() == 90:
    snake.left(90)
  elif snake.heading() == 270:
    snake.right(90)
def right():
  if snake.heading() == 90:
    snake.right(90)
  elif snake.heading() == 270:
    snake.left(90)
def up():
  if snake.heading() == 0:
    snake.left(90)
  elif snake.heading() == 180:
    snake.right(90)
def down():
  if snake.heading() == 0:
    snake.right(90)
  elif snake.heading() == 180:
    snake.left(90)

# Keyboard bindings
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

length = 0
body_list = []
playing = True

while playing:
  # hit surrounding walls
  if(snake.xcor() > 375 or snake.xcor() < -375) or (snake.ycor() > 380 or snake.xcor() < -380):
    playing = False
    break
  # movement based on heading
  if snake.heading() == 0:
    snake.goto(snake.xcor() + 20, snake.ycor())
  elif snake.heading() == 90:
    snake.goto(snake.xcor(), snake.ycor() + 20)
  elif snake.heading() == 180:
    snake.goto(snake.xcor() - 20, snake.ycor())
  elif snake.heading() == 270:
    snake.goto(snake.xcor(), snake.ycor() - 20)
  # move by frame
  sleep(0.1)
  # eat food
  if snake.position() == food.position():
    length += 1
    # new food change position
    food.goto(random.choice(total_cords), random.choice(total_cords))
    # new snake body
    body = turtle.Turtle()
    body.hideturtle()
    body.speed(0)
    body.shape("square")
    body.color("green")
    body.penup()
    body.showturtle()
    body_list.append(body)
  # starting from 2nd body decrement by 1, from snake tail to front
  # index, index-1, index-2, index-3, ......
  for index in range(len(body_list)-1, 0, -1):
    # head touches body
    if snake.pos() == body_list[index].pos():
      playing = False
    # position of front body
    x = body_list[index-1].xcor()
    y = body_list[index-1].ycor()

    # back body move to front
    body_list[index].goto(x, y)
  # first body
  if len(body_list) > 0:
    x = snake.xcor()
    y = snake.ycor()
    body_list[0].goto(x, y)

# game over
if not playing:
  score.write("Game Over\nScore : {}".format(length),align="center", font=("Courier", 14, "normal"))

turtle.done()