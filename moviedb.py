
from movie import Movie


class MovieDb:
    """
    This class represents all data for reviews for several movies
    ----instance variables----
    database: a list of Movie objects in the database
    """
    def __init__(self):
        # This constructor creates an empty database with no movies
        self.__database = list()

    def add_movie(self, title, year):
        """
        This method creates a new movie object and adds it to the database if it does not exist already.
        If it does exist, the method raises a KeyError.
        :param title: string - title of the movie
        :param year: string - year of the movie
        """
        movie_obj = Movie(title, year)
        for m in self.__database:
            if (movie_obj.get_title() == m.get_title) and (movie_obj.get_year() == m.get_year):
                raise KeyError("Duplicate movie!")
        self.__database.append(movie_obj)

    def find_movie(self, title, year):
        """
        This method finds and returns the movie object with the same name and year as input parameters
        :param title: title of the movie
        :param year: year of the movie
        :return: movie object
        """
        for m in self.__database:
            if (m.get_title() == title) and (m.get_year() == year):
                return m
        return None

    def show_all(self):
        """
        This method sorts all movies with title and prints all short reviews for all movies in the database
        """
        self.__database = sorted(self.__database, key=lambda x: x.get_title())

        # if some movies have the same title they will be sorted from the oldest to the newest
        for i in range(len(self.__database) - 1):
            if self.__database[i].get_title() == self.__database[i + 1].get_title():
                if int(self.__database[i].get_year()) > int(self.__database[i+1].get_year()):
                    temp = self.__database[i]
                    self.__database[i] = self.__database[i + 1]
                    self.__database[i + 1] = temp

        # prints all short reviews for all movies in the database
        for m in self.__database:
            print(m.short_review())
