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

def print_menu():
    print('1. Adicionar avaliação ao banco de dados')
    print('2. Listar minhas avaliações')
    print('3. Listar filmes mais bem avaliados')
    print('4. Sair')

def add_review(db):
    pass

def list_user_reviews(db):
    pass

def list_top_movies(db):
    pass

def close_app(db):
    pass

def interface(db):

    while(1):
        print_menu()
        try:
            option = int (input('Digite a opção desejada(Ex.: \'1\' para Adicionar avaliação ao banco de dados): '))
        except:
            raise(TypeError('Digite um número inteiro para identificação do comando'))
            continue
        if option == 1:
            add_review(db)
        elif option == 2:
            list_user_reviews(db)
        elif option == 3 :
            list_top_movies(db)
        elif option == 4:
            close_app(db)
        else:
            raise(ValueError('Comando inválido'))
            continue
        


if __name__ == '__main__':
    db = DataManager()
    interface(db)