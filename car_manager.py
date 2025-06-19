import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def new_car(self):
        color = random.choice(COLORS)
        car = Turtle()
        car.speed('fastest')
        car.penup()
        car.color(color)
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        y = random.randint(-240, 240)
        car.goto(300, y)
        self.cars.append(car)

    def move_car(self, car, level):
        if car.xcor() > -300:
            new_x = car.xcor() - (STARTING_MOVE_DISTANCE + ((level -1)*MOVE_INCREMENT))
            car.goto(new_x, car.ycor())
        else:
            car.hideturtle()
            self.cars.remove(car)