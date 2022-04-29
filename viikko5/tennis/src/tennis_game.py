class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.results ={
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
            }

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def game_is_even(self, score):
        if score == 4:
            return "Deuce"
        else:
            return f"{self.results.get(score)}-All"

    def game_is_advantage(self, difference):
        if difference < 0:
            player = "player2"
        else:
            player = "player1"

        if abs(difference) == 1:
                return f"Advantage {player}"
        else:
                return f"Win for {player}"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.game_is_even(self.player1_score)
        
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.game_is_advantage(self.player1_score - self. player2_score)
        else:
            return f"{self.results.get(self.player1_score)}-{self.results.get(self.player2_score)}"
