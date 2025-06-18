import pytest 
from src.movie import Movie

@pytest.fixture
def movie_sample():
    movie_name = 'test_movie'
    user_name = 'test_user'
    rating = 3

    return Movie(movie_name,user_name,rating)

def test_create_movie(movie_sample):

    assert movie_sample != None

def test_create_movie_with_invalid_rating_type():
    movie_name = 'test_movie'
    user_name = 'test_user'
    rating = 'test'

    with pytest.raises(TypeError,match='A nota deve ser um número real entre 0 e 5.'):
        Movie(movie_name,user_name,rating)

def test_create_movie_with_invalid_rating_range():
    movie_name = 'test_movie'
    user_name = 'test_user'
    rating = 7

    with pytest.raises(ValueError,match='A nota deve estar no intervalo entre 0 e 5.'):
        Movie(movie_name,user_name,rating)

def test_get_movie_name(movie_sample):

    assert movie_sample.get_movie_name() == 'test_movie'

def test_get_movie_user_name(movie_sample):

    assert movie_sample.get_user_name() == 'test_user'

def test_get_movie_rating(movie_sample):

    assert movie_sample.get_rating() == 3
    