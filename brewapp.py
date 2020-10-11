from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Brewery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'x70-caQ0)9f5'
db = SQLAlchemy(app)

class Brew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String)

    def __repr__(self):
        return 'Comment %r' % self.id

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/about/', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/our_team/', methods=['GET'])
def our_team():
    return render_template("our_team.html")

@app.route('/alcohol/', methods=['GET'])
def alcohol():
    return render_template("alcohol.html")

@app.route('/menu/', methods=['GET'])
def menu():
    return render_template("menu.html")

@app.route('/store/', methods=['GET'])
def store():
    return render_template("store.html")

@app.route('/contact/', methods=['GET'])
def contact():
    return render_template("contact.html")

# function to add comments to SQLite DB
@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    date = str(datetime.today().replace(microsecond=0))

    if comment == "":
        return redirect('/contact/')
    else:
        entry = Brew(comment=comment, date=date)
        db.session.add(entry)
        db.session.commit()
        flash("Thank you for your feedback!")
        return redirect('/contact/')

@app.errorhandler(404)
def show_404(e):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
