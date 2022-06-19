from movies.adapter import adapt
from .movie_request import get_movies

#
# We apply Interface segregation by dividing all actions into smaller parts that are used form other functions/classes
#
# We also apply Open for Extension Closed for Modification, as we have everything in function only more functions or functionality can be added and 
# if anything needs to be changed is from classes themselves.
#
def movies_chain():
    soup = get_movies()
    # we use an adapter to make readable and usable information for our functions.
    adapt(soup)

    

    

if __name__ == '__main__':
    main()
