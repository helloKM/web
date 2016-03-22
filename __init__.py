from flask import Flask
from controller.user import bp

app = Flask(__name__)
app.secret_key = 'PS#yio`%_!((f_or(%)))s'
app.register_blueprint(bp, url_prefix='/user')


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     str = request.args['abc']  # 获取GET或者POST中的参数
#     print(str)
#     return str
#
#
# @app.route('/htmlTest/')
# @app.route('/htmlTest/<sth>/')
# def htmlTest(sth=None):  # 模板
#     return render_template('htmlTest.html', name=sth)


if __name__ == '__main__':
    app.run(debug=True)
