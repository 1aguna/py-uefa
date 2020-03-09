# class color:
#     PURPLE = '\033[95m'
#     CYAN = '\033[96m'
#     DARKCYAN = '\033[36m'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = '\033[91m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     END = '\033[0m'


# league_vals holds a dictionary of the ranges of position within
# the league's table in order to qualify for the champions league, europa league
# or if the team is going to be relegated
league_vals = {
    'BL': {'ucl': range(1, 5), 'europa': range(5, 7), 'rlgate': range(16, 19)},
    'EPL': {'ucl': range(1, 5), 'europa': range(5,6), 'rlgate': range(18, 21)},
    'ERED': {'ucl': range(1, 3), 'europa': range(3,4), 'rlgate': range(16, 19)},
    'LL': {'ucl': range(1, 5), 'europa': range(5, 7), 'rlgate': range(18, 21)},
    'L1': {'ucl': range(1, 4), 'europa': range(4,5), 'rlgate': range(18, 21)},
    'PPL': {'ucl': range(1, 3), 'europa': range(3, 5), 'rlgate': range(16, 19)},
    'SA': {'ucl': range(1, 5), 'europa': range(5, 7), 'rlgate': range(18, 21)},
    'UCL': {},
}

league_sizes ={
    'BL': 18,
    'EPL': 20,
    'ERED': 18,
    'LL': 20,
    'L1': 20,
    'PPL': 18,
    'SA': 20,
    'UCL': 32,
}

codes = {
    'Bundesliga': 2002,
    'BL': 2002,
    'English Premier League': 2021,
    'EPL': 2021,
    'Eredivisie': 2003,
    'ERED': 2003,
    'La Liga': 2014,
    'LL': 2014,
    'Ligue 1': 2015,
    'L1': 2015,
    'Primeira Liga': 2017,
    'PPL': 2017,
    'Serie A': 2019,
    'SA': 2019,
    'UEFA Champions League': 2001,
    'UCL': 2001,
}
