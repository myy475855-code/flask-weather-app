from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
app.secret_key = "dev-secret"

OPENWEATHER_API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/weather")
def api_weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    r = requests.get(BASE_URL, params=params)
    data = r.json()

    return jsonify({
        "city": data["name"],
        "country": data["sys"]["country"],
        "description": data["weather"][0]["description"],
        "temp": data["main"]["temp"],
        "icon": data["weather"][0]["icon"]
    })

if __name__ == "__main__":
    app.run(debug=True)
