from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

url = "https://rickandmortyapi.com/api/"

@app.route('/')
@app.route('/<page>')
def get_list_characters_page(page='Anonymous'):

    pageUrl = "character"

    if page:
        pageUrl = "character/?page=" + page

    response = urllib.request.urlopen(url + pageUrl)
    characters = response.read()
    dict = json.loads(characters)

    info=dict["info"]

    nextPage=info['next'][-1:] 

    prevPage=0

    if info['prev'] != None:
        prevPage=info['prev'][-1:]

    return render_template("characters.html", characters=dict["results"], nextPage=nextPage, prevPage=prevPage)

@app.route('/profile/<id>')
def get_profile(id):
    response = urllib.request.urlopen(url + "character/" + id)
    characters = response.read()
    dict = json.loads(characters)

    return render_template("profile.html", profile=dict)

@app.route('/episodes')
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    ler_episodios = response.read()
    dict = json.loads(ler_episodios)
    
    return render_template("episodes.html",episodes=dict["results"])

@app.route("/locations")
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    locations_dict = json.loads(data)

    return render_template("locations.html", locations=locations_dict['results'])
