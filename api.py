from flask import Flask, jsonify
from python.infos import *

app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/cars")
def showCars():
    return jsonify(cars())

@app.route("/cars-problems")
def showCarsAndProblems():
    return jsonify(carsAndProblems())

@app.route("/cars-prices")
def showCarsAndPrices():
    return jsonify(carsAndPrice)

if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)