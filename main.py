from game_recommendation import obtain_recommendation

game_list = []
number = int()
except_games = []


def local_user():
    while True:
        if len(game_list) < 5:
            game = input('Añade juegos a la lista, para mejorar la recomendacion')
            game_list.append(game)
        else:
            game = input('Añade juegos a la lista, para mejorar la recomendacion, para salir presiona enter')
            if game == '':
                break
            else:
                game_list.append(game)
                continue
    while True:
        game_exception = input('Añade juegos que no quieres obtener en la lista, para salir presiona enter')
        if game_exception == '':
            number = input('Number of recommendations')
            break
        except_games.append(game_exception)


if __name__ == '__main__':
    game_list= ['The witcher 3', 'Red Dead Redemption 2', 'Dragon Age Origins', 'Dragon Age Inquisition', 'Skyrim', 'Star Wars KOTOR']
    except_games = ['Assasins Creed', 'Dark Souls', 'Souls', 'Mass Effect', 'Mass Effect 2', 'Skyrim']
    number= 15
    print(obtain_recommendation(game_list, number, except_games))
