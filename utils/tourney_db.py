import pandas as pd
from rapidfuzz import process

class TourneyDB:

    def __init__(self, data_path: str = 'data/tourney/tourneys_68_24.csv'):
        self.tourneys = pd.read_csv(data_path)
        self.names_list = self.tourneys['name'].dropna().unique().tolist()

    def get_tourney_from_name(self, name):
        best_match, score, index = process.extractOne(name, self.names_list)
        return self.tourneys[self.tourneys['name'] == best_match]