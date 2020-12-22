from flask import Flask, redirect, url_for, request
from riotwatcher import LolWatcher, ApiError

app = Flask(__name__)

@app.route('/')
def home():
   return 'Hello World'

@app.route('/<summoner_name>')
def lookup(summoner_name):
    return 'Showing data for %s' % summoner_name

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('/', summoner_name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('/', summoner_name = user))

if __name__ == '__main__':
   #app.run()
   app.run(debug = True)
