from app import db, app
with app.app_context():
    db.drop_all()   # (optional, clears old broken DB)
    db.create_all()

