from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from config import db

class Instrument(db.Model, SerializerMixin):
    __tablename__ = 'instruments'

    serialize_rules = ('-users', '-purchases.instrument','-reviews.instrument',)

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    brand=db.Column(db.String, nullable=False)
    model=db.Column(db.String, nullable=False)
    size=db.Column(db.String, nullable=False)
    color=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    image=db.Column(db.String, nullable=False)

    sale_price=db.Column(db.Float)
    in_stock=db.Column(db.Boolean)

    reviews = db.relationship('Review', back_populates='instrument', cascade='all, delete-orphan')
    purchases = db.relationship('Purchase', back_populates='instrument', cascade='all, delete-orphan')
    users = db.relationship('User', secondary='purchases', back_populates='instruments')
