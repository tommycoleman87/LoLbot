class Player():
    def __init__(self, summoner, champion):
        self.summoner = summoner
        self.champion = champion
        self.roles = {
            'top_lane' : 0,
            'mid_lane' : 0,
            'jungle' : 0,
            'support' : 0,
            'carry' : 10
        }

    def main_role(self):
        return max(self.roles.values())