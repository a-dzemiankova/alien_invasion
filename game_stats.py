import os.path


class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        if os.path.isfile(self.settings.filename):
            with open(self.settings.filename, 'r') as f:
                score = int(f.read())
        else:
            score = 0

        self.start_score = score
        self.high_score = score

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1