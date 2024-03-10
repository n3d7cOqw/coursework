from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kyrsova.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer(), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    addition_info = db.Column(db.String(256))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello')
def hello():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)