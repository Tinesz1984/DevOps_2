from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    message = os.getenv("APP_MESSAGE", "hello world")
    return f"{message}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
