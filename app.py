from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

url = "https://rickandmortyapi.com/api/"

@app.route('/')
def get_list_characters_page():
    response = urllib.request.urlopen(url + "character")
    characters = response.read()
    dict = json.loads(characters)

    return render_template("characters.html", characters=dict["results"])