from website import create_app
from flask import Flask, request, jsonify

app = create_app()

@app.route("/get-convo/<user_id>")
def get_user(user_id):
    convo = {
        "user_id": user_id,
        "name": "Alp Serin",
        "email": "alpsrn@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        convo['extra'] = extra

    return jsonify(convo), 200

# We want to only run the server IF we run this file directly. If we didn't do this, we would run the server whenever we imported this file.
if __name__ == '__main__':
    app.run(debug=True)