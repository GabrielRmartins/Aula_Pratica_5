from db_manager import DataManager
from movie import Movie

def print_movie_list(movie_list):
    for movie in movie_list:
        movie_name,user_name,rating = movie
        print(f' User: {user_name} | Rating: {rating} | Movie: {movie_name}' )

def print_top_movies(top_movies_list):
    for movie in top_movies_list:
        movie_name,rating = movie
        print(f' Avarage Rating: {rating} | Movie: {movie_name}  ')

def print_menu():
    print('\n')
    print('1. Adicionar avaliação ao banco de dados')
    print('2. Listar minhas avaliações')
    print('3. Listar filmes mais bem avaliados')
    print('4. Sair')
    print('\n')

def add_review(db):
    try:
        movie_name = input('Digite o nome do filme: ')
        user_name = input('Digite o seu nome de usuário: ')
        rating = float(input('Digite a sua nota para o filme: '))
        db.add_review(Movie(movie_name,user_name,rating))
        print(f'Nova avaliação adicionada com sucesso!\n')
        input('Pressione qualquer tecla para voltar ao menu!')
    except:
        print('Falha ao adicionar nova avaliação, tente novamente!\n')
    

def list_user_reviews(db):

    user = input('Digite o seu nom de usuário: ')
    user_reviews = db.list_user_reviews(user)
    print_movie_list(user_reviews)
    print('\n')
    input('Pressione qualquer tecla para voltar ao menu!')

def list_top_movies(db):

    top_movies = db.list_top_movies()
    print_top_movies(top_movies)
    print('\n')
    input('Pressione qualquer tecla para voltar ao menu!')


def close_app(db):
    db.close()
    exit()

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