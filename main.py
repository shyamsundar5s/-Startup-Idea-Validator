from flask import Flask, request, jsonify
from validator import StartupIdeaValidator
from pdf_exporter import generate_pdf_report
from auth import User, check_premium_access

app = Flask(__name__)
validator = StartupIdeaValidator()

@app.route('/validate', methods=['POST'])
def validate_idea():
    data = request.json
    if not data or 'idea' not in data:
        return jsonify({'error': 'Please provide a business idea'}), 400

    # Extract user information and request details
    user = User(user_id=data.get('user_id', 'guest'), is_premium=data.get('is_premium', False))
    idea = data['idea']
    industry = data.get('industry')
    features = data.get('features', [])
    generate_pdf = data.get('generate_pdf', False)

    # Check for premium access if advanced features are requested
    if 'advanced' in features:
        access_error = check_premium_access(user)
        if access_error:
            return jsonify(access_error), 403

    # Validate the startup idea
    result = validator.validate(idea, industry)

    # Generate a PDF report if requested
    if generate_pdf:
        output_file = f"{idea.replace(' ', '_')}_report.pdf"
        generate_pdf_report(result, output_file)
        result['pdf_report'] = output_file

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
