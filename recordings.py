from term_output import API_KEY
from term_output import BASE_URL
import json
import requests
import matplotlib.pyplot as plt

# http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/


def print_samp_standings():
    plt.plot([1,2],sa_standings["UC Sampdoria"])
    plt.show()

def update_sa_standings():
    
    # query to get new scores. Updates on wednesday 
    custom_headers = {"X-Auth-Token": API_KEY}
    response = requests.get(BASE_URL +"competitions/2019/standings", headers=custom_headers)
    standings = response.json()
    team_list = standings["standings"][0]["table"]

    with open('sa_standings') as json_file: 
        sa_standings = json.load(json_file)

    for team in team_list:
        key = team["team"]["name"]
        standing_array = sa_standings[key]
        standing_array.append(int(team["position"]))

        # must save these changes to file
    json_file = json.dumps(standing_array)
    f = open("sa_standings.json", "w")
    f.write(json_file)
    f.close()



sa_standings = {
    "AC Chievo Verona": [14,20],
    "AC Milan": [12,17],
    "ACF Fiorentina": [10,8],
    "AS Roma": [5,5],
    "Atalanta BC": [1,4],
    "Bologna FC 1909": [16,14],
    "Cagliari Calcio": [19,15],
    "Empoli FC": [2,10],
    "FC Internazionale Milano": [17,11],
    "Frosinone Calcio": [20,16],
    "Genoa CFC": [11,9],
    "Juventus FC": [3,1],
    "Parma Calcio 1913": [8,12],
    "SPAL 2013": [7,3],
    "SS Lazio": [15,19],
    "SSC Napoli": [4,2],
    "Torino FC": [18,13],
    "UC Sampdoria": [13,18],
    "US Sassuolo Calcio": [6,6],
    "Udinese Calcio": [9,7],
}

# json_file = json.dumps(sa_standings)
# f = open("sa_standings.json", "w")
# f.write(json_file)
# f.close()

print_samp_standings()

# https://datahub.io/awesome/football
# https://datahub.io/sports-data/italian-serie-a
