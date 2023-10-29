import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize the Turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Ask the player if they want to play the game
play_game = turtle.textinput("Snake Game",  "Use the arrow keys to move a 'snake' around the board.\n As the snake finds food, it eats the food, and thereby grows larger.\n The game ends when the snake either moves off the screen or moves into itself.\n The goal is to make the snake as large as possible before that happens.\n\nDo you want to play the snake game? Click 'OK' or enter 'y' to start the game")

if play_game == "" or "y" or "yes":
    game_is_on = True
    while game_is_on:
        screen.update()  # Manually update the screen to control animation speed
        time.sleep(0.1)  # Control the game speed by sleeping between frames

        snake.move()  # Move the snake

        # Set up keyboard bindings
        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with walls
        if (
            snake.head.xcor() > 295
            or snake.head.xcor() < -295
            or snake.head.ycor() > 295
            or snake.head.ycor() < -295
        ):
          scoreboard.reset()
          snake.reset()


        # Detect collision with tail segments
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

# Allow the user to click to exit the game
screen.exitonclick()
