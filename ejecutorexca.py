from flask import Flask, render_template, request, jsonify
import lexicoexca

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Examen_casa.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    expression = request.form['expression']

    # Calcular el resultado de la expresión
    try:
        result = eval(expression)  # Usar eval para evaluar la expresión matemática
    except Exception as e:
        result = "Error"  # Si hay un error en la operación, mostrar "Error"
    
    # Tokenizar la expresión
    tokens = lexicoexca.tokenize(expression)

    # Devolver el resultado y los tokens al cliente
    return jsonify({"result": result, "tokens": tokens})

@app.route('/tree')
def tree():
    return render_template('tree.html')

if __name__ == '__main__':
    app.run(debug=True)
