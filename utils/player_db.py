import pandas as pd
from rapidfuzz import process
from datetime import datetime

class PlayerDB:

    def __init__(self, data_path: str = 'data/player/players_68_24.csv'):
        self.players = pd.read_csv(data_path)
        self.names_list = self.players['name'].dropna().unique().tolist()

    def get_player_from_name(self, name, game_date: datetime = datetime.now()):
        best_match, score, index = process.extractOne(name, self.names_list)
        player_dict = self.players[self.players['name'] == best_match].iloc[0].to_dict()

        last_tourney_date = player_dict['last_tourney_date']
        last_tourney_age = player_dict['age']

        time_delta_days = (game_date - datetime.strptime(str(last_tourney_date), '%Y%m%d')).days
        current_age = round(last_tourney_age + (time_delta_days / 365), 1)
        player_dict['age'] = current_age
        del(player_dict['id'])
        del(player_dict['last_tourney_date'])

        return player_dict