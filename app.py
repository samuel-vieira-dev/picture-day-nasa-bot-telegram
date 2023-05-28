from flask import Flask, request
import requests

app = Flask(__name__)

base_url = "https://api.telegram.org/bot6191098144:AAEo8eVcA04tb5bszVESyMcQ6rxlcd1cKM8/"

@app.route('/', methods=['POST'])
def default():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    sendMessage(chat_id)
    sendPhoto(chat_id)

    return 'ok', 200

def sendMessage(chat_id):
    message_data = DayPicture()
    message = message_data['texto']
    url = base_url + f'sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(url)
    return response.json()

def sendPhoto(chat_id):
    photo_data = DayPicture()
    photo_url = photo_data['foto']
    url = f"https://api.telegram.org/bot6191098144:AAEo8eVcA04tb5bszVESyMcQ6rxlcd1cKM8/sendPhoto"
    data = {
        "chat_id": chat_id,
        "photo": photo_url
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