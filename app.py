import secrets
import string
import hashlib
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'twoj_tajny_klucz_aplikacji'  # klucz do HMAC-SHA256

# Generowanie hasła - funkcja pozostaje prawie taka sama
def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

# Funkcja do generowania skrótu hasła
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/api/generate', methods=['POST'])
def api_generate():
    """Endpoint API do generowania hasła (dla żądań AJAX)"""
    try:
        data = request.get_json()
        length = int(data.get('length', 12))
        
        if length <= 0:
            return jsonify({'error': 'Długość musi być większa od 0.'}), 400
        elif length > 50:
            return jsonify({'error': 'Długość nie może być większa niż 50.'}), 400
        
        password = generate_password(length)
        session['password_hash'] = hash_password(password)  # Przechowanie hasha hasła w sesji
        
        return jsonify({'password': password, 'message': 'Hasło wygenerowane!'})
    except ValueError:
        return jsonify({'error': 'Niepoprawna wartość długości.'}), 400

if __name__ == '__main__':
    app.run(debug=True)