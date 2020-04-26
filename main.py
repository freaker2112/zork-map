
import turtle
t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
t.speed(0)
def north():
  t. heading()
  while t. heading() != 90:
    t. right(1)
  t. color('blue')
  t. forward(40)

def south():
  t. heading()
  while t. heading() != 270:
    t. right(1)
  t. color('red')
  t. forward(40)

def east():
  t. heading()
  while t. heading() != 0:
    t. right(1)
  t. color('yellow')
  t. forward(40)

def west():
  t. heading()
  while t. heading() != 180:
    t. right(1)
  t. color('purple')
  t. forward(40)

def northeast():
  t. heading()
  while t. heading() != 45:
    t. right(1)
  t. color('green')
  t. forward(40)

def northwest():
  t. heading()
  while t. heading() != 135:
    t. right(1)
  t. color('dark blue')
  t. forward(40)

def southeast():
  t. heading()
  while t. heading() != 315:
    t. right(1)
  t. color('orange')
  t. forward(40)

def southwest():
  t. heading()
  while t. heading() != 225:
    t. right(1)
  t. color('hot pink')
  t. forward(40)

def object_():
  t. color("white")
  t. left(90)
  t. forward(5)
  t. dot(5)
  t. penup
  t. backward(5)
  t. pendown

v_1 = 0
while v_1 < 10:
  choice = input ("please enter the direction you are going")
  if choice == "north" or choice == "n":
    north()
  elif choice == "south" or choice == "s":
    south()
  elif choice == "west" or choice == "w":
    west()
  elif choice == "east" or choice == "e":
    east()
  elif choice == "northeast" or choice == "ne":
    northeast()
  elif choice == "northwest" or choice == "nw":
    northwest()
  elif choice == "southeast" or choice == "se":
    southeast()
  elif choice == "southwest" or choice == "sw":
    southwest()
  elif choice == "object":
    object_()
  