from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User   # <-- make sure your models.py is correct (shown below)

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ------------------ ROUTES ------------------ #
@app.route("/")
def home():
    return redirect(url_for('login'))   # safer than rendering login directly


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash("Email and Password are required!", "danger")
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash("⚠️ Email already registered.", "warning")
            return redirect(url_for('register'))

        # Hash password before saving
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=hashed_password)

        try:
            db.session.add(user)
            db.session.commit()
            flash("✅ Registration successful. Please log in.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f"❌ Database error: {str(e)}", "danger")

    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("❌ Invalid credentials", "danger")

    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("✅ You have been logged out.", "success")
    return redirect(url_for('login'))


# ------------------ MAIN ------------------ #
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

