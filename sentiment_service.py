from flask import Flask, request, jsonify
from textblob import TextBlob
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)

@app.route('/analyze', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Sentiment analysis result',
            'examples': {
                'application/json': {
                    'score': 0.5
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'text',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'Text to analyze'
        }
    ]
})
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    return jsonify({"score": score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
