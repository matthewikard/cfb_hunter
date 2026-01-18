import cfbd
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

configuration = cfbd.Configuration(
    access_token = os.getenv('CFBD_API_KEY')
)

logos_data = []

with cfbd.ApiClient(configuration) as api_client:
    api_instance = cfbd.TeamsApi(api_client)
    logos = api_instance.get_teams(year=2025)
    logos_data = [*logos, *logos_data]
        

logos_df = pd.DataFrame.from_records([dict(school = t.school,
                                           color = t.color,
                                           logo=t.logos[0] if t.logos else None) for t in logos_data])

logos_df = logos_df.drop_duplicates()

def override_school_name(df, old_name, new_name):
    df.loc[df['school'] == old_name, 'school'] = new_name
    print(f"Updated '{old_name}' to '{new_name}'")
    return(df)

override_school_name(logos_df, 'App State', 'Appalachian State')

logos_df.to_csv("data/team_logos.csv", index=False)

teams = pd.read_csv("data/fbs_teams_ranked.csv")

teams = teams.merge(logos_df, on="school", how="left")

teams.to_csv('data/fbs_teams_ranked.csv')