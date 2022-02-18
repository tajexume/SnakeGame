from turtle import Screen, Turtle
import time
import random
from food import Food
from snake import Snake
screen = Screen()
screen.setup(width=200, height=200)
screen.bgcolor('black')
screen.title('Snake Game')
snake = Snake()
food = Food(screen)
snake.start(screen,food)
screen.listen()
#screen.exitonclick()