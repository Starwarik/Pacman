state = {'score': 0}

class Score():
    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

class ScoreSystem():
    def __init__(self):
        self.score = Score()

    def increment(self):
        self.score.set_score(get_score() += 1)

    def get_score(self):
        return score.get_score()
