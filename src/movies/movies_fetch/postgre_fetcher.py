from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime

from movies.db.models import Movie, get_postgres_uri
from .movie_fetcher import movies_chain

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()
#db = scoped_session(session)

def store_movies_postgre(key):

    movies = session.query(Movie).filter(Movie.preference_key == key).all() 
    return movies


def check_postgre():
    inspector = inspect(session.bind)

    if(inspector.has_table('movies') == False):
        movies_chain()
    else:
        movies = session.query(Movie).all() 
        if(len(movies) < 1):
            movies_chain()