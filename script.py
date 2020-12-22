
from flask import Flask, redirect, url_for, request
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
   output = "Showing data for %s<br/><br/>" % summoner_name
   me = watcher.summoner.by_name(my_region, str(summoner_name))
   output+="ACCOUNT DATA<br/><br/>"
   for line in me:
      output+=(str(line) + ': ' + str(me[line])+"<br/>")
   output+="<br/>"
   my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
   output+="RANKED DATA<br/><br/>"
   for line in my_ranked_stats[0]:
      output+=(str(line) + ': ' + str(my_ranked_stats[0][line]) + "<br/>")
   return output

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