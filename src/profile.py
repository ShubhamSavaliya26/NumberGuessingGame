class UserProfile:
    def __init__(self, username):
        self.username = username
        self.game_score = 0

    def save_profile(self, db):
        db.insert_score(self.username, self.game_score)
