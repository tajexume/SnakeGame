import turtle as t
import random
import time
class Food:
  def __init__(self,scene):
    t.colormode(255)
    self.nibble = t.Turtle()
    self.nibble.penup()
    self.nibble.hideturtle()
    self.cookFood(scene)
    #self.nibble.ht()
  def cookFood(self,scene):
    self.nibble.goto(random.randint(-100,100),random.randint(-100,100) )
    self.nibble.dot(10,'White')
    scene.update()
  def isEaten(self, snake, scene):
    if int(snake.tim[0].xcor() + 20) > int(self.nibble.xcor()) and int(snake.tim[0].xcor() - 20) < int(self.nibble.xcor()) and int(snake.tim[0].ycor() + 20) > int(self.nibble.ycor()) and int(snake.tim[0].ycor() - 20) < self.nibble.ycor():
      self.nibble.clear()
      self.cookFood(scene)
      snake.addTurtle()
      scene.update()
    scene.listen()