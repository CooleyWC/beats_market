from config import app, api, db, os
from flask_restful import Resource

from flask import Flask, jsonify, request, make_response, redirect


from models.users import User
from models.purchases import Purchase
from models.reviews import Review
from models.instruments import Instrument

from resources.users import Users
# from resources.signup import Signup
from resources.check_session import CheckSession
from resources.login import Login
from resources.logout import Logout
from resources.instruments import Instruments
from resources.reviews import Reviews
from resources.purchases import Purchases



api.add_resource(Users, '/api/users')
# api.add_resource(Signup, '/api/signup')
api.add_resource(CheckSession, '/api/check_session')
api.add_resource(Login, '/api/login')
api.add_resource(Logout, '/api/logout')
api.add_resource(Instruments, '/api/instruments')
api.add_resource(Reviews, '/api/reviews')
api.add_resource(Purchases, '/api/purchases')

if __name__ == "__main__":
  app.run(port=5555, debug=True)
