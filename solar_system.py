import turtle

screen = turtle.Screen()
screen.title("Solar System Simulation")
screen.bgcolor("black")
screen.setup(width=800, height=800)

# planet statistics
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planet_colors = ["#c28967", "#c07e31", "#18b17c", "#e11817", "#f09532", "#a25460", "#0056bf", "#3ea0f5", "#836044"]
planet_velocity = [47.4, 35, 29.8, 24.1, 13.1, 9.7, 6.8, 5.4, 4.7] # km/s
planet_diameters = [4.88, 12.1, 12.76, 6.79, 142.98, 120.5, 51.12, 49.24, 2.38] # km
planet_distances = [0.39, 0.72, 1, 1.52, 5.2, 9.5, 19.19, 30.07, 39.5] # in AU
# irl to simulation ratio
diameter_ratio, distance_radius_ratio, velocity_ratio = 40, 20, 1
total_planets, total_names = [], []

# moon = turtle.Turtle()
# moon.color("#9195a2")

# sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("#f3770e")
sun.shapesize(0.5)
sun.speed(0)

# display planet name
for i in range(len(planet_names)):
  name = turtle.Turtle()
  name.hideturtle()
  name.speed(0)
  name.color("white")
  name.penup()
  name.goto(-planet_distances[i]*distance_radius_ratio, 0)
  name.write("{}".format(planet_names[i]),align="center", font=("Courier", 8, "normal"))
  total_names.append(name)
  
# planet appearance
for i in range(len(planet_names)):
  planet = turtle.Turtle()
  planet.shape("circle")
  planet.color(planet_colors[i])
  planet.shapesize(planet_diameters[i]/diameter_ratio)
  planet.speed(0)
  planet.penup()
  planet.goto(0, -planet_distances[i]*distance_radius_ratio)
  total_planets.append(planet)

while True:
  # screen.update()
  for planet in total_planets:
    # orbit travel color
    planet.pencolor("white")
    planet.pendown()
    # assign respective speed
    planet.speed(planet_velocity[total_planets.index(planet)]/velocity_ratio)
    # orbit with given radius
    planet.circle(planet_distances[total_planets.index(planet)]*distance_radius_ratio)
    planet.penup()
    # stop at 3 o'clock as display
    planet.circle(planet_distances[total_planets.index(planet)]*distance_radius_ratio, 90)
  break

turtle.done()