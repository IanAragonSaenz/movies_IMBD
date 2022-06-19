from movies.movies_fetch.postgre_fetcher import check_postgre
from .movie_get_csv import get_movies_csv


# This Facade fetches the full list of movies and returns the html code of the 5 movies based on the user preference key

class MoviesFacade:

    def save_movies(self):
        check_postgre()
    

    def get_movies(self, file_path, preference_key, is_sorted):
        return get_movies_csv(file_path, preference_key, is_sorted)