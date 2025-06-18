
class Movie:

    def __init__(self, movie_name, user_name, rating):
        self.movie_name = movie_name
        self.user_name = user_name
        try:
            self.rating = float(rating)
        except:
            raise TypeError('A nota deve ser um número real entre 0 e 5.')

        if not (0.0 <= self.rating <= 5.0):
            raise ValueError('A nota deve estar no intervalo entre 0 e 5.')

    def get_movie_name(self):
        return self.movie_name
    
    def get_user_name(self):
        return self.user_name
    
    def get_rating(self):
        return self.rating
    
        