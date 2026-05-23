from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8884623458:AAHUEQHTCDCnvcMtwAQ4YiA5MBBKStSkPsQ"
CHAT_ID = "1003993482701"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    msg = data.get("message", str(data))
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
    )
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
