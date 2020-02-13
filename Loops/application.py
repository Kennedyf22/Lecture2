from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    names=["Alice", "Bob", "Charlie", "Kennedy", "Jennifer", "Ingrid", "Otávio", "Matheus", "Paulo"]
    return render_template("names.html", names=names)
