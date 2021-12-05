class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, winner):
        if winner == "player1":
            self.p1_score += 1
        else:
            self.p2_score += 1
    
    def get_score_name(self, score):
        if score == 0:
            return "Love-All"
        elif score == 1:
            return "Fifteen-All"
        elif score == 2:
            return "Thirty-All"
        elif score == 3:
            return "Forty-All"
        else:
            return "Deuce"
    
    def get_score_name_ending(self, score):
        for i in range(1, 3):
            if i == 1:
                temp = self.p1_score
            else:
                score += "-"
                temp = self.p1_score

            if temp == 0:
                score += "Love"
            elif temp == 1:
                score += "Fifteen"
            elif temp == 2:
                score += "Thirty"
            elif temp == 3:
                score += "Forty"
        return score

    def get_score(self):
        score = ""

        if self.p1_score == self.p2_score:
            score = self.get_score_name(self.p1_score)

        elif self.p1_score >= 4 or self.p2_score >= 4:
            minus_result = self.p1_score - self.p2_score

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = self.get_score_name_ending(score)

        return score
