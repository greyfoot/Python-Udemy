MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def accept_input():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


# Create other functions for:
#   - listing movies
def list_movies():
    for movie in movies:
        print_movie(movie)


#   - finding movies
def find_movies():
    search = input("Enter the name of the movie you want to search: ")
    for movie in movies:
        if movie['title'] == search:
            print_movie(movie)


selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        accept_input()
    elif selection == "l":
        list_movies()
    elif selection == "f":
        find_movies()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)

