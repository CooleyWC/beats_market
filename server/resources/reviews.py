from config import app, api, db
from flask_restful import Resource

from models.reviews import Review


class Reviews(Resource):
  def get(self):
    reviews = [review.to_dict() for review in Review.query.all()]
    return reviews, 200