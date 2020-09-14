from flask import render_template
from app import app

#Home Page Route
@app.route('/')
def index():
    return render_template("index.html")

#Stats Page Route
@app.route('/stats')
def add_stats():
    return render_template("stats.html")