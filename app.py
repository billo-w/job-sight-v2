from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/register/')
def register():
    return render_template("register.html")