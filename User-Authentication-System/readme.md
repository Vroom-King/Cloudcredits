# 🔐 User Authentication System (Flask + SQLAlchemy)

A simple and secure user authentication system built with **Flask**, **Flask-Login**, **Flask-Bcrypt**, and **SQLAlchemy**.  
It allows users to **register, log in, log out**, and access a **protected dashboard**.

---

## 📌 Features
- ✅ User Registration (with hashed password storage)
- ✅ Secure Login & Logout
- ✅ Session Management with `Flask-Login`
- ✅ Password hashing using `Flask-Bcrypt`
- ✅ SQLite Database with SQLAlchemy ORM
- ✅ Protected Dashboard (only for logged-in users)

---

## 🛠️ Tech Stack
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

---

## 📂 Project Structure
User-Auth-System/
│── app.py # Main application
│── models.py # Database models (User model)
│── users.db # SQLite database (auto-created)
│── requirements.txt # Python dependencies
│── /templates # HTML templates
│ ├── login.html
│ ├── register.html
│ └── dashboard.html


---

## ⚡ Installation & Setup

1️⃣ Clone the repo:
```bash
git clone https://github.com/yourusername/User-Auth-System.git
cd User-Auth-System
```

2️⃣ Create virtual environment:
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3️⃣ Install dependencies:
```
pip install -r requirements.txt
```
4️⃣ Initialize the database:

run databse.py to recreate users.db file
```
python database.py
```

5️⃣ Run the server:

```
python -m flask run --debug
```

6️⃣ Open in browser:

http://127.0.0.1:5000


🔑 Default Pages

/register → Register new user

/login → Login with credentials

/dashboard → Protected page (login required)

/logout → Logout
