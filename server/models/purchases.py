from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from config import db


class Purchase(db.Model, SerializerMixin):
    __tablename__ = 'purchases'

    serialize_rules = ('-user.rentals', '-user.reviews', '-user.instruments', 
                       '-instrument.rentals', '-instrument.reviews', '-review',)

    id=db.Column(db.Integer, primary_key=True)

    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    instrument_id=db.Column(db.Integer, db.ForeignKey('instruments.id'))

    created_at=db.Column(db.DateTime)

    user = db.relationship('User', back_populates='purchases')
    instrument = db.relationship('Instrument', back_populates='purchases')
    review = db.relationship('Review', back_populates='purchases', cascade='all, delete-orphan')

    def __repr__(self):
        user=self.user.username if self.user else None
        instrument=self.instrument.name if self.instrument else None
        return f'<Purchase {user}: {instrument}'