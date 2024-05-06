from flask import Flask, request, jsonify
from models import generate_marketing_content

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    topic = data.get('topic')
    format = data.get('format')
    # You can include additional parameters like emotion, length, etc. from the request data
    
    # Generate marketing content based on the input
    content = generate_marketing_content(topic, format)
    
    return jsonify({'text': content})

if __name__ == '__main__':
    app.run(debug=True)
