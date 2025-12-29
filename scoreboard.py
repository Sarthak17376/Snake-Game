from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.up()
        self.score = 0
        with open("Day 020 - 021 - The Snake Game/data.txt") as file:
            self.highscore = int(file.read())
        self.create_scoreboard()

    def create_scoreboard(self):
        self.up()
        self.goto(0, 270)
        self.down()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=12)
        self.up()

    def increase_score(self):
        self.clear()
        self.down()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=12)
        self.up()

    def reset_score(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            with open("data.txt") as file:
                self.highscore = int(file.read())
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=12)
