from flask import Flask, render_template
from flask_cors import CORS
from pymongo import MongoClient
import os
import certifi
from dotenv import load_dotenv


from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

load_dotenv()

# Dummy user data
class User(UserMixin):
    pass

users = {
    'demo@hack.com': {'password': 'ignition'}
}

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.secret_key = 'your_secret_key'

    # Setup Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    client = MongoClient(os.getenv('MONGO_URI'), tlsCAFile=certifi.where())
    app.db = client[os.getenv('DATABASE')]

    # register routes
    from .routes.email_routes import email_routes

    app.register_blueprint(email_routes)

    @app.route("/")
    @login_required # TODO: Uncomment this line to require login
    def index():
        return render_template("index.html", category="inbox")

    @app.route("/family")
    @login_required
    def family():
        return render_template("index.html", category="family")

    @app.route("/social")
    @login_required
    def social():
        return render_template("index.html", category="social")

    @app.route("/friends")
    @login_required
    def friends():
        return render_template("index.html", category="friends")

    @app.route("/work")
    @login_required
    def work():
        return render_template("index.html", category="work")

    @app.route("/other")
    @login_required
    def other():
        return render_template("index.html", category="other")
    
    @login_manager.user_loader
    def user_loader(email):
        if email not in users:
            return None
        user = User()
        user.id = email
        return user

    @login_manager.request_loader
    def request_loader(request):
        email = request.form.get('email')
        if email not in users:
            return None
        user = User()
        user.id = email
        user.is_authenticated = request.form['password'] == users[email]['password']
        return user

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            if email in users and request.form['password'] == users[email]['password']:
                user = User()
                user.id = email
                login_user(user)
                return redirect(url_for('index'))
            flash('Invalid credentials', 'danger')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    return app


