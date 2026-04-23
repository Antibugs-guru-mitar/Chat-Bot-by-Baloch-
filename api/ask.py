from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
GROQ_KEY = os.environ.get('GROQ_API_KEY')

def ask_tedi_gpt(question):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Tu Tedi Bot hai. Tu funny, desi, helpful hai. User ko 'Mitar' bol. Emoji use kar. Chote jawab de. 'meaaah' kabhi kabhi bol."},
            {"role": "user", "content": question}
        ],
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

@app.route('/', methods=['POST'])
def ask():
    question = request.json['question']
    try:
        reply = ask_tedi_gpt(question)
        return jsonify({"reply": reply})
    except:
        return jsonify({"reply": "Mitar dimaagh hang ho gaya 😂💀 Phir se pooch"})
