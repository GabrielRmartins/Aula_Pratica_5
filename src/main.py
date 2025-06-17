from db_manager import DataManager
from movie import Movie

def print_movie_list(movie_list):
    for movie in movie_list:
        movie_name,user_name,rating = movie
        print(f'Movie: {movie_name} | User: {user_name} | Rating: {rating}')

def print_top_movies(top_movies_list):
    for movie in top_movies_list:
        movie_name,rating = movie
        print(f'Movie: {movie_name} | Avarage Rating: {rating}')

db = DataManager()

movie = Movie('movie_test','user_test',3)
movie2 = Movie('movie2','user_test',4)
movie3 = Movie('movie3','user_test',2.5)
movie4 = Movie('movie2','user_test2',3)
db.add_review(movie)
db.add_review(movie2)
db.delete_review(movie.get_movie_name(),movie.get_user_name())
db.add_review(movie3)
db.add_review(movie4)
all_movies = db.list_movies_rating()
user_reviews = db.list_user_reviews('user_test')
top_movies = db.list_top_movies()
print_top_movies(top_movies)