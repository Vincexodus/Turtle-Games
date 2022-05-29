import turtle

screen = turtle.Screen()
screen.title("Space Invasion")
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
# player score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 360)
score.write("Score : 0",align="center", font=("Courier", 16, "normal"))

# input motion
def left():
  if player.xcor() >= -260:
    x = player.xcor()
    x -= 30
    player.setx(x)

def right():
  if player.xcor() <= 260:
    x = player.xcor()
    x += 30
    player.setx(x)

timer = 0
shooting = True
load = False
# bullet appear
def shoot(load):
  if load:
    bullet.showturtle()
    load = False
  bullet.goto(player.xcor(), player.ycor() + 10)
# all available color & spawn position
alien_colors = ["green", "blue", "red", "orange", "yellow"]

# obtain all x coordinates of car
left_alien = -220
total_pos = []
for i in range(8):
  total_pos.append(left_alien)
  left_alien += 60

all_alien = []
height = [340, 300, 260, 220, 180]
# display cars into a list
for i in  height:
  for j in total_pos:
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
direction = 1
new_height = [h-20 for h in height]
print(new_height*5)
while playing:
  # bullet.forward(10)
  for alien in all_alien:
    if alien.xcor() > 260:
      direction = -1
      alien.sety(new_height[all_alien.index(alien)])
    elif alien.xcor() < -260:
      direction = 1 
    alien.setx(alien.xcor() + speed * direction)
    


if not playing:
  score.clear()
  score.goto(0, 0)
  score.write("Game Over !!!",align="center", font=("Courier", 16, "normal"))

# enemy move down after reaching left and right
# player bullet collision with enemy
# enemy bullet spontaneous shoot toward player
turtle.done()