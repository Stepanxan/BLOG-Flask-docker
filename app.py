from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:19982804@localhost:3306/posttitle'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "59ceec65a970fa3b1a00830e53081eb6f565c272"
db = SQLAlchemy(app)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.init_app(app)




with app.app_context():
     db.create_all()

with app.app_context():
    from routes.main import *
    from routes.registration import *
    from routes.login import *
    from routes.post import *
    from models.models import *




if __name__ == "__main__":
    app.run(debug=True)