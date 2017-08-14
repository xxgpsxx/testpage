from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    name = "George Sheng"
    return render_template("index.html", myName = name)


