from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from config import db, bcrypt
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Developer(db.Model):
    __tablename__ = "developer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr(self):
        return '<Developer{}>'.format(self.first_name)

    @classmethod
    def register_validation(cls, form):
        errors = []
        if len(form['first_name']) < 1:
            errors.append("Please enter your first name!")
        if len(form['last_name']) < 1:
            errors.append("Please enter your last name!")
        if not EMAIL_REGEX.match(form['email']):
            errors.append("Please enter valide Email!")
        
        existing_emails = cls.query.filter_by(email=form['email']).first()
        if existing_emails:
            errors.append("Email already registered!")

        if len(form['username']) < 1:
            errors.append("Please enter username")
        
        existing_username = cls.query.filter_by(username=form['username']).first()
        if existing_username:
            errors.append("Username is already exist")
        
        if len(form['password']) < 6:
            errors.append("Password must be at least 6 characters long!")
        if len(form['password']) != len(form['confirm_password']):
            errors.append("Passwords don't match")
        

        return errors

    @classmethod
    def create_developer(cls, form):
        pw_hash = bcrypt.generate_password_hash(form['password'])
        developer = cls(
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],
            username=form['username'],
            password=pw_hash,
        )
        db.session.add(developer)
        db.session.commit()
        return developer.id
    
    @classmethod
    def login_developer(cls, form):
        developer = cls.query.filter_by(email=form['email']).first()
        if developer:
            if bcrypt.check_password_hash(developer.password, form['password']):
                return (True, developer.id)
        return (False, "Email or password is incorrect")

    @classmethod 
    def get_all_developer(cls):
        return cls.query.all()

    @classmethod
    def get_developer(cls, developer_id):
        return cls.query.get(developer_id)
    
    @classmethod
    def edit_developer_info(cls, form, developer_id):
        dev_update = Developer.get(developer_id)
        dev_update.first_name = form['first_name']
        dev_update.last_name = form['last_name']
        dev_update.username = form['username']
        dev_update.password = form['password']
        db.session.commit()
        return dev_update