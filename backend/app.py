# Simple Backend for DarkEye (Python)
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests



# Placeholder for monitoring keywords and alert simulation
MONITORED_KEYWORDS = ["password", "credit card", "SSN",'social attack',"harshitha@gmail.com",
                      'phising','malware','virus','worms']

# Simulated dark web content source (in practice, replace with real API/data streams)
DARK_WEB_CONTENT = [
    "This is a harmless message.",
    "Credit card information leaked here!",
    "Another example of sensitive SSN detected.",
    'another example of social attack',
    "your gmail harshitha@gmail.com is unsafe",
    "Another example of sensitive phising detected.",
    "Another example of sensitive malware detected.",
    "Another example of sensitive virus detected.",
    "Another example of sensitive worms detected."
]

@app.route("/set_keywords", methods=["POST"])
def set_keywords():
    """Set custom keywords for monitoring."""
    global MONITORED_KEYWORDS
    keywords = request.json.get("keywords", [])
    MONITORED_KEYWORDS = keywords
    return jsonify({"message": "Keywords updated successfully.", "keywords": MONITORED_KEYWORDS})

@app.route("/monitor", methods=["GET"])
def monitor():
    """Monitor dark web content for specified keywords."""
    detected_alerts = []
    for content in DARK_WEB_CONTENT:
        for keyword in MONITORED_KEYWORDS:
            if keyword.lower() in content.lower():
                detected_alerts.append({"content": content, "keyword": keyword})

    return jsonify({"alerts": detected_alerts})

if __name__ == "__main__":
    print("DarkEye backend running...")
    app.run(debug=True)
