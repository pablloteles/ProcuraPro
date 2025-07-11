from flask import Flask, request, jsonify
from scraper import buscar_produtos

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    termo = request.args.get('q', '')
    resultados = buscar_produtos(termo)
    return jsonify(resultados)
