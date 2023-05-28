from flask import Flask, request
import requests

app = Flask(__name__)

base_url = "https://api.telegram.org/bot6191098144:AAEo8eVcA04tb5bszVESyMcQ6rxlcd1cKM8/"

@app.route('/', methods=['POST'])
def default():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    user_input = update['message']['text']

    if user_input.upper() != "FOTO DO DIA":
        sendMessage(chat_id, "Para ver a foto do dia selecionada pela NASA, envie: 'Foto do dia'")
        
    sendPhoto(chat_id)

    return 'ok', 200

def sendMessage(chat_id, message):
    url = base_url + f'sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(url)
    return response.json()

def sendPhoto(chat_id):
    data = DayPicture()
    photo_url = data['foto']
    caption = data['texto']
    url = f"https://api.telegram.org/bot6191098144:AAEo8eVcA04tb5bszVESyMcQ6rxlcd1cKM8/sendPhoto"
    data = {
        "chat_id": chat_id,
        "photo": photo_url,
        "caption": caption
    }
    response = requests.post(url, data=data)
    return response.json()

def DayPicture():
    requestNasaPhoto = requests.get('https://api.nasa.gov/planetary/apod?api_key=1nbbZjZ1uECdR6ftEGryeV9qqKKizdg4ySLHRNxB')
    response = requestNasaPhoto.json()
    body = {
        "texto": response['title'],
        "foto": response['url']
    }    
    return body

if __name__ == "__main__":
    app.run(debug=True)