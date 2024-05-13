from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "jirewrlwerkm"
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
    records = User.query.order_by(User.id).all()

    return render_template("index.html", records=records)


@app.route('/store-record', methods=["POST"])
def store_record():
    if request.method == "POST":
        name = request.form['name']
        surname = request.form['surname']
        phone_number = request.form['phone_number']
        address = request.form['address']
        add_info = request.form['add_info']

        if(len(name) > 3 and len(surname) > 3 and len(phone_number) >10 and len(address) > 3):
            user = User(name=name, surname=surname, phone_number=phone_number, address=address, addition_info=add_info)



        try:
            db.session.add(user)
            db.session.commit()
            flash('Новий контакт успішно додано', 'success')
            return redirect("/")
        except:
            flash("Сталася помилка при валідації нового контакту. Заповніть поля коректно", "danger")

    return redirect("/")


@app.route('/edit-record/<int:record_id>')
def edit_record(record_id):
    user = User.query.get_or_404(record_id)
    return render_template("edit_record.html", user=user)

@app.route('/update-record/<int:record_id>', methods=['POST'])
def update_record(record_id):
    user = User.query.get_or_404(record_id)
    if (len(request.form['name']) > 3 and len(request.form['surname']) > 3 and len(request.form['phone_number']) > 10 and len(request.form['add_info']) > 3):
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.phone_number = request.form['phone_number']
        user.address = request.form['address']
        user.addition_info = request.form['add_info']
        db.session.commit()
        flash('Контакт успішно оновлено', 'success')
        return redirect("/")
    else:
        flash('Помилка валідації', 'danger')
        return redirect(request.referrer or "/")

@app.route('/delete-record/<int:record_id>', methods=['POST'])
def delete_record(record_id):
    user = User.query.get_or_404(record_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=False)
