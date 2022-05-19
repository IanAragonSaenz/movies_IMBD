from movies.movie_storer_csv import store_movies_csv
from movies.movie_storer_postgre import store_movies_postgre
from movies.adapter import adapt
from movies.movie_request import get_movies

#
# We apply Interface segregation by dividing all actions into smaller parts that are used form other functions/classes
#
# We also apply Open for Extension Closed for Modification, as we have everything in function only more functions or functionality can be added and 
# if anything needs to be changed is from classes themselves.
#
def main():
    soup = get_movies()
    # we use an adapter to make readable and usable information for our functions.
    movies = adapt(soup)

    #
    # we apply SRP from solid by separating both ways of saving the data, that way if one needs to be changed it will not affect the other
    #
    store_movies_csv(movies)
    store_movies_postgre(movies)

    

if __name__ == '__main__':
    main()
