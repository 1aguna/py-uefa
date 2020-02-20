import requests
import json
import os
import sys
import dictionaries as config
from tabulate import tabulate
from termcolor import colored

BASE_URL = 'http://api.football-data.org/v2/'  # base url for API
API_KEY = os.environ["SSC_KEY"]


def print_teams():
    """
    Available leagues to choose from
    Input from user must match the code in paranthesis
    eg. League Name (CODE)2
    """

    print("Bundesliga (BL)")
    print("English Premier League (EPL)")
    print("Eredivisie (ERED)")
    print("La Liga (LL)")
    print("Ligue 1 (L1)")
    print("Primeira Liga (PPL)")
    print("Serie A (SA)")
    print("UEFA Champions League (UCL)")

    return

def get_standings(league_key):
    """
    Make API call to get league information. Prints league information
    in tablular format. Free tier API limit number of calls per month

    Args:
        league_key (string): The league code used to make API call
    """

    # Make call to football data API to get league information
    custom_headers = {"X-Auth-Token": API_KEY}
    response = requests.get(
        BASE_URL +
        "competitions/" +
        str(config.codes[league_key]) +
        "/standings",
        headers=custom_headers)
    standings = response.json()  # turn response string into dictionary

    # set var to correct path to access standings easier
    curr_league = standings["standings"][0]["table"]

    # assemble the data table
    size = config.league_sizes[league_key]
    league_table = [None] * size  # number of teams

    
    i = 0
    while i < size:
        # team_list represents the data of ONE team
        for team in curr_league:
            team_list = [None] * 9
            team_list[0] = team["team"]["name"]

            #print(team_list[0])
            team_list[1] = team["playedGames"]
            team_list[2] = team["won"]
            team_list[3] = team["draw"]
            team_list[4] = team["lost"]
            team_list[5] = team["goalsFor"]
            team_list[6] = team["goalsAgainst"]
            team_list[7] = team["goalDifference"]
            team_list[8] = team["points"]
            # now to apply appropriate modifications to the list
            # things like relegation colors or bold
            team_list = modify_strings(team_list, i, league_key)
            league_table[i] = team_list  # assign modified list to table
            i += 1

    standings_headers = ["Team", "GP", "W", "D", "L", "GF", "GA", "GD", "PTS"]
    print(chr(27) + "[2J") # clear terminal
    print(tabulate(league_table, headers = standings_headers))
    
    return 


def modify_strings(data_row, position, league_id):
    """
    function to find out which the appropriate config.coloring of each team
    Leagues handle relegation differently
    Champions league and europe league slots can also change over the season
    so i left them seperately as well.
    I chose to have different paths for all the leagues
    in order to make changes to each leagues

    Args:
        data_row is a single row in the table
        contains a singles entire team's standings data

        data_row[0] teams name
        data_row[1] games played
        data_row[2] Wins
        data_row[3] draws
        data_row[4] Loss
        data_row[5] goals for
        data_row[6] goals against
        data_row[7] goal differential
        data_row[8] pts

        league_id must be a string abbreviation of the leagues
        ie. BL, EPL, or SA

        position is the team's standing in the table
    """
    league_key = config.league_vals[league_id]

    # not functional atm
    if (
        data_row[0] == "UC Sampdoria" or
        data_row[0] == "AS Roma" or
        data_row[0] == "Olympique Lyonnais"
    ):
        data_row = standing_colors("bold", data_row)
    if position + 1 in league_key["ucl"]:
        data_row = standing_colors("ucl", data_row)
        return data_row
    elif position + 1 in league_key["europa"]:
        data_row = standing_colors("europa", data_row)
        return data_row
    elif position + 1 in league_key["rlgate"]:
        data_row = standing_colors("rlgate", data_row)
        return data_row
    else:
        return data_row


def standing_colors(qualif_code, manip_list):
    """
    Apply appropriate color manipulation to the teams. Each League
    has different metrics for qualifying for European leagues
    and getting relegated.

    Args:
        qualif_code (string): Modification to apply
        manip_list (string): Data to modify
    """
    if qualif_code == "ucl":
        i = 0
        while i < len(manip_list):
            manip_list[i] = colored(manip_list[i], "green")
            i += 1
        return manip_list
    elif qualif_code == "europa":
        i = 0
        while i < len(manip_list):
            manip_list[i] = colored(manip_list[i], "blue")
            i += 1
        return manip_list
    elif qualif_code == "rlgate":
        i = 0
        while i < len(manip_list):
            manip_list[i] = colored(manip_list[i], "red")
            i += 1
        return manip_list
    elif qualif_code == "bold":
        i = 0
        while i < len(manip_list):
            manip_list[i] = colored(manip_list[i], attrs=["bold"])
            i += 1
        return manip_list
    else:
        return manip_list

def test():
    """
    Test function. Try not to call often to conserve API calls

    Tests API call and string modification
    """
    custom_headers = {"X-Auth-Token": API_KEY}
    response = requests.get(BASE_URL + "competitions/" +
                            str(2019) + "/standings", headers=custom_headers)
    standings = response.json()  # turn response string into dictionary

    print(standings)

    base = "Hello"
    base = config.color.BOLD + base + config.color.END

    print(base)
    
def test_standings(league_key):  # league id is the NUMBER CODE
    """
    Test function. Try not to call to often to conserve API calls

    Checking for league config.codes outside of the for loop eliminates
    excess checking but creates duplicate code
    """

    custom_headers = {"X-Auth-Token": API_KEY}
    response = requests.get(
        BASE_URL +
        "competitions/" +
        str(league_key) +
        "/standings",
        headers=custom_headers)
    standings = response.json()  # turn response string into dictionary
    # set var to correct path to access standings easier
    table = standings["standings"][0]["table"]
    
    total = 0
    for teams in table:  # for each team in the league
        if league_key == config.codes["Ligue 1"]:  # french ligue 1
            total += 1
            if teams["team"]["name"] == "FC Girondins de Bordeaux":
                # bold my favorite teams
                print(total, "-", config.color.BOLD +
                      teams["team"]["name"] + config.color.END)
            else:
                # otherwise print it normally
                print(total, "-", teams["team"]["name"])
        elif league_key == config.codes["Serie A"]:  # Italian serie a
            total += 1
            if teams["team"]["name"] == "Atalanta BC" or teams["team"]["name"] == "UC Sampdoria":
                print(total, "-", config.color.BOLD +
                      teams["team"]["name"] + config.color.END)
            else:
                print(total, "-", teams["team"]["name"])
        else:
            total += 1
            print(total, "-", teams["team"]["name"])

    return