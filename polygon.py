import turtle

window = turtle.Screen() 
window.bgcolor("white") 

# get number of sides from user
side =  input("How many sides do you want your shape to have? (0-10): ")
# obtain integer betweeen 0 to 10 only
while(side.isdigit() == False or (int(side) < 1 or int(side) > 10)):
  side = input("Invalid input. Integers only! (0-10): ")

num = int(side)

pen = turtle.Turtle()
pen.pensize(5)         
for i in range(num):
  pen.forward(50)
  # move according to exterior angle
  pen.right(360/num)   
turtle.done()