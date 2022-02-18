""" importing libraries """
import os
import flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class FavMovies(db.Model):
    """ creating database """
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)

db.create_all()

@app.route("/", methods = ["GET","POST"])
def index():
    """ main index """
    movies = FavMovies.query.all()
    num_movies = len(movies)
    return flask.render_template("index.html", num_movies=num_movies, movies=movies)

@app.route("/added", methods = ["GET","POST"])
def index2():
    """ creating index function """
    if flask.request.method == "POST":
        data = flask.request.form
        new_movie = FavMovies(title=data["title"])
        if FavMovies.query.filter_by(title=data["title"]).first() is None:
            db.session.add(new_movie)
            db.session.commit()
        return flask.redirect("/")

@app.route("/deleted", methods = ["GET","POST"])
def index3():
    """ creating index function """
    if flask.request.method == "POST":
        data = flask.request.form
        deletion = FavMovies.query.filter_by(title=data["title"]).first()
        if FavMovies.query.filter_by(title=data["title"]).first() is not None:
            db.session.delete(deletion)
            db.session.commit()
        return flask.redirect("/")

app.run(
    debug = True
)
