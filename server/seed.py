from config import app, db
from faker import Faker
from models.users import User
from models.purchases import Purchase
from models.reviews import Review
from models.instruments import Instrument
from datetime import datetime, date

if __name__ == "__main__":
  with app.app_context():
    print('starting seed...')

    User.query.delete()
    Purchase.query.delete()
    Review.query.delete()
    Instrument.query.delete()

    fake = Faker()

    print('adding users')
    user_1 = User(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), location=fake.city(), admin=False)
    user_1.password_hash='paradiddle'
    user_2 = User(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), location=fake.city(), admin=False)
    user_2.password_hash='paradiddle'
    user_3 = User(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), location=fake.city(), admin=False)
    user_3.password_hash='paradiddle'
    user_4 = User(first_name='will', last_name='cool', email='will@gmail.com', location='chicago', admin=True)
    user_4.password_hash='paradiddle'

    db.session.add_all([user_1, user_2, user_3, user_4])
    db.session.commit()

    print('adding instruments...')
    instrument_1 = Instrument(name='Snare Drum', brand='Pearl', model='Philharmonic', size='14x5', color='Maple', description=fake.paragraph(nb_sentences=5), image='https://images.unsplash.com/photo-1626962131658-603aae425e19?q=80&w=3560&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', sale_price=400, in_stock=True)
    instrument_2 = Instrument(name='Marimba', brand='Marimba One', model='Standard', size='5 Octave', color='Natural Wood', description=fake.paragraph(nb_sentences=5), image='https://images.unsplash.com/photo-1635737775897-cbc4c19a697d?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bWFyaW1iYXxlbnwwfHwwfHx8MA%3D%3D', sale_price=12000, in_stock=True)
    instrument_3 = Instrument(name='Tambourine', brand='Black Swamp', model='German Silver', size='10in', color='Natural Wood', description=fake.paragraph(nb_sentences=5), image='https://plus.unsplash.com/premium_photo-1702552106545-feef7cbecfe0?q=80&w=3540&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', sale_price=400, in_stock=True)
    instrument_4 = Instrument(name='Triangle', brand='Alan Abel', model='Alan Abel', size='9in', color='silver', description=fake.paragraph(nb_sentences=5), image='https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?q=80&w=3655&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', sale_price=5000075, in_stock=True)


    db.session.add_all([instrument_1, instrument_2, instrument_3, instrument_4])
    db.session.commit()

    print('adding purchases...')

    purchase_1 = Purchase(user_id=1, instrument_id=1, created_at=datetime(2024,3,1,10,10,10))
    purchase_2 = Purchase(user_id=2, instrument_id=2, created_at=datetime(2024,5,10,11,1,0))
    purchase_3 = Purchase(user_id=3, instrument_id=3, created_at=datetime(2024,6,3,11,5,0))
    purchase_4 = Purchase(user_id=2, instrument_id=4, created_at=datetime(2024,5,11,10,1,0))

    db.session.add_all([purchase_1, purchase_2, purchase_3, purchase_4])
    db.session.commit()

    print('adding reviews')

    review_1 = Review(user_id=1, instrument_id=1, purchase_id=1, created_at=datetime(2024,8,10,10,10,0), content=fake.paragraph(nb_sentences=5))
    review_2 = Review(user_id=2, instrument_id=2, purchase_id=2, created_at=datetime(2024,8,10,10,10,0), content=fake.paragraph(nb_sentences=5))
    review_3 = Review(user_id=2, instrument_id=4, purchase_id=4, created_at=datetime(2024,9,10,10,10,0), content=fake.paragraph(nb_sentences=5))


    db.session.add_all([review_1, review_2, review_3])
    db.session.commit()