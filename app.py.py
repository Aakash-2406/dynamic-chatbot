from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load GPT-style response generator
generator = pipeline('text-generation', model='gpt2')

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # Simple GPT-style response
    bot_response = generator(user_message, max_length=50, do_sample=True)[0]['generated_text']
    
    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
