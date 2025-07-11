from flask import Flask, request, jsonify
from scraper import buscar_produtos

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    termo = request.args.get('q', '')
    if not termo:
        return jsonify({"erro": "Parâmetro 'q' é obrigatório"}), 400
    resultados = buscar_produtos(termo)
    return jsonify(resultados)

@app.route('/')
def home():
    return jsonify({"mensagem": "API ProcuraPro funcionando!"})
