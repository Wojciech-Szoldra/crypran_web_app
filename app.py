import secrets
import string
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'twoj_tajny_klucz_aplikacji'  # Wymagane do działania flash i session

# Generowanie hasła - funkcja pozostaje prawie taka sama
def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    length = 12  # Domyślna długość
    
    if request.method == 'POST':
        try:
            length = int(request.form.get('length', 12))
            
            if length <= 0:
                flash("Długość musi być większa od 0.", "error")
            elif length > 50:
                flash("Długość nie może być większa niż 50.", "error")
            else:
                password = generate_password(length)
                session['password'] = password  # Przechowanie hasła w sesji
                flash("Hasło zostało wygenerowane!", "success")
        except ValueError:
            flash("Niepoprawna wartość długości. Wprowadź liczbę.", "error")
    
    return render_template('index.html', password=password, length=length)

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
        session['password'] = password  # Przechowanie hasła w sesji
        
        return jsonify({'password': password, 'message': 'Hasło wygenerowane!'})
    except ValueError:
        return jsonify({'error': 'Niepoprawna wartość długości.'}), 400

if __name__ == '__main__':
    app.run(debug=True)