from player import Player

class PlayerStats:
    def __init__(self, stats):
        self.stats = stats
        request = self.stats.response()
        self.players = []
        for player_dict in request:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )
            self.players.append(player)

    def get_score(self, player):
        return player.goals + player.assists

    def top_scorers_by_nationality(self, nationality):
        response = []
        for player in self.players:
            if nationality == player.nationality:
                response.append(player)
        response.sort(key=self.get_score, reverse=True)
        return response
