from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime

from movies.db.models import Movie, get_postgres_uri

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()
db = scoped_session(session)

def store_movies_postgre(movies):
    i = 0
    for movie in movies:
        m = Movie(movie_id = i, preference_key = movie["preference_key"], movie_title = movie["movie_title"], rating = movie["rating"], year = movie["year"], create_time = datetime.datetime.now())
        session.add(m)
        i += 1

    session.commit()    

    
    