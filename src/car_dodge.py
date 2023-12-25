from sys import maxsize
from time import time
import random
import turtle

screen = turtle.Screen()
screen.title("Car dodging game")
screen.bgcolor("grey")
screen.setup(width=600, height=800)

# player object
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("black")
player.shapesize(1.5, 1.5)
player.penup()
player.left(90)
player.goto(0, -360)

# game level display
level = turtle.Turtle()
level.speed(0)
level.color("black")
level.penup()
level.hideturtle()
level.goto(0, 360)
level.write("Level : 1",align="center", font=("Courier", 16, "normal"))

# scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.hideturtle()
score.goto(0, 0)

# input motion
def left():
  if player.xcor() >= -260:
    x = player.xcor()
    player.setx(x - 30)

def right():
  if player.xcor() <= 260:
    x = player.xcor()
    player.setx(x + 30)

# all available color & spawn position
car_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
total_pos = []

# obtain all x coordinates of car
left_car = -260
for i in range(14):
  total_pos.append(left_car)
  left_car += 40

# car spawn randomizer, max 14 cars
def spawn(min_car, max_car):
  total_cars = []
  # car rows
  for i in [340, 420, 500, 580, 660]:
    car_spawns = random.randint(min_car, max_car)
    random_pos = random.sample(total_pos, car_spawns)
    # car columns
    for j in range(car_spawns):
      car = turtle.Turtle()
      car.hideturtle()
      car.penup()
      car.speed(0)
      car.shape("square")
      car.right(90)
      car.color(random.choice(car_colors))
      car.shapesize(1, 2, 2)
      car.goto(random_pos[j], i)
      car.showturtle()
      total_cars.append(car)
  return total_cars

# input functions
screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

running = True

# game variables
count, level_count = 0, 0
min_spawn, max_spawn = 4, 7
min_speed, max_speed = 10, 20

while running:
  # level 1
  if(count % 70 == 0):
    level_count += 1
    level.clear()
    level.write("Level : {}".format(level_count),align="center", font=("Courier", 16, "normal"))
    # car spawns
    cars = spawn(min_spawn, max_spawn)
    min_spawn += 1
    max_spawn += 1
    min_speed += 10
    max_speed += 10
  count += 1
  for car in cars:
    # car between impace range & touchs vertical position of player
    if (car.ycor() < -320 and car.ycor() > -360) and (car.xcor() < player.xcor() + 30 and car.xcor() > player.xcor() - 30):
      running = False
    random_distance = random.randint(10, 20)
    car.forward(random_distance)

# game over
if not running:
  level.clear()
  level.write("Game Over !!!",align="center", font=("Courier", 16, "normal"))
  score.write("Score : {}".format(count//5),align="center", font=("Courier", 16, "normal"))
  
turtle.done()

# limits :
#   move cars back to front instead of spawning 
#   larger player collision surface

