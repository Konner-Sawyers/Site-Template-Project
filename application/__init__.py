from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def initialize():
    return render_template("index.html")