class Player:
    def __init__(self, name, verifier, roller):
        self.name = name
        self.scoreboard = {}
        self.fpart_score = 0
        self.lpart_score = 0
        self.bonus_score = 0
        self.total_score = 0
        self.verifier = verifier
        self.roller = roller

    def add_session_score(self, score_type, points):
        self.scoreboard[score_type] = points

    def add_top_score(self, value):
        self.fpart_score += value

    def add_bonus_if_allowed(self):
        if self.fpart_score > 62:
            self.bonus_score = 50
            self.scoreboard['bonus'] = 50
        else:
            self.scoreboard['bonus'] = 0

    def get_fpart_score(self):
        return self.fpart_score

    def print_scoreboard(self):
        total_score = 0
        for key, value in self.scoreboard.items():
            print(f'{key} : {value}')
            total_score += value
        print(f'Total poäng: {total_score}')

    def get_verifier(self):
        return self.verifier

    def get_roller(self):
        return self.roller
