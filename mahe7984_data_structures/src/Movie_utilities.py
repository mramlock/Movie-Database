"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Ahmed Maher
ID:      169037984
Email:   mahe7984@mylaurier.ca
__updated__ = "2023-01-31"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    # Your code here
    title = input('Title: ')
    year = int(input('Year of release: '))
    director = input('Director: ')
    rating = float(input('Rating: '))
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    # Your code here
    list = line.split("|")
    title = list[0]
    year = int(list[1])
    director = list[2]
    rating = float(list[3])
    genre_codes = list[4].split(',')
    genres = []
    for i in range(len(genre_codes)):
        genres.append(int(genre_codes[i]))
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    movies = []
    lines = fv.readlines()
    for i in range(len(lines)):
        movie = read_movie(lines[i])
        movies.append(movie)

    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    # Your code here
    print(Movie.genres_menu())
    genres = []
    genre = input("Enter a genre number (ENTER to quit): ")
    while genre == '':
        print('Error: must have at least one genre')
        genre = input("Enter a genre number (ENTER to quit): ")
    while genre != '':
        if genre.isdigit():
            genre_num = int(genre)
            if int(genre) > len(Movie.GENRES):
                print('Error: input must be <= ' + str(len(Movie.GENRES)))
            elif genre_num in genres:
                print("Error: Genre already chosen.")
            else:
                genres.append(genre_num)
        else:
            print('Error: not a positive number')
        genre = input("Enter a genre number (ENTER to quit): ")
    genres.sort()
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    ymovies = []
    for i in movies:
        if i.year == year:
            ymovies.append(i)
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    rmovies = []
    for i in movies:
        if i.rating >= rating:
            rmovies.append(i)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    gmovies = []
    for i in movies:
        if genre in i.genres:
            gmovies.append(i)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    gmovies = []
    for i in movies:
        if i.genres == genres:
            gmovies.append(i)
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """

    # Your code here
    counts = []
    i = 0
    while i <= len(Movie.GENRES):
        genre_number = 0
        for j in movies:
            if i in j.genres:
                genre_number += 1
        counts.append(genre_number)
        i += 1
    return counts
