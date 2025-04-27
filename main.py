from flask import Flask, request, jsonify
from validator import StartupIdeaValidator

app = Flask(__name__)
validator = StartupIdeaValidator()

@app.route('/validate', methods=['POST'])
def validate_idea():
    data = request.json
    if not data or 'idea' not in data:
        return jsonify({'error': 'Please provide a business idea'}), 400

    idea = data['idea']
    result = validator.validate(idea)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
