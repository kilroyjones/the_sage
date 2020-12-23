from flask import redirect, render_template, request, send_from_directory, url_for

from app import app


@app.route("/")
def home():
    return render_template('index.html') 