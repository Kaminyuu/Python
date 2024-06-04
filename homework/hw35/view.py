def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap

    return wrapper


class MovieInterface:
    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        print("Действие с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма")
    def add_movie(self):
        dict_movie = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key} фильма: ")
        return dict_movie

    @add_title("Каталог фильмов")
    def show_all_movies(self, movies):
        for ind, movie in enumerate(movies, 1):
            print(f"{ind}. {movie}")

    @add_title("Ввод названия фильма")
    def get_movie(self):
        user_movie = input("Введите название фильма: ")
        return user_movie

    @add_title("Просмотр определенного фильма")
    def show_single_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @add_title("Сообщение об ошибке")
    def incorrect_movie_error(self, incorrect_movie):
        print(f"Фильма с название {incorrect_movie} не существует")

    @add_title("Удаление фильма")
    def remove_single_movie(self, removed_movie):
        print(f"Фильм {removed_movie} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")
