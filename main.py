import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from welcomescreen import WelcomeScreen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('beige')
screen.tracer(0)
screen.listen()

welcome_screen = WelcomeScreen()

def run_game():
    global is_game_running
    if is_game_running: return

    is_game_running = True

    welcome_screen.clear()
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    screen.onkey(player.move_up, 'Up')

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        if scoreboard.count % (6/scoreboard.level) == 0.0:
            car_manager.new_car()
        scoreboard.count += 1

        if scoreboard.level > 6:
            game_is_on = False
            welcome_screen.win_game()

        for car in car_manager.cars:
            car_manager.move_car(car, scoreboard.level)

            if player.distance(car) < 26:
                game_is_on = False
                scoreboard.game_over()
                break

        if player.ycor() > 250:
            player.player_next_level()
            scoreboard.new_level()

is_game_running = False
screen.onkey(run_game, 'Return')

screen.exitonclick()
