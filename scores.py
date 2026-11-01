from turtle import Turtle


class Score(Turtle):
    def __init__(self, x):
        super().__init__()

        self.score = 0
        

        self.color('white')
        self.penup()
        self.hideturtle()

        self.goto(x, 300)

        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(self.score,align='center',font=('Arial', 20, 'normal'))