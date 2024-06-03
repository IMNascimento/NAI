from flask import Flask, request, jsonify
from .model_service import generate_text

def create_app():
    app = Flask(__name__)

    @app.route('/generate', methods=['POST'])
    def generate():
        input_data = request.json
        input_text = input_data.get("text", "")
        
        generated_text = generate_text(input_text)
        return jsonify({"generated_text": generated_text})

    return app