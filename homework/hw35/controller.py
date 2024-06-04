from view import MovieInterface
from model import MovieModel


class Controller:
    def __init__(self):
        self.movie_module = MovieModel()
        self.movie_view = MovieInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.movie_view.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            movie = self.movie_view.add_movie()
            self.movie_module.add_movie(movie)
        elif answer == "2":
            movie = self.movie_module.get_all_movies()
            self.movie_view.show_all_movies(movie)
        elif answer == "3":
            movie_title = self.movie_view.get_movie()
            try:
                movie = self.movie_module.get_single_movie(movie_title)
            except KeyError:
                self.movie_view.incorrect_movie_error(movie_title)
            else:
                self.movie_view.show_single_movie(movie)
        elif answer == "4":
            movie_title = self.movie_view.get_movie()
            try:
                movie = self.movie_module.remove_movie(movie_title)
            except KeyError:
                self.movie_view.incorrect_movie_error(movie_title)
            else:
                self.movie_view.remove_single_movie(movie)
        elif answer == "q":
            self.movie_module.saved_data()
        else:
            self.movie_view.show_incorrect_answer_error(answer)
