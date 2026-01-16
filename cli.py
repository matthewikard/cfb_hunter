from game_engine import Game
from data import teams, categories
import pandas as pd
import csv

game = Game(teams, categories)

while not game.is_complete():
    team = game.current_team()
    print(f"\nTeam: {team['school']}")
    print("Available categories:")
    for c in game.available_categories():
        print(f"- {c}")

    choice = input("Choose category: ")

    best_category = min(
        game.available_categories(),
        key=lambda c: team["metrics"][c]
    )
    
    game.assign(choice)

    print(
        f"\nBest possible category for {team['school']}: "
        f"{best_category} {team['metrics'][best_category]}"
    )

    print(
        f"\nCurrent Score: {game.score()}"
    )

    # After assigning a category, print the chosen categories and their ranks
    print("\nChosen categories and ranks:")
    for cat, team in game.assignments.items():
        print(f"- {cat}: {team['school']} {team['metrics'][cat]}")

print("\nGame complete!")
print("Assignments:")
for cat, team in game.assignments.items():
    print(cat, "→", team["school"], team["metrics"][cat])

print("Final score:", game.score())
