from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    msg = data.get("text") or data.get("message") or str(data)
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
    )
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
