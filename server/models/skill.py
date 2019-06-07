from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from config import db, bcrypt 


class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr(self):
        return '<Organization{}>'.format(self.organization)

    @classmethod
    def register_validation(cls, form):
        errors = []

        if not EMAIL_REGEX.match(form['email']):
            errors.append("Please enter valide Email!")
        
        existing_emails = cls.query.filter_by(email=form['email']).first()
        if existing_emails:
            errors.append("Email already registered!")

        if len(form['organization']) < 1:
            errors.append("Please enter your organization!")

        existing_organization = cls.query.filter_by(organization=form['organization']).first()
        if existing_organization:
            errors.append("Organization is already exist")
        
        if len(form['password']) < 6:
            errors.append("Password must be at least 6 characters long!")
        if password!=confirm_password:
            errors.append("Passwords don't match")
        
        return errors

    @classmethod
    def register_organization(cls, form):
        pw_hash = bcrypt.generate_password_hash(form['password'])
        organization = cls(
            email=form['email'],
            organization=form['organization'],
            password=pw_hash,
        )
        db.session.add(organization)
        db.session.commit()
        return organization.id
    
    @classmethod
    def login_organization(cls, form):
        organization = cls.query.filter_by(email=form['email']).first()
        if organization:
            if bcrypt.check_password_hash(organization.pw_hash, form['password']):
                return (True, organization.id)
        return (False, "Email or password is incorrect")

    @classmethod 
    def get_all_organization(cls):
        return cls.query.all()

    @classmethod
    def get_organization(cls, organization_id):
        return cls.query.get(organization_id)
    
    @classmethod
    def edit_organization_info(cls, form, organization_id):
        org_update = Organization.get(organization_id)
        org_update.organization = form['organization']
        org_update.password = form['password']
        db.session.commit()
        return org_update