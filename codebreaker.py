from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Variable global para almacenar el código secreto
secret_code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
print("Código secreto inicial", secret_code)  # Esto es solo para propósitos de prueba

def generate_secret_code():
    """Genera un nuevo código secreto de cuatro dígitos."""
    return ''.join([str(random.randint(0, 9)) for _ in range(4)])

@app.route('/')
def index():
    return jsonify({"Hello": "World"})

@app.route('/code')
def code():
    return jsonify({"code": secret_code})

@app.route('/code', methods=['POST'])
def set_code():
    global secret_code
    if not request.json or not 'new_code' in request.json:
        return jsonify({'error': 'Bad request, missing new_code'}), 400

    new_code = request.json['new_code']
    if len(new_code) != 4 or not new_code.isdigit():
        return jsonify({'error': 'New code must be four digits'}), 400
    
    secret_code = new_code
    return jsonify({'message': 'Secret code updated successfully'}), 200

@app.route('/code/guess', methods=['POST'])
def guess():
    if not request.json or not 'guess' in request.json:
        return jsonify({'error': 'Bad request'}), 400

    user_guess = request.json['guess']
    if len(user_guess) != 4 or not user_guess.isdigit():
        return jsonify({'error': 'Guess must be four digits'}), 400

    response = {
        'exact': sum(1 for x, y in zip(user_guess, secret_code) if x == y),
        'near': sum(min(user_guess.count(d), secret_code.count(d)) for d in set(secret_code)) \
                - sum(1 for x, y in zip(user_guess, secret_code) if x == y)
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333)
    app.run(debug=True)
