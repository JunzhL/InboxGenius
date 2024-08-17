from flask import Flask, render_template
from flask_cors import CORS
from pymongo import MongoClient
import os
import certifi

def create_app():
    app = Flask(__name__)
    CORS(app)

    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    app.db = client[os.getenv('DATABASE')]

    # register routes
    from .routes.email_routes import email_routes

    app.register_blueprint(email_routes)

    @app.route("/")
    def index():
        return render_template("index.html", category="inbox")

    @app.route("/family")
    def family():
        return render_template("index.html", category="family")

    @app.route("/social")
    def social():
        return render_template("index.html", category="social")

    @app.route("/friends")
    def friends():
        return render_template("index.html", category="friends")

    @app.route("/work")
    def work():
        return render_template("index.html", category="work")

    return app
