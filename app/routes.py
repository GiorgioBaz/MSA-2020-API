from flask import render_template, request, redirect, url_for, jsonify
from app import app

# Task = models.Task

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/steam/', methods = ['GET'])
def getSteamGames():
    steamId = request.form.get('steamId')

    # getGames(steamId)
    return redirect(url_for('index'))

@app.route('/stats')
def add_stats():
    return render_template("stats.html")