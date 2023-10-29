from turtle import Turtle
import random

class Food(Turtle):
    """
    A class to represent the food in the Snake game.

    Attributes:
        None
    """

    def __init__(self):
        """
        Initializes a new Food instance with a circular shape and blue color.

        The initial position of the food is randomized within the game window.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        """
        Moves the food to a new random position within the game window.

        This method is called when the snake eats the food, and a new location
        for the food is needed.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
