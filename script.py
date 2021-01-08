
from flask import Flask, redirect, url_for, request, render_template
from riotwatcher import LolWatcher, ApiError
import pandas as pd

app = Flask(__name__)

api_key = ''
watcher = LolWatcher(api_key)
my_region = 'na1'

@app.route('/')
def home():
   return 'Hello World'

@app.route('/<summoner_name>')
def lookup(summoner_name):
   me = watcher.summoner.by_name(my_region, str(summoner_name))
   my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

   ### Match History ### (This code is taken from How To Use Riot API website)
   my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
   df_html = ''

   for match in range(5):
       last_match = my_matches['matches'][match]
       match_detail = watcher.match.by_id(my_region, last_match['gameId'])

       participants = []
       for row in match_detail['participants']:
           participants_row = {}
           participants_row['champion'] = row['championId']
           #participants_row['spell1'] = row['spell1Id']
           #participants_row['spell2'] = row['spell2Id']
           participants_row['win'] = row['stats']['win']
           participants_row['kills'] = row['stats']['kills']
           participants_row['deaths'] = row['stats']['deaths']
           participants_row['assists'] = row['stats']['assists']
           participants_row['totalDamageDealtToChampions'] = row['stats']['totalDamageDealtToChampions']
           participants_row['goldEarned'] = row['stats']['goldEarned']
           participants_row['champLevel'] = row['stats']['champLevel']
           participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
           #participants_row['item0'] = row['stats']['item0']
           #participants_row['item1'] = row['stats']['item1']
           participants.append(participants_row)

       df = pd.DataFrame(data=participants)
       df_html += df.to_html()

   return render_template('summonerinfo.html', name = summoner_name, lines = me, ranked = my_ranked_stats, match_history = df_html)

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('lookup', summoner_name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('lookup', summoner_name = user))

if __name__ == '__main__':
   #app.run()
   app.run(debug = True)
