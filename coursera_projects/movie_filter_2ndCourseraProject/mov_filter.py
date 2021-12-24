import requests_with_caching
import json

def get_movies_from_tastedive(name):
    url = 'https://tastedive.com/api/similar'
    params = {'q': name, 'type': 'movies', 'limit': 5}
    data = requests_with_caching.get(url, params = params).text
    data_TDIVE = json.loads(data)
    return data_TDIVE
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")


def extract_movie_titles(movie_dict):
    titles = []
    for key in movie_dict['Similar']['Results']:
        titles.append(key['Name'])
    return titles
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))


def get_related_titles(titles_lst):
    titles_set = set()
    for title in titles_lst:
        for mov_title in extract_movie_titles(get_movies_from_tastedive(title)):
            titles_set.add(mov_title)
    return list(titles_set)
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])


def get_movie_data(movie_title):
    url = 'http://www.omdbapi.com/'
    params = {'t': movie_title, 'r': 'json'}
    data2 = requests_with_caching.get(url, params = params).text
    data_OMBD = json.loads(data2)
    return data_OMBD
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
    
    
def get_movie_rating(movie_dict):
    source_rate = 0
    for source in movie_dict['Ratings']:
        if 'Rotten Tomatoes' in source.values(): source_rate = int(source['Value'][:2])
    return source_rate
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))


def get_sorted_recommendations(mov_titles_lst):
    movies_dict = {}
    mov_titles = get_related_titles(mov_titles_lst)
    for title in mov_titles:
        movies_dict[title] = get_movie_rating(get_movie_data(title))
    sort_movies = sorted(movies_dict.items(), key = lambda x: (x[1], x[0]), reverse = True)
    sort_movies = [i[0] for i in sort_movies]
    return sort_movies
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


if '__main__' == __name__:
    print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))