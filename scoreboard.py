from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    """
    A class to represent the scoreboard in the Snake game.

    Attributes:
        score (int): The player's current score.
    """

    def __init__(self):
        """
        Initializes a new Scoreboard instance with an initial score of 0.

        The scoreboard is displayed at the top of the screen.
        """
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
          self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the displayed score on the scoreboard.
        """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the player's score by 1 and updates the scoreboard.
        """
        self.score += 1
        self.update_scoreboard()

    def reset(self):
      """
      reset the score, and update the highest score
      """
      if self.score > self.high_score:
        self.high_score = self.score
        with open("data.txt",mode="w") as data:
          data.write(f"{self.high_score}")
      self.score = 0
      self.update_scoreboard()

