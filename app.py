from flask import Flask, render_template
import urllib.request,json

app = Flask(__name__)

@app.route("/")
def get_list_character_page():
    url = "https://rickandmortyapi.com/api/character/"
    # abre a conexao com a url especificada
    response = urllib.request.urlopen(url)
    #lê dados retornados pela URL
    data = response.read()
    #converete os dados JSON em dicionario python
    dict = json.loads(data)
    
    #renderiza um modelo HTML chamado "characters.html"
    #e passa os resultados da API como um argumento 
    # chamado "characters" para o modelo HTML
    return render_template("characters.html",characters=dict["results"])
    


'''
def hello_world():
    return '<h1>olá mundo</h1>'
'''