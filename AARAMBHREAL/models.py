from flask_sqlalchemy import SQLAlchemy

# Create db object
db = SQLAlchemy()

# Property Table
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    price = db.Column(db.String(50))
    status = db.Column(db.String(20))  # Available / Sold
    description = db.Column(db.Text)
    image = db.Column(db.String(200))
    video = db.Column(db.String(300))

# Lead Table (for user registrations)
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))