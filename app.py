from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///notes.db"
db = SQLAlchemy(app)


class notes(db.Model):
    title = db.Column(db.String(300),nullable=False,primary_key=True)
    note = db.Column(db.String(1000))

    def __repr__(self):
        return f"{self.title}-{self.note}"
with app.app_context():
    db.create_all()


def clear_database():
    # Delete all records from the 'notes' table
    with app.app_context():
        db.session.query(notes).delete()
        db.session.commit()
clear_database()


@app.route("/",methods=['GET','POST'])
def func():
    if request.method == 'POST':
        title = request.form['title']
        note = request.form['note']
        n1 = notes(title=title,note=note)
        db.session.add(n1)
        db.session.commit()
    allnote = notes.query.all()
    return render_template("index.html", allnote=allnote)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

