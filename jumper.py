import random
import turtle

screen = turtle.Screen()
screen.title("Jumping game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# player object
player = turtle.Turtle()
player.speed(0)
player.shape("circle")
player.color("black")
player.shapesize(1.5)
player.penup()
player.goto(-300, -85)

ground = turtle.Turtle()
ground.speed(0)
ground.shape("square")
ground.color("green")
ground.shapesize(10, 40)
ground.penup()
ground.goto(0, -200)

obstacle = turtle.Turtle()
obstacle.hideturtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("red")
obstacle.shapesize(4, 2)
obstacle.penup()
obstacle.goto(200, -60)
obstacle.showturtle()

score = turtle.Turtle()
score.hideturtle()
score.speed(0)
score.color("black")
score.penup()
score.goto(300, 260)
score.write("000000", align="center", font=("Courier", 16, "normal"))

floor = True
def jump(floor):
  floor = False
  
screen.onkeypress(lambda: jump(floor), "space")
screen.listen()

count = 0
playing = True

while playing:
  obstacle.backward(10)
  if not floor:
    for i in range(10):
      player.sety(player.ycor() + 2*i)
    for i in range(10):
      player.sety(player.ycor() - 2*i)

  count += 1
  score.clear()
  score.write("{:06d}".format(count), align="center", font=("Courier", 16, "normal"))
  # screen.update()

if not playing:
  board = turtle.Turtle()
  board.hideturtle()
  board.speed(0)
  board.color("black")
  board.penup()
  board.write("Game Over !", align="center", font=("Courier", 16, "normal"))

turtle.done()