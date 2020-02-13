from flask import Flask
app= Flask(__name__)
@app.route("/")
def index():
    return "Hello, world!"
@app.route("/kennedy")
def kennedy():
    return "Hello, Kennedy!"
@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return f"Hello, {name}!"
from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def index():
    headline="Hello!"
    return render_template("index.html", headline=headline)
@app.route("/bye")
def bye():
    headline="Goodbye!"
    return render_template("index.html", headline=headline)
    