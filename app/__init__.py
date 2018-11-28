from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


folder_path = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = 'uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#app.config["SQLALCHEMY_DATABASE_URI"] = f"""sqlite:///{os.path.join(folder_path, "my_database.db")}"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import models, stores
instructor_store = stores.InstructorStore()
instructor_course_store = stores.InstructorCourseStore()


from app import views


