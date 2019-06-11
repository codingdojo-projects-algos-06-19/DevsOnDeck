from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from config import db, bcrypt 


class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    languages = db.Column(db.String(255))
    bio = db.Column(db.Text)
    developer_id = db.Column(db.Integer, db.ForeignKey("developer.id"))
    developer = db.relationship('Developer', foreign_keys=[developer_id], backref="developer_skills", cascade='all') 
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


    @classmethod
    def skill_validation(cls, form):
        errors = []

        if len(form['bio']) < 10:
            errors.append("Please enter your bio!")

        return errors

    @classmethod
    def add_skill(cls, form, developer_id):
        skills = cls(
            languages=form['languages'],
            bio=form['bio'],
            developer_id = developer_id
        )
        db.session.add(skills)
        db.session.commit()


    @classmethod 
    def get_all_skills(cls):
        return cls.query.all()

    @classmethod
    def get_user_skills(cls, user_id):
        get_user_all_skills = cls.query.filter_by(user_id = user_id).all()
        return get_user_all_skills
    
    @classmethod 
    def get_skills(cls, skill_id):
        get_single_skill = cls.query.filter_by(id = skill_id).first()
        return get_single_skill

    @classmethod
    def delete_skills(cls, skill_id):
        get_single_skill = cls.query.get(skill_id)
        db.session.delete(get_single_skill)
        db.session.commit()


    @classmethod
    def edit_skills_info(cls, form, skill_id):
        skills_update = Skill.get(skill_id)
        skills_update.languages = form['languages']
        skills_update.bio = form['bio']
        db.session.commit()
        return skills_update