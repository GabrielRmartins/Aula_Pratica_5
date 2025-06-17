
class Movie:

    def __init__(self,movie_name,user_name,rating):
        self.movie_name = movie_name
        self.user_name = user_name
        try:
            self.rating = float(rating)
            if not (0.0<=rating<=5.0):
                raise('ValueError: movie rating should be in the real interval [0.0,5.0]')
        except:
            raise('TypeError: movie rating should be a real number')

    def get_movie_name(self):
        return self.movie_name
    
    def get_user_name(self):
        return self.user_name
    
    def get_rating(self):
        return self.rating
    
        