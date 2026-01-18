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