from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hey, babe this is sultan!</h1>"

app.run()