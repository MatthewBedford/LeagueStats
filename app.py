import requests
import sqlite3
from flask import Flask, render_template, request, send_from_directory
from werkzeug.exceptions import abort

def get_champdb_connection():
    conn = sqlite3.connect('champ.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__, static_url_path='')

@app.route('/')
def base():
    return render_template('homepage.html')

@app.route('/champIcons/<path:path>')
def send_icon(path):
    return send_from_directory('static/champImages', path)

@app.route('/champDatabase')
def champDatabaseOutput():
    conn = get_champdb_connection()
    champions = conn.execute('SELECT * FROM champions').fetchall()
    conn.close()
    return render_template('champions.html', champions=champions)

@app.route('/rotation')
def rotation():
    return render_template('champRotations.html')

@app.route('/freeRotation')
def freeRotation():
    conn = get_champdb_connection()

    r = requests.get("https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=RGAPI-96ab15bd-de0b-4d65-8563-158811931975")
    r = r.json()

    champions = []

    for inputID in r['freeChampionIds']:
        champions += conn.execute(f'SELECT * FROM champions WHERE champID="{inputID}"').fetchall()

    conn.close()
    return render_template('champions.html', champions=champions)

@app.route('/freeRotationNewPlayers')
def freeRotationNew():
    conn = get_champdb_connection()

    r = requests.get("https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=RGAPI-96ab15bd-de0b-4d65-8563-158811931975")
    r = r.json()

    champions = []

    for inputID in r['freeChampionIdsForNewPlayers']:
        champions += conn.execute(f'SELECT * FROM champions WHERE champID="{inputID}"').fetchall()

    conn.close()
    return render_template('champions.html', champions=champions)