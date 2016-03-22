# coding=utf-8

from model import security
import hashlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ttkl1231@localhost:3306/web'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user_account'
    user_num = db.Column('user_num', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = db.Column('user_name', db.String(40), unique=True, nullable=False)
    user_pwd = db.Column('user_pwd', db.String(40), nullable=False)
    salt = db.Column('salt', db.String(16), nullable=False)
    phone = db.Column('phone', db.String(11), nullable=False)
    account_money = db.Column('account_money', db.DECIMAL(9, 2), nullable=False)
    email = db.Column('email', db.String(60))
    check_flag = db.Column('check_flag', db.Boolean, nullable=False)
    deposit = db.Column('deposit', db.DECIMAL(6, 2), nullable=False)
    pad_flag = db.Column('pad_flag', db.Boolean)
    real_name = db.Column('real_name', db.String(18))
    user_id = db.Column('user_id', db.String(20))
    card_pic = db.Column('card_pic', db.String(255))
    permit_pic = db.Column('permit_pic', db.String(255))
    car_num = db.Column('car_num', db.String(20))

    def __init__(self, user_name, password, phone, card_pic, permit_pic, email=None, user_id=None, real_name=None,
                 car_num=None):
        self.user_name = user_name
        self.salt = security.get_salt(16)
        self.user_pwd = hashlib.md5((password + self.salt).encode('ascii')).hexdigest()
        self.phone = phone
        self.account_money = 0
        self.email = email
        self.check_flag = False
        self.deposit = 0
        self.user_id = user_id
        self.real_name = real_name
        self.card_pic = card_pic
        self.permit_pic = permit_pic
        self.car_num = car_num

    def __repr__(self):
        return '<User %r>' % self.username
