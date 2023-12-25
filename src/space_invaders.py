import turtle
import random
import math

screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=600, height=800)

# player object
player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("cyan")
player.shapesize(1.5, 1.5)
player.penup()
player.left(90)
player.goto(0, -360)

# player bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("circle")
bullet.color("red")
bullet.shapesize(0.5, 0.5)
bullet.penup()
bullet.left(90)
bullet.hideturtle()
bullet.goto(1000, 1000)

# enemy quadron 
indicator = turtle.Turtle()
indicator.speed(0)
indicator.shape("square")
indicator.color("white")
indicator.shapesize(0.1, 23)
indicator.penup()
indicator.goto(-10, 350)

# player score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 360)
score.write("Score : 0",align="center", font=("Courier", 16, "normal"))

# motion input
def left():
  if player.xcor() >= -260:
    x = player.xcor()
    x -= 20
    player.setx(x)

def right():
  if player.xcor() <= 260:
    x = player.xcor()
    x += 20
    player.setx(x)

state = True
# bullet input
def shoot():
  global state
  if state == True:
    state = False
    bullet.goto(player.xcor(), player.ycor() + 20)
    bullet.showturtle()

# object collision
def collision(a ,b):
  distance = math.sqrt(math.pow(a.xcor() - b.xcor(), 2) + math.pow(a.ycor() - b.ycor(), 2))
  return True if distance < 25 else False

# color based on height
alien_colors = ["green", "blue", "red", "orange", "yellow"]

# available alien x position
left_alien = -220
total_pos = []
for i in range(8):
  total_pos.append(left_alien)
  # interval distance between each other
  left_alien += 60

all_alien = []
height = [340, 300, 260, 220, 180]
for i in  height:
  # random column spawns
  for j in random.sample(total_pos, random.randint(1, 4)):
    alien = turtle.Turtle()
    alien.hideturtle()
    alien.penup()
    alien.speed(0)
    alien.shape("classic")
    alien.left(90)
    alien.color(alien_colors[height.index(i)])
    alien.shapesize(4, 2)
    alien.goto(j, i)
    alien.showturtle()
    all_alien.append(alien)

# input functions
screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(shoot, "space")

playing = True
speed = 10
direction, point  = 1, 0

while playing:
  for alien in all_alien:
    # alien motion
    x = alien.xcor()
    x += speed * direction
    alien.setx(x)
    # to detect edges
    indicator.setx(indicator.xcor() + speed/len(all_alien) * direction)
    # quadron touches right edge
    if indicator.xcor() + indicator.shapesize()[1]*10 > 290:
      for a in all_alien:
        y = a.ycor()
        y -= 20
        a.sety(y)
      direction *= -1
    # quadron touches left edge
    elif indicator.xcor() - indicator.shapesize()[1]*10 < -290:
      for a in all_alien:
        y = a.ycor()
        y -= 20
        a.sety(y)
      direction *= -1
    # bullet collide with alien
    if collision(bullet, alien):
      alien.goto(1000, 1000)
      bullet.goto(player.pos())
      bullet.hideturtle()
      point += 1
      score.clear()
      score.write("Score : {}".format(point),align="center", font=("Courier", 16, "normal"))
    # player collide with alien
    if collision(player, alien) or alien.ycor() < player.ycor() + 20:
      playing = False
  # space button pressed
  if not state:
    y = bullet.ycor()
    y += 75
    bullet.sety(y)
  # bullet exceed edge of top
  if bullet.ycor() > 360:
    state = True
    bullet.hideturtle()
  if point == len(all_alien):
    break

# lose the game
if not playing:
  score.clear()
  score.goto(0, 0)
  score.write("Game Over !!!\n {} points".format(point),align="center", font=("Courier", 16, "normal"))

# win the game
score.clear()
score.goto(0, 0)
score.write("Victory !!!\n {} points".format(point),align="center", font=("Courier", 16, "normal"))

turtle.done()