import pickle
import os.path


class Movie:
    def __init__(self, name, genre, director, year, direction, studio, actors):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.direction = direction
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.name} ({self.director})"


class MovieModel:
    def __init__(self):
        self.db_name = "movies.txt"
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.name] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, user_movie):
        movie = self.movies[user_movie]
        dict_movie = {
            "название": movie.name,
            "жанр": movie.genre,
            "режиссер": movie.director,
            "год выпуска": movie.year,
            "длительность": movie.direction,
            "студия": movie.studio,
            "актеры": movie.actors
        }
        return dict_movie

    def remove_movie(self, user_movie):
        return self.movies.pop(user_movie)

    def saved_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.movies, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
