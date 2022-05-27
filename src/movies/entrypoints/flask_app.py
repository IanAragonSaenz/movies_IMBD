from flask import Flask, request
from movies import models
from flask import render_template

from movies.postgre_fetcher import store_movies_postgre, check_postgre

app = Flask(__name__)
models.start_mappers()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "hello", 200

@app.route("/", methods=["GET"])
def home(name=None):
    check_postgre()
    return render_template('home.html', name=name)


@app.route("/movies", methods=["POST"])
def movies(name=None):
    category_value = {'comedy' : 1, 'drama' : 2, 'sci-fi' : 3, 'romantic' : 4, 'adventure' : 5}

    category1 = category_value[request.form['category1']]
    category2 = category_value[request.form['category2']]
    category3 = category_value[request.form['category3']]

    sorted = request.form['rated']

    preference_key = category1 * category2 * category3 % 5 + 1

    movies = store_movies_postgre(preference_key)

    return 'troll' 