import turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    A class to represent the snake in the Snake game.

    Attributes:
        segments (list): A list of Turtle objects representing the snake's body segments.
        head (Turtle): The head segment of the snake.
    """

    def __init__(self):
        """
        Initializes a new Snake instance with an initial set of segments.

        The snake starts with three body segments in the starting position.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def create_snake(self):
        """
        Creates the initial set of snake segments in the starting position.
        """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the specified position.

        Args:
            position (tuple): The position where the new segment should be added.
        """
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
      for seg in self.segments:
        seg.goto(800,800)
      self.segments.clear()
      self.create_snake()
      self.head = self.segments[0]
      self.head.color("red")


    def extend(self):
        """
        Extends the snake by adding a new segment to the end of its body.
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Moves the snake by updating the positions of its segments.

        The snake's head moves forward by a certain distance, and the rest of the
        body segments follow the head.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Changes the snake's direction to up (north) if it's not currently moving down (south).
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the snake's direction to down (south) if it's not currently moving up (north).
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the snake's direction to left (west) if it's not currently moving right (east).
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the snake's direction to right (east) if it's not currently moving left (west).
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
