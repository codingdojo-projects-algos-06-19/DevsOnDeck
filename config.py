from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
bcrypt=Bcrypt(app)
app.secret_key="portfolionumberone"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///getyou.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ROOT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'client', 'templates')
STATIC_DIR = os.path.join(ROOT_DIR, 'client', 'static')

app.template_folder = TEMPLATES_DIR
app.static_folder = STATIC_DIR

db = SQLAlchemy(app)
migrate = Migrate(app, db)