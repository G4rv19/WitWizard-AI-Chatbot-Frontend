from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)

BACKEND_URL = ' http://10.88.39.136:6969/backend'  # Replace <PC_IP> with your MacBook's IP address
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/backend', methods=['POST'])
def forward_message():
    try:
        data = request.get_json()
        message = data.get('message')
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BACKEND_URL, json={'message': message}, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'message': f"Error: {response.status_code}"}), response.status_code
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
