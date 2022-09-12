
class Movie:
    """
    This class represents the data associated with a movie
    ----instance variables----
    title: string - title of the movie
    year: string - year of the movie
    review: dictionary - key: number of stars in range1-5, values: the number of votes
    """

    # constants
    MIN_STARS = 1
    MAX_STARS = 5

    def __init__(self, title, year):
        """
        The constructor initializes the values for instance variables and creates a movie with no reviews
        :param title: string - title of the movie
        :param year: string - year of the movie
        """

        # instance variables
        self.__title = title
        self.__year = year
        self.__review = {}
        for i in range(Movie.MIN_STARS, Movie.MAX_STARS + 1):
            self.__review[i] = 0

    def add_review(self, vote):
        """
        This function accepts a single integer parameter that represents a new review
        :param vote: an integer
        """
        if Movie.MIN_STARS <= vote <= Movie.MAX_STARS:
            self.__review[vote] += 1

    def short_review(self):
        """
        This function represents a short description for a movie
        :return: a string representation of a movie object
        """
        return "{} ({}): {}".format(self.__title, self.__year, self.__calc_average())

    def long_review(self):
        """
        This function represents a long description for a movie
        :return: a string representation of a movie object
        """
        s = self.__title + " (" + self.__year + ")\n" + \
            "Average review: " + self.__calc_average() + '\n'
        for i in range(Movie.MAX_STARS, Movie.MIN_STARS - 1, -1):
            if i != Movie.MIN_STARS:
                s += ("*" * i) + (" " * (Movie.MAX_STARS - i)) + ": " + str(self.__review[i]) + "\n"
            else:
                s += ("*" * i) + (" " * (Movie.MAX_STARS - i)) + ": " + str(self.__review[i])
        return s

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __calc_average(self):
        """
        This method calculates the average review of a movie
        :return: average reviews of a movie
        """
        sum_votes = 0
        number_voters = 0
        for star, vote in self.__review.items():
            sum_votes += star * vote
            number_voters += vote
        if number_voters == 0:
            return "0.0/5"
        else:
            average_votes = sum_votes / number_voters
            return "{:.1f}/5".format(average_votes)
