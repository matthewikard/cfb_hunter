import pandas as pd
import csv

categories = [
    "smallest_venue_rank",
    "largest_venue_rank",
    "elevation_rank",
    "wins_rank",
    "losses_rank",
    "enrollment_rank",
    "oldest_rank",
    "top_receiver_yards_rank"
]


def load_teams_from_csv(path, categories):
    teams = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            team = {
                "school": row["school"],
                "metrics": {
                    c: int(row[c]) for c in categories
                }
            }
            teams.append(team)

    return teams

teams = load_teams_from_csv("data/fbs_teams_ranked.csv", categories)