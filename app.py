from flask import Flask, request, jsonify, render_template
from lexico import Lexico

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classificar', methods=['POST'])
def classificar():
    data = request.json
    texto = data.get('texto', '')

    lexico = Lexico("Docs/LIWC.txt")

    classificacao = lexico.classic_classification(texto)

    return jsonify({'classificacao': classificacao})

if __name__ == '__main__':
    app.run(debug=True)