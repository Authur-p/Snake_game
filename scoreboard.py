from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")
filename = 'data.txt'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        with open(filename, 'r') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(filename, 'w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()