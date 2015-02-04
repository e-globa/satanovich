# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap


def create_app():

    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def index():
        return 'Hello World!'

    @app.route('/favicon.ico')
    def favicon():
        return redirect(url_for('static', filename='favicon.ico'))

    return app
