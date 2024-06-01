from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from config import db

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    serialize_rules = ('-user.reviews', '-user.instruments', '-user.purchases', '-user.id', '-purchases', '-instrument.reviews', '-instrument.id',)


    id=db.Column(db.Integer, primary_key=True)

    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    instrument_id=db.Column(db.Integer, db.ForeignKey('instruments.id'))
    purchase_id=db.Column(db.Integer, db.ForeignKey('purchases.id'))
    
    created_at=db.Column(db.DateTime)
    content=db.Column(db.String, default='')

    user = db.relationship('User', back_populates='reviews')
    purchases = db.relationship('Purchase', back_populates='review')
    instrument = db.relationship('Instrument', back_populates='reviews')