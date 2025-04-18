from flask import Flask, request, jsonify
import requests
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# One-time download for NLTK sentiment model
nltk.download('vader_lexicon')

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# LM Studio Endpoint
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

def detect_negative_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound'] < -0.2  # adjust threshold as needed

def rewrite_with_llm(original_text, desired_tone="neutral"):
    prompt = f"""
You are a helpful assistant. A customer wrote this message: "{original_text}".
Please rewrite the message in a {desired_tone} tone, keeping the meaning unchanged.
Return only the rewritten message.
"""
    payload = {
        "model": "your-model-name-here",  # LM Studio model name, e.g. llama-3-8b-instruct
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=payload)
        rewritten = response.json()['choices'][0]['message']['content']
        return rewritten.strip()
    except Exception as e:
        print("Error:", e)
        return "Error rewriting message."

@app.route('/transform', methods=['POST'])
def transform_text():
    data = request.get_json()
    original_text = data.get('text', '')
    
    if not original_text:
        return jsonify({"error": "No text provided."}), 400

    if detect_negative_sentiment(original_text):
        transformed_text = rewrite_with_llm(original_text, desired_tone="neutral")
        return jsonify({"transformed": transformed_text})
    else:
        return jsonify({"transformed": original_text})

if __name__ == '__main__':
    app.run(debug=True, port=1234)
