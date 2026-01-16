display_names = {
    'smallest_venue_rank': 'Smallest Venue',
    'largest_venue_rank': 'Largest Venue',
    'elevation_rank': 'Elevation',
    'wins_rank': 'Wins',
    'losses_rank': 'Losses',
    'enrollment_rank': 'Enrollment',
    'oldest_rank': 'First Year Played',
    'top_receiver_yards_rank': 'Top Receiver Yards (All Time)'
}

def map_column_names(columns):
    return [display_names[col_name] for col_name in columns]