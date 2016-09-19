import requests
from flask import Flask, render_template
app = Flask(__name__,  template_folder="templates")


@app.route("/")
def hello():
    nombre = "yeswegaming"
    URL = "https://euw.api.pvp.net/api/lol/euw/v1.4/summoner/by-name/%s?%s"\
        % (nombre, api_key)
    print URL
    response = requests.get(URL)
    datos = response.json()
    URL_IMG = "http://ddragon.leagueoflegends.com/cdn/6.18.1/img/champion/Aatrox.png"
    # datos2 = json.dumps(datos)
    nameUser = datos[nombre]['name']
    idUser = datos[nombre]['id']
    profileIconId = datos[nombre]['profileIconId']
    summonerLevel = datos[nombre]['summonerLevel']
    return render_template('index.html', iconId=profileIconId,
                           level=summonerLevel, name=nameUser, id=idUser,
                           urlImg=URL_IMG)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
