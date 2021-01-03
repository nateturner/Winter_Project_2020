
from flask import Flask, redirect, url_for, request, render_template
from riotwatcher import LolWatcher, ApiError

app = Flask(__name__)

@app.route('/')
def home():
   return 'Hello World'

api_key = ''
watcher = LolWatcher(api_key)
my_region = 'na1'

@app.route('/<summoner_name>')
def lookup(summoner_name):
   me = watcher.summoner.by_name(my_region, str(summoner_name))
   my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
   return render_template('summonerinfo.html', name = summoner_name, lines = me, ranked = my_ranked_stats)

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
