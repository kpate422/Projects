######################################################
# Project: Project 1
# Student Name:  <your name: Patel, Krisha>
# UIN: <668999424>
# URL: <https://replit.com/@UICCS111HayesSpring2022/Project-1-KrishaPatel14#main.py>

# either list the students who provided help or remove the comment lines below
#For this project, I received help from the following members of CS111.
#Student1name, netID 12345678: help with background loop
#Student2name, netID 87654321: help with turtle heading and function parameters
 

######################################################
# imports
import turtle
import random

t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
height=500
width=500
# title="Project_1"

s=turtle.Screen()
s.setup(width=500, height=500)
s.tracer(0)

# Function defination
def draw_rectangle(t, x, y, heading, pensize, pen_color, fill_color, length, width):
  t.penup()
  t.fillcolor(fill_color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.goto(x,y)
  t.pensize(pensize)
  t.setheading(heading)
  t.forward(length)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(length)
  t.left(90)
  t.forward(width)
  t.hideturtle()
  t.pendown()
  t.end_fill()

def draw_triangle(t, x, y, heading, pensize, pen_color, fill_color, side_length):
  t.penup()
  t.fillcolor(fill_color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.goto(x,y)
  t.pensize(pensize)
  t.setheading(heading)
  t.forward(side_length)
  t.left(120)
  t.forward(side_length)
  t.left(120)
  t.forward(side_length)
  for i in range(3):
    t.left(120)
    t.forward(150)
    t.left(120)
    t.forward(150)
  
  t.pendown()
  t.end_fill()
  

def draw_circle(t, x, y, heading, pensize, pen_color, fill_color, radius, extent, steps):
  t.penup()
  t.fillcolor(fill_color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.goto(x,y)
  t.circle(radius)
  t.circle(extent)
  t.circle(steps)
  t.pensize(pensize)
  t.setheading(heading)
  t.hideturtle()
  t.pendown()
  t.end_fill()
  t.penup()


def draw_shape(t, x, y, heading, pensize, pen_color, fill_color, radius, extent, steps):
  t.penup()
  t.fillcolor(fill_color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.goto(x,y)
  t.circle(radius)
  t.circle(extent)
  t.circle(steps)
  t.pensize(pensize)
  t.setheading(heading)
  t.hideturtle()
  t.pendown()
  t.end_fill()
  t.penup()
  # for i in range(2):
  #   t.draw_arc_outline(x, y, 20, 20, 'black', 0, 90)
  #   t.draw_arc_outline(x + 40, y, 20, 20,'black', 90, 180)
  #   for bird_count in range(10):
  #     x = random.randrange(200, 580)
  #     y = random.randrange(100 // 3, 100 - 20)

  #   # Draw the bird.
  #     draw_shape(x, y)
# def draw_shape(t,x,y,radius):
#   t.goto(x,y)
#   t.dot(radius)
#   while True:
#     t1.clear()
#     x+=1
#   if(x>150):
#     x=-150-radius
# draw_shape(t1,0,0,25)

  
def draw_shape(t,x, y, heading, pensize, pen_color,radius,extent):
  t.penup()
  # t.fillcolor(fill_color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.goto(x,y)
  t.left(90)
  t.circle(radius)
  t.circle(extent)
  # t.circle(steps)
  t.left(-90)
  t.pensize(pensize)
  t.setheading(heading)
  t.hideturtle()
  t.pendown()
  t.end_fill()
  t.penup()



def draw_object(t,x, y, heading, pensize, pen_color,radius,extent):
  t.penup()
  # t.fillcolor(fill_color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.goto(x,y)
  t.left(90)
  t.circle(radius)
  t.circle(extent)
  # t.circle(steps)
  t.left(-90)
  t.pensize(pensize)
  t.setheading(heading)
  t.hideturtle()
  t.pendown()
  t.end_fill()
  t.penup()
  
def draw_background(t, x, y, heading, pensize, pen_color, fill_color, length, width):
  t.penup()
  t.fillcolor(fill_color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.goto(x,y)
  t.pensize(pensize)
  t.setheading(heading)
  t.forward(length)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(length)
  t.left(90)
  t.forward(width)
  t.hideturtle()
  t.pendown()
  t.end_fill()


def main():

  t1=turtle.Turtle()
  t2=turtle.Turtle()
  draw_background(t1,-4000,-300,0,10,"skyblue","skyblue",9000,9000)
  
  draw_rectangle(t1,800, 0, 0,10,"darkgreen","darkgreen",-5000,-600)

  #  draw_object
  draw_triangle(t1, 0, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, 100, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, 200, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, 300, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, 400, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, 500, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, 600, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, -100, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, -200, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, -300, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, -400, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, -500, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, -600, 0, 0, 10, "brown", "brown", 100)
  draw_triangle(t1, -700, 0, 0, 10, "brown", "brown", 100)

  draw_triangle(t2,-145,-250,0,10,"black","black",290)

  draw_rectangle(t2,-9,-90,0,10,"orange","orange",10, 30)
  draw_rectangle(t2,-9,-140,0,10,"orange","orange",10, 30)

  draw_rectangle(t3,-50,-220,0,10,"red","red",100,30)
  draw_rectangle(t4,-40,-235,0,10,"grey","grey",20,15)
  draw_rectangle(t4,20,-235,0,10,"grey","grey",20,15)
  draw_rectangle(t5,-40,-190,0,10,"red","red",80, 40)
  draw_rectangle(t5,-35,-187,0,10,"white","white",69, 30)

  draw_circle(t1,0,170,0,3,"yellow","yellow",40,0,0)

  draw_circle(t2,-45,-205,0,10,"yellow","yellow",10,0,0)
  draw_circle(t3,25,-205,0,10,"yellow","yellow",10,0,0)
  

  t1.goto(0,190)
  t1.color('white')
  t1.write("The Road to Paradise", align="center", font=("arial", 20, "bold"))
 
  # draw_shape


main()

print('Krisha Patel- 668999424')

list_of_colors=['lightblue','darkgreen','brown','red','grey','black','white','yellow']

x = [t1, t2, t3, t4, t5]

for item in x:
  item.speed(0)
  item.hideturtle()

# information for scorers

# on what line number is the required for loop?
# <line number>

# on what line number is the required use of a random number?
# <line number>

# on what line number is the required use of a conditional statement?
# <line number>

# on what line number is the required use of a list?
# <line number>
