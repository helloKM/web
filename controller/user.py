from flask import request, render_template, session, current_app
from model.user import User
import os
from werkzeug.utils import secure_filename
from model.user import db
import hashlib
from . import bp

app = current_app

@bp.route('/check_login', methods=['POST'])
def check_login():
    user_name = request.form['user_name']
    password = request.form['password']
    user = User.query.filter_by(user_name=user_name).first()
    if user == None:
        return '<script>alert("用户名或密码错误");location.href="/user/login"</script>'
    else:
        password = hashlib.md5((password + user.salt).encode('ascii')).hexdigest()
        if password == user.user_pwd:
            session['real_name'] = user.real_name
            session['user_num'] = user.user_num
            session['user_name'] = user.user_name
            return '<script>location.href="/user/welcome"</script>'
        else:
            return '<script>alert("用户名或密码错误");location.href="/user/login"</script>'


@bp.route('/check_signup', methods=['POST'])
def check_signup():
    user_name = request.form['user_name']
    email = request.form['email']
    phone = request.form['phone']
    real_name = request.form['real_name']
    password = request.form['password']
    ID_card_image = request.files['ID_card_image']
    permit_card_image = request.files['permit_card_image']
    ID_filename = secure_filename(ID_card_image.filename)
    permit_filename = secure_filename(permit_card_image.filename)
    ID_card_image.save(os.path.join(app.root_path, 'static/image/ID_card', ID_filename))
    permit_card_image.save(os.path.join(app.root_path, 'static/image/permit_card', permit_filename))
    u = User(user_name, password, phone, ID_filename, permit_filename, email, real_name=real_name)
    db.session.add(u)
    db.session.commit()
    return '<script>alert("注册成功!");location.href="/user/login"</script>'


@bp.route('/hey')
def hey():
    return '<script>alert("注册成功!");location.href="/user/login"</script>'


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/signup')
def signup():
    return render_template('create-account.html')


@bp.route('/welcome')
def welcome():
    print(session['user_name'])
    return render_template('home.html', name=session['real_name'])

@bp.route('/test')
def test():
    print(session['user_name'])
    return render_template('htmlTest.html', name=session['user_name'])
