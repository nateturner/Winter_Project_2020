from flask import Flask
app = Flask(__name__)

@app.route('/')            # when 'blog' is entered in the url, the following int is taken in as the variable postID
def home():
   return 'Hello World'

@app.route('/<summoner_name>')
def lookup(summoner_name):
    return 'Showing data for %s' % summoner_name

if __name__ == '__main__':
   #app.run()
   app.run(debug = True)
