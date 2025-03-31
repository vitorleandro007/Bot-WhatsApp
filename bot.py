from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(_name_)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    reply = resp.message()

    if "oi" in incoming_msg:
        reply.body("Olá! Como posso te ajudar?")
    else:
        reply.body("Desculpe, não entendi.")

    return str(resp)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
