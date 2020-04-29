from lib.globals import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy import create_engine

db = SQLAlchemy()

# How do we want to model our application?

# 1.  There needs to be some place that stores the current values of stocks. 
#     Though it doesn't seem necessary, we will probably need access to it sometime


class Corporation(db.Model):
    __tablename__ = 'corporations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    symbol = db.Column(db.Text, unique=True, nullable=False)

    stocks = db.relationship('Stock')


class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    corporation_id = db.Column(db.Integer, db.ForeignKey('corporations.id'), nullable=False)
    closing_value = db.Column(db.Float, nullable=False)
    highest_value = db.Column(db.Float, nullable=False)
    day_prediction_value = db.Column(db.Float, nullable=False)
    week_prediction_value = db.Column(db.Float, nullable=False)
    month_prediction_value = db.Column(db.Float, nullable=False)
    record_date = db.Column(db.Date)

    corporation = db.relationship('Corporation', foreign_keys=corporation_id)

# class Atricle(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text, unique=True, nullable=False)
#     symbol = db.Column(db.Text, unique=True, nullable=False)
#     date = db.Column(db.DateTime)
    

def get_new_connection(echo=False) -> session.Session:
    engine = create_engine(config['SQLALCHEMY_DATABASE_URI'], echo=echo)
    connection = sessionmaker(bind=engine)
    session = connection()
    return session