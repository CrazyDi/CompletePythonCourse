"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit:

- Add  movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[x]: Decide where to store movies
[]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[]: Stop running the program when they type 'q'
"""

MOVIES = []

"""
movie = {
    'name': ... (str),
    'director': ... (str),
    'year': ... (int)
}
"""


def add_movie():
    name = input("Enter a name of movie: ")
    director = input("Enter a director of movie: ")
    year = int(input("Enter a year of movie: "))

    movie = {'name': name, 'director': director, 'year': year}
    MOVIES.append(movie)
    print("Movie added correctly!")


def show_movies():
    for movie in MOVIES:
        print(f"Movie: {movie['name']} created in {movie['year']} by {movie['director']}")


def find_movie():
    find_type = input("What property of the movie is that? ")
    looking_for = input("What are you looking for? ")

    for movie in MOVIES:
        if movie[find_type] == looking_for:
            print(f"Movie: {movie['name']} created in {movie['year']} by {movie['director']}")


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command - please try again.")

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ")


menu()