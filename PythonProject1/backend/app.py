from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = " "  # OpenWeather API Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather(city)
        return render_template("index.html", weather=weather_data)
    return render_template("index.html", weather=None)


def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
    else:
        return {"error": "City not found"}


if __name__ == "__main__":
    app.run(debug=True)
