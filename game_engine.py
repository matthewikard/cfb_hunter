import random

class Game:
    def __init__(self, teams, categories):
        self.categories = categories
        self.teams = random.sample(teams, len(categories))
        self.assignments = {}
        self.current_index = 0

    def current_team(self):
        return self.teams[self.current_index]

    def available_categories(self):
        return [c for c in self.categories if c not in self.assignments]

    def assign(self, category):
        if category not in self.available_categories():
            raise ValueError("Category not available")

        team = self.current_team()
        self.assignments[category] = team
        self.current_index += 1

    def is_complete(self):
        return self.current_index == len(self.categories)

    def score(self):
        return sum(
            team["metrics"][cat]
            for cat, team in self.assignments.items()
        )
