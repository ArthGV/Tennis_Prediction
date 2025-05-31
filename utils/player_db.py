import pandas as pd
import pandasql as ps
from rapidfuzz import process

data_path = '../data/player/players_68_24.csv'

class PlayerDB:

    def __init__(self, data_path: str = 'data/player/players_68_24.csv'):
        self.players = pd.read_csv(data_path)
        self.names_list = self.players['name'].dropna().unique().tolist()

    def get_player_from_name(self, name):
        best_match, score, index = process.extractOne(name, self.names_list)
        return self.players[self.players['name'] == best_match]