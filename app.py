from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "8884623458:AAFNrLnIgvj8dAa_YPcFxlEJnIsUjxPdocE"
CHAT_ID = "-1003993482701"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        msg = data.get("text") or data.get("message") or str(data)
    except:
        msg = request.data.decode("utf-8")
    
    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
    )
    print(f"Telegram response: {response.status_code} - {response.text}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
