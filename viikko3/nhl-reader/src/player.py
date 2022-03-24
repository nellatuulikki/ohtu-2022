from unittest.case import _AssertRaisesContext


class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    def get_nationality(self):
        return self.nationality

    def get_all_points(self):
        return self.assists + self.goals
    
    def __str__(self):
        return f"{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(self.get_all_points()):2}"

