import turtle
import random
import time

screen = turtle.Screen()
screen.title("Ball Drop")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# player object
player = turtle.Turtle()
player.hideturtle()
player.speed(0)
player.shape("circle")
player.color("red")
player.shapesize(2)
player.penup()
player.goto(0, 160)

# player score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(240, 270)
score.write("000000",align="center", font=("Courier", 16, "normal"))

# upper line
divider = turtle.Turtle()
divider.speed(0)
divider.shape("square")
divider.color("navyblue")
divider.shapesize(0.5, 30)
divider.penup()
divider.goto(0, 255)

# coordincate list generator
def cord_list(start, interval, iteration):
  total_cords = []
  for _ in range(iteration):
    total_cords.append(start)
    start += interval
  return total_cords

# top spikes
for i in cord_list(-280, 40, 15):
  spike = turtle.Turtle()
  spike.hideturtle()
  spike.speed(0)
  spike.penup()
  spike.shape("triangle")
  spike.color("grey")
  spike.shapesize(2)
  spike.right(90)
  spike.goto(i, 240)
  spike.showturtle()

live_list = []
# player live number
for i in cord_list(-280, 20, 5):
  heart = turtle.Turtle()
  heart.hideturtle()
  heart.speed(0)
  heart.penup()
  heart.shape("circle")
  heart.color("red")
  heart.shapesize(0.75)
  heart.right(90)
  heart.goto(i, 280)
  heart.showturtle()
  live_list.append(heart)

# live number display
def live_update(lives):
  for i in range(len(live_list)):
    live_list[i].hideturtle()
  for l in range(lives):
    live_list[l].showturtle()

# motion input
def left():
  if player.xcor() >= -280:
    x = player.xcor()
    x -= 10
    player.setx(x)

def right():
  if player.xcor() <= 280:
    x = player.xcor()
    x += 10
    player.setx(x)

total_lines = []
# levitating platform
for i in  cord_list(130, -120, 5):
  # random column spawns
  line = turtle.Turtle()
  line.hideturtle()
  line.speed(0)
  line.penup()
  line.shape("square")
  line.color("navyblue")
  line.shapesize(1, 4)
  line.goto(random.randint(-260, 260), i)
  line.showturtle()
  total_lines.append(line)
player.setx(total_lines[0].xcor())
player.showturtle()

extra_hitbox = player.shapesize()[1]*10
# input functions
screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# game stats
count, lives, levitate_speed = 0, 5, 2
falling, playing = True, True
time.sleep(2)

while playing:
  # score display
  count += 1
  score.clear()
  score.write("{:06d}".format(count), align="center", font=("Courier", 16, "normal"))
  # gravity simulation
  if falling:
    fall_speed = 1.25*levitate_speed
  else:
    fall_speed = -levitate_speed/len(total_lines) 
  falling = True
  
  # all platforms
  for line in total_lines:
    # platform levitation
    y = line.ycor()
    y += levitate_speed
    line.sety(y)
    # player falling
    f = player.ycor()
    f -= fall_speed
    player.sety(f)
    # player and line collision
    if (player.xcor() + player.shapesize()[1]*10  <= line.xcor() + line.shapesize()[1]*10 + extra_hitbox) and (player.xcor() - player.shapesize()[1]*10 >= line.xcor() - line.shapesize()[1]*10 - extra_hitbox)\
    and (player.ycor() - player.shapesize()[0]*10 < line.ycor() + line.shapesize()[0]*10):
      falling = False
    # platform reposition
    if line.ycor() > 240: line.goto(random.randint(-250, 250), -360)
  # player dies
  if player.ycor() < -300 or player.ycor() > 200:
    # respawn
    for t in total_lines:
      # within initial player spawn height
      if t.ycor() < 120 and t.ycor() > 40:
        player.goto(t.xcor(), t.ycor() + 20)
    lives -= 1
    # no lives left
    if lives < 1:
      playing = False
    live_update(lives)
    time.sleep(2)

# game over
if not playing:
  score.clear()
  score.goto(0, 0)
  score.write("Game Over !!!\nScore: {}".format(count), align="center", font=("Courier", 16, "normal"))

turtle.done()