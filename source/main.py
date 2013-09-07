import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html');

@app.route('/day/')
def day():
	return render_template('day.html');