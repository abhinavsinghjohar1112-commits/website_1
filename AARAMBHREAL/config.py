import os

class Config:
    SECRET_KEY = 'your_secret_key'

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload folder (for images, PDFs, etc.)
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')