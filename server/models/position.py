from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from config import db, bcrypt 


class Position(db.Model):
    __tablename__ = "positions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    organization_id = db.Column(db.Integer, db.ForeignKey("organization.id"), nullable=False)
    organization = db.relationship('Organization', foreign_keys=[organization_id], backref="organization_positions", cascade='all')
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


    @classmethod
    def position_validation(cls, form):
        errors = []

        if len(form['name']) < 1:
            errors.append("Please fill out name!")

        if len(form['description']) < 1:
            errors.append("Please fill out description!")

        return errors

    @classmethod
    def add_position(cls, form, organization_id):
        positions = cls(
            name=form['name'],
            description=form['description'],
            organization_id = organization_id
        )
        db.session.add(positions)
        db.session.commit()

    @classmethod 
    def get_all_positions(cls):
        return cls.query.all()

    @classmethod
    def get_user_positions(cls, user_id):
        get_user_all_positions = cls.query.filter_by(user_id = user_id).all()
        return get_user_all_positions
    
    @classmethod 
    def get_positions(cls, position_id):
        get_single_position = cls.query.filter_by(id = position_id).first()
        return get_single_position

    @classmethod
    def delete_positions(cls, position_id):
        get_single_position = cls.query.get(position_id)
        db.session.delete(get_single_position)
        db.session.commit()

        
    @classmethod
    def edit_positions_info(cls, form, position_id):
        positions_update = Position.get(position_id)
        positions_update.name = form['name']
        positions_update.description = form['description']
        db.session.commit()
        return positions_update