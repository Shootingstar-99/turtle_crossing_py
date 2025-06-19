from turtle import Turtle
FONT = ('Courier', 20, 'bold')

class WelcomeScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(0, 20)
        self.write("Welcome!", align= 'center', font= FONT)
        self.goto(0,-20)
        self.write("Press Enter to play!", align= 'center', font= FONT)
        self.goto(0, -50)
        self.write("(Rule: Don't Get Hit!)", align= 'center', font= ('Courier', 15, 'normal'))
