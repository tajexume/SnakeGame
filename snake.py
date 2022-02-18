from turtle import Screen, Turtle
import time
from food import Food
class Snake:
  def __init__(self):
    self.screen = Screen()
    self.tim = []
    for x in range(0,3):
      self.tim.append(Turtle())
      self.tim[x].penup()
      self.tim[x].shape('square')
      self.tim[x].color('white')
      self.tim[x].setx(x * -20)
    self.screen.update()
  def addTurtle(self):
    startX = self.tim[len(self.tim)-1].xcor()
    startY = self.tim[len(self.tim)-1].ycor()
    newtim = Turtle()
    newtim.penup()
    newtim.goto(startX, startY)
    newtim.shape('square')
    newtim.color('White')
    self.tim.append(newtim)
    self.screen.update()
    time.sleep(.1)
  def move_right(self):
    #self.tim[0].forward(20)
    self.tim[0].setheading(0)
  def move_left(self):
    #self.tim[0].forward(20)
    self.tim[0].setheading(180)
  def move_up(self):
    #self.tim[0].forward(20)
    self.tim[0].setheading(90)
  def move_down(self):
    #self.tim[0].forward(20)
    self.tim[0].setheading(270)
  def start(self, scene, food):
    while True == True:
      scene.update()
      time.sleep(.1)
      scene.onkey(self.move_left,'Left')
      scene.onkey(self.move_right,'Right')
      scene.onkey(self.move_down,'Down')
      scene.onkey(self.move_up,'Up')
      scene._listen()
      for x in range(len(self.tim) - 1, 0, -1):
        newX = self.tim[x-1].xcor()
        newY = self.tim[x-1].ycor()
        self.tim[x].goto(newX, newY)
      self.tim[0].forward(20)
      food.isEaten(self,scene)