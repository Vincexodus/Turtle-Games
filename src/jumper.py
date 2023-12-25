import random
import time
import turtle

from cv2 import moveWindow

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

# fake display
ground = turtle.Turtle()
ground.speed(0)
ground.shape("square")
ground.color("green")
ground.shapesize(10, 40)
ground.penup()
ground.goto(0, -200)

obstacle_list = []
# path blocking obstacle
def create_obs(height, x, y):
  obstacle = turtle.Turtle()
  obstacle.hideturtle()
  obstacle.speed(0)
  obstacle.shape("square")
  obstacle.color("brown")
  obstacle.shapesize(height, 2)
  obstacle.penup()
  obstacle.goto(x, y - (4 - height)*10)
  obstacle.showturtle()
  return obstacle

# obstacle horizontal position
start_xpos = random.randint(100, 300)
for i in range(3):
  obs = create_obs(random.randint(2, 5), start_xpos, -60)
  start_xpos += start_xpos
  obstacle_list.append(obs)

# scoreboard
score = turtle.Turtle()
score.hideturtle()
score.speed(0)
score.color("black")
score.penup()
score.goto(300, 260)
score.write("000000", align="center", font=("Courier", 16, "normal"))

# display panel
board = turtle.Turtle()
board.hideturtle()
board.speed(0)
board.color("black")
board.penup()

floor = True
# input event
def jump():
  global floor 
  floor = False

# Keyboard bindings
screen.onkeypress(jump, "space")
screen.listen()

extra_hitbox = player.shapesize()[1]*10
# game stats
count = 0
playing = True
move_speed = 10
jump_speed = move_speed/5

# game title
board.write("Jumper", align="center", font=("Courier", 16, "normal"))
time.sleep(2)
board.clear()

while playing:
  # obstacle speed up
  move_speed += 0.01
  # update scores
  count += 1
  score.clear()
  score.write("{:06d}".format(count), align="center", font=("Courier", 16, "normal"))
  # for every obstacle
  for obs in obstacle_list:
    # obstacle within player range
    if (obs.xcor() < -280 and obs.xcor() > -340):
      # player touches obstacle
      if(player.xcor() + player.shapesize()[1]*10 > obs.xcor() - obs.shapesize()[1]*10) or (player.ycor() - player.shapesize()[0]*10 > obs.ycor() + obs.shapesize()[0]*10):
        playing = False
    # move forward continously
    obs.backward(move_speed)
    # obstacle reposition
    if obs.xcor() < -380:
      obs.setx(random.randint(600, 1200))
  # when jumped
  if not floor:
    # velocity decreases as height increases
    for i in range(7, 0 , -1):
      for obs in obstacle_list:
        obs.backward(move_speed)
        player.sety(player.ycor() + jump_speed*i)
    for i in range(8):
      # velocity increases upon falling
      for obs in obstacle_list:
        obs.backward(move_speed)
        player.sety(player.ycor() - jump_speed*i)
  floor = True

# game over
if not playing:
  board.clear()
  board.write("Game Over !", align="center", font=("Courier", 16, "normal"))

# issues 
  # weird player collisions
turtle.done()