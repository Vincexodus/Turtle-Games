import turtle
from time import sleep

screen = turtle.Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=1000 , height=600)

# paddle ratio
paddle_width, paddle_length = 6, 2

# left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
# strech multiples dimensional value of original shapes 
# left pad is now 6 in width 2 in length
left_pad.shapesize(stretch_wid=paddle_width, stretch_len=paddle_length)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=paddle_width, stretch_len=paddle_length)
right_pad.penup()
right_pad.goto(400, 0)

# collision surface
paddle_surface = paddle_width * 14

# Circle ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# player initial score
player_1, player_2 = 0, 0

# scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 240)
score.write("0\t\t\t\t0",align="center", font=("Courier", 24, "normal"))

# Functions to move paddle vertically
left_bound, right_bound = False, False
def left_up():
  # top left border
  if left_pad.ycor() <= 220:
    y = left_pad.ycor()
    left_pad.sety(y + 20)

def left_down():
  # bottom left border
  if left_pad.ycor() >= -220:
    y = left_pad.ycor()
    left_pad.sety(y -20)

def right_up():
  # top right border
  if right_pad.ycor() <= 220:
    y = right_pad.ycor()
    right_pad.sety(y + 20)

def right_down():
  # bottom left border
  if right_pad.ycor() >= -220:
    y = right_pad.ycor()
    right_pad.sety(y - 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(left_up, "w")
screen.onkeypress(left_down, "s")
screen.onkeypress(right_up, "Up")
screen.onkeypress(right_down, "Down")

while True:
  screen.update()
  # ball starts moving
  hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
  hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

  # ball hit top line
  if hit_ball.ycor() > 280:
    # hit_ball.sety(280)
    # reverse horizontal motion
    hit_ball.dy *= -1
  
  # ball hit bottom line
  if hit_ball.ycor() < -280:
    # hit_ball.sety(-280)
    # reverse horizontal motion
    hit_ball.dy *= -1

  # ball went through right border
  if hit_ball.xcor() > 500:
    hit_ball.goto(0, 0)
    sleep(1)
    hit_ball.dy *= -1
    player_1 += 1
    score.clear()
    score.write("{}\t\t\t\t{}".format(player_1, player_2), align="center", font=("Courier", 24, "normal"))
  # ball went through left border
  if hit_ball.xcor() < -500:
    hit_ball.goto(0, 0)
    sleep(1)
    # hit_ball.dy *= -1
    player_2 += 1
    score.clear()
    score.write("{}\t\t\t\t{}".format(player_1, player_2), align="center", font=("Courier", 24, "normal"))

  # Ball reaches within right range and touches vertical coordinates of right paddle
  if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+ paddle_surface and hit_ball.ycor() > right_pad.ycor()- paddle_surface):
      # hit_ball.setx(360)
      # reverse vertical motion
      hit_ball.dx*=-1

  # Ball reaches within left range and touches vertical coordinates of left paddle
  if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+ paddle_surface and hit_ball.ycor()>left_pad.ycor()- paddle_surface):
      # hit_ball.setx(-360)
      # reverse vertical motion
      hit_ball.dx*=-1
