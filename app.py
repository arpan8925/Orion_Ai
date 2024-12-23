from flask import Flask, request, render_template, redirect, url_for, jsonify, session
import os


app = Flask(__name__)
app.secret_key = "arpandeyflaskformorionai"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)