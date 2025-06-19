from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.count = 0
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align= 'left', font= FONT)

    def new_level(self):
        self.level += 1
        self.count = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER! You got hit☠️", align= 'center', font= FONT)

