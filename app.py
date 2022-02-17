import os
import flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class FavMovies(db.model):
    """ creating database """
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)

db.create_all()

@app.route("/", methods = ["GET","POST"])
def index():
    """ creating index function """
    if flask.request.method == "POST":
        data = flask.request.form
        new_movie = FavMovies(
            title=data["title"],
        )
        db.session.add(new_movie)
        db.session.commit()

    if flask.request.method == "GET":
        data = flask.request.form
        
    movies = FavMovies.query.all()
    num_movies = len(movies)
    return flask.render_template("index.html", num_movies=num_movies, movies=movies)

app.run(
    debug = True
)
