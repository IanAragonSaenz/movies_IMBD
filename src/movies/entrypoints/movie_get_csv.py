import csv

def get_movies_csv(file_path, preference_key, is_sorted):
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        movies = list(filter(lambda m : int(m[0]) == preference_key, data[1:]))

        print("mis peliculas", movies)
        res_list = movies[0:5]
        print("ordenados?", is_sorted)
        if is_sorted == 'yes':
            res_list.sort(key=lambda x : x[3], reverse=False)

        s = ''
        print(res_list)
        for m in res_list:
            s += '<li>' + m[1] + '</li>'

        return '<ol>' + s + '</ol>'