import sqlite3
import os
from movie import Movie


class DataManager:
        
    def __init__(self, db_path='data/database.db'):
        # testing db file existence and getting connected
        try:   
            directory = os.path.dirname(db_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            with open(db_path, 'w') as f:
                pass
            
        except:
            pass

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS movies_rating (
                movie_name TEXT,
                user_name TEXT,
                rating REAL
            )
        '''
        self.cursor.execute(query)
        self.conn.commit()

    def add_review(self,movie:Movie):
        query = '''
        INSERT OR IGNORE INTO movies_rating (movie_name,user_name,rating)
        VALUES(?,?,?)
        '''
        self.cursor.execute(query,(movie.get_movie_name(),movie.get_user_name(),movie.get_rating()))
        self.conn.commit()

    def delete_review(self,movie_name,user_name):
        query='''
        DELETE FROM movies_rating WHERE movie_name = ? and user_name = ?
        '''
        self.cursor.execute(query,(movie_name,user_name))

    def list_movies_rating(self):
        query = '''
        SELECT *
        FROM movies_rating
        '''
        self.cursor.execute(query)
        movies_rating = self.cursor.fetchall()
        return movies_rating
    
    def list_user_reviews(self,user_name):
        query = '''
        SELECT *
        FROM movies_rating
        WHERE user_name = ?
        '''
        self.cursor.execute(query,(user_name,))
        user_movies = self.cursor.fetchall()
        return user_movies
    
    def list_top_movies(self):
        query = '''
        SELECT movie_name, AVG(rating) as avg_rating
        FROM movies_rating
        GROUP BY movie_name
        ORDER BY avg_rating DESC
        LIMIT 10
        '''
        self.cursor.execute(query)
        top_movies = self.cursor.fetchall()
        return top_movies
    
    def close(self):
        self.connection.close()