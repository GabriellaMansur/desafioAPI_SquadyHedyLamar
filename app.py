from flask import Flask, render_template
import urllib.request, json
from werkzeug.exceptions import BadRequest

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

@app.route('/location/<id>')
def  get_location(id):
    response = urllib.request.urlopen(url + "location/" + id)
    location = response.read()
    dict = json.loads(location)
    residents = [resident for resident in dict.get('residents')]
    characters = [json.loads(urllib.request.urlopen(resident).read().decode('utf-8')) for resident in residents]
    return render_template("location.html", location=dict, characters=characters)

@app.route("/locations")
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    locations_dict = json.loads(data)

    return render_template("locations.html", locations=locations_dict['results'])

@app.route("/location/<id>")
def get_location(id):
    # Validação do id fornecido pelo usuário
    if 0 < int(id) < 127:
        # Acessar a api do Ricky and Morty e carregar os dados da localização
        url = "https://rickandmortyapi.com/api/location/" + id
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)

    # Levantar erro se o id fornecido não consta na base de dados da api
    else:
        raise BadRequest(f"Localização com o id {id} não encontrada")
    
    residents = {}
   
    # Acessar os dados de cada um dos residentes da localização fornecida e extrair o nome do personagem
    for url_character in dict["residents"]:
        url2 = url_character
        response2 = urllib.request.urlopen(url2)
        data_character = response2.read()
        dict_character = json.loads(data_character)
        residents[dict_character["id"]] = dict_character["name"]

    return render_template("location.html", location=dict, characters=residents)

if __name__ == '__main__':
    app.run(debug=True)