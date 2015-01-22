from get_temp import get_temperature

from flask import Flask
app = Flask(__name__)

@app.route("/sensor/temperature")
def hello():
    return get_temperature()

if __name__ == "__main__":
    app.run(host='0.0.0.0')