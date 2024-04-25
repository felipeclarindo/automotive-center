from flask import Flask, jsonify

carsAndProblems = {
    "Toyota": "Problemas de queima de óleo em alguns modelos, resultando em consumo excessivo de óleo entre as trocas de óleo programadas.",
    "Honda": "Falhas na transmissão automática em alguns modelos, resultando em solavancos, trancos ou mau funcionamento geral da transmissão.",
    "Ford": "Problemas de confiabilidade da transmissão automática de dupla embreagem Powershift em alguns modelos, levando a solavancos, trancos ou falhas na transmissão.",
    "Chevrolet": "Problemas de qualidade do acabamento interior, incluindo rangidos, ruídos e peças quebradiças em alguns modelos.",
    "Volkswagen": "Problemas de confiabilidade do sistema elétrico e eletrônico, resultando em falhas ou mau funcionamento de componentes como luzes, sistemas de áudio e eletrônicos.",
    "BMW": "Problemas de confiabilidade do sistema elétrico e eletrônico, resultando em falhas ou mau funcionamento de componentes como luzes, sistemas de áudio e eletrônicos.",
    "Mercedes-Benz": "Problemas de confiabilidade do sistema elétrico e eletrônico, resultando em falhas ou mau funcionamento de componentes como luzes, sistemas de áudio e eletrônicos.",
    "Audi": "Problemas de confiabilidade do sistema de suspensão pneumática em alguns modelos, resultando em vazamentos de ar ou falhas no sistema.",
    "Nissan": "Problemas de confiabilidade da transmissão continuamente variável (CVT) em alguns modelos, resultando em solavancos, trancos ou falhas prematuras.",
    "Hyundai": "Problemas de corrosão prematura em alguns modelos, especialmente em regiões sujeitas a climas extremos ou ambientes corrosivos.",
    "Kia": "Problemas de confiabilidade do sistema de freio regenerativo em alguns modelos híbridos ou elétricos, incluindo perda de eficácia dos freios ou ruídos anormais.",
    "Subaru": "Problemas de confiabilidade do sistema de transmissão automática CVT em alguns modelos, incluindo solavancos, trancos ou falhas prematuras.",
    "Mazda": "Problemas de confiabilidade com o sistema de infotainment Mazda Connect em alguns modelos, incluindo falhas no touchscreen, conectividade Bluetooth intermitente ou falhas no sistema de navegação.",
    "Tesla": "Problemas de qualidade de construção e controle de qualidade, incluindo painéis de carroceria mal alinhados, acabamento interno irregular ou falhas de pintura.",
    "Fiat": "Problemas de confiabilidade do sistema de transmissão automática Dualogic em alguns modelos, incluindo solavancos, trancos ou falhas de operação.",
    "Volvo": "Problemas de confiabilidade do sistema de freio de estacionamento elétrico em alguns modelos, incluindo falhas no acionamento ou liberação.",
    "Jaguar": "Problemas de confiabilidade elétrica em alguns modelos, incluindo falhas no sistema de infotainment, sistemas de entretenimento ou falhas nos controles eletrônicos.",
    "Land Rover": "Problemas de confiabilidade do sistema de suspensão a ar em alguns modelos, incluindo vazamentos de ar, falhas na altura de condução ou falhas no sistema.",
    "Porsche": "Problemas de confiabilidade do sistema de transmissão PDK (Porsche Doppelkupplung) em alguns modelos, incluindo solavancos, trancos ou falhas de operação.",
    "Ferrari": "Problemas de confiabilidade do sistema de transmissão F1 (Ferrari Formula One) em alguns modelos, incluindo solavancos, trancos ou falhas de operação."
}

carsAndPrices = {
    "Toyota" : "R$ 500 a R$ 5.000",
    "Honda" : "R$ 1.000 a R$ 8.000",
    "Ford" : "R$ 1.500 a R$ 10.000",
    "Chevrolet" : "R$ 300 a R$ 3.000",
    "Volkswagen" : "R$ 800 a R$ 6.000",
    "BMW" : "R$ 800 a R$ 6.000",
    "Mercedes" : "R$ 800 a R$ 6.000",
    "Audi" : "R$ 1.500 a R$ 10.000",
    "Nissan" : "R$ 1.200 a R$ 9.000",
    "Hyundai" : "R$ 500 a R$ 4.000",
    "Kia" : "R$ 800 a R$ 6.000",
    "Subaru" : "R$ 1.200 a R$ 9.000",
    "Mazda" : "R$ 700 a R$ 5.000",
    "Tesla" : "R$ 700 a R$ 5.000",
    "Fiat" : "R$ 1.000 a R$ 8.000",
    "Volvo" : "R$ 1.000 a R$ 8.000",
    "Jaguar" : "R$ 700 a R$ 5.000",
    "Land Rover" : "R$ 1.500 a R$ 10.000",
    "Porsche" : "R$ 2.000 a R$ 15.000",
    "Ferrari" : "R$ 2.000 a R$ 15.000"
    }

cars = [
    "Toyota",
    "Honda",
    "Ford",
    "Chevrolet",
    "Volkswagen",
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Nissan",
    "Hyundai",
    "Kia",
    "Subaru",
    "Mazda",
    "Tesla",
    "Fiat",
    "Volvo",
    "Jaguar",
    "Land Rover",
    "Porsche",
    "Ferrari",
    ]

carsMoreProblems = {
    "Fiat" : "Marea",
    "Ford" : "Fiesta",
    "Chevrolet" : "Agile",
    "Renault" : "Sandero",
    "Volkswagen" : "Gol",
    "Fiat" : "Palio",
    "Citroën" : "C3",
    "Peugeot" : "206",
    "Renault" : "Logan",
    "Fiat" : "Siena",
}

app = Flask(__name__)

#Rota principal com informações da minha API.
@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to my API.",
        "endpoints": {
            "/cars": "Return a car list",
            "/cars-problems": "Return a problems list",
            "/cars-prices" : "Return a price list",
            }
        })

# Rota que retorna uma lista com os carros.
@app.route("/cars")
def showCars():
    return jsonify(cars)

# Rota que retorna um dicionario com os carros que mais dão problema e a marca de cada carro.
@app.route("/cars/more-problems")
def showCarsMoreProblem():
    return jsonify(carsMoreProblems)

# Rota que retorna um dicionario com o carro e o problema mais comum.
@app.route("/cars/problems")
def showCarsAndProblems():
    return jsonify(carsAndProblems)

# Rota que retorna um dicionario com o carro e os preços de orçamento medio.
@app.route("/cars/prices")
def showCarsAndPrices():
    return jsonify(carsAndPrices)

if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)