
from moviedb import MovieDb

# constants
COMMAND = 0
TITLE = 1
YEAR = 2
REVIEW = 3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'


def read_file(input_file):
    """
    This function read the commands from input file
    :param input_file: information about the movies including their title, year of production and reviews
    """

    # make an object of MovieDb() class
    db = MovieDb()

    # make a dictionary of information about movies
    movie_dict = {}

    with open(input_file, 'r') as fh:
        # read the input file line by line
        for line in fh:
            data = line.strip().split('-')
            command = data[COMMAND]

            # create a new movie for the database if it does not exist
            if command == NEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                if db.find_movie(title, year) is None:
                    db.add_movie(title, year)
                    movie_dict[title] = [year, 0]

            # add review for a movie if it already exists in the database
            elif command == REVIEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                if db.find_movie(title, year) is not None:
                    db.find_movie(title, year).add_review(int(data[REVIEW]))
                    movie_dict[title][1] += 1

            # show the short version of the reviews for all movies in the database
            elif command == SHOW_COMMAND:
                db.show_all()

            # print the long version of the reviews for one movie in the database, if it exists
            elif command == PRINT_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                if db.find_movie(title, year) is not None:
                    print(db.find_movie(title, year).long_review())


def main():
    file_name = input("Enter the name of the file: ")
    read_file(file_name)


main()
