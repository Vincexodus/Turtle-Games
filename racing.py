from turtle import *
import random
import turtle

screen = Screen()
screen.setup(width=800, height=600)

# all available x coordinates
vertical_pos = [-300, -200, -100, 0, 100, 200, 300]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
total_t = []

for i in range(len(vertical_pos)):
  t = Turtle(shape="turtle")
  t.penup()
  t.color(colors[i])
  t.left(90)
  # move to assign position
  t.goto(x=vertical_pos[i], y=-260)
  total_t.append(t)

running = True
while running:
  for t in total_t:
    # move up with random distance
    random_distance = random.randint(0, 7)
    t.pendown()
    t.forward(random_distance)
    # if exceed top border
    if t.ycor() > 290:
      running = False

turtle.done()
