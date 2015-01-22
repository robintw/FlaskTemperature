from get_temp import get_temperature

from flask import Flask
app = Flask(__name__)

@app.route("/temperature")
def hello():
    return str(get_temperature())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
