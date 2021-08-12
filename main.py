def intro():
    print("""Hello, Welcome to MOVIE DATA STORAGE
What task would like to perform now

Press 1 to ADD a movie into storage ;
Press 2 to VIEW your current storage;
Press 3 to SEARCH a specific movie from storage;
Press 4 to QUIT
    
:)    
""")


intro()


option = int(input("Enter the number here: "))


movies = []


def add_movie():
    name = input("Enter the name of movie: ")
    director = input("Enter the name of director: ")
    year = input("Enter the year of release of the movie: ")

    movies.append({
        "name": name,
        "director": director,
        "year": year
    })


def view_movie():
    for movie in movies:
        print(f'The name of movie is {movie["name"]}')
        print(f'The director of movie is {movie["director"]}')
        print(f'The year of release is {movie["year"]}')
        print("")


def search_movie():
    print("""
    How would you like to search :-
    a) By name of movie;
    b) By name of director;
    c) By year of release
    """)
    type = input("Enter a or b or c here: ")
    if type == "a":
        name = input("Enter name of movie you want to search: ")
        for movie in movies:
            if movie["name"] == name:
                print(movie["name"])
                print(movie["director"])
                print(movie["year"])
            elif movie["name"] != name:
                print("")
    elif type == "b":
        direc = input("Enter name of director here :")
        for movie in movies:
            if movie["director"] == direc:
                print(movie["name"])
                print(movie["director"])
                print(movie["year"])
                break
            else:
                print("")
    elif type == "c":
        year = input("Enter the year of release: ")
        for movie in movies:
            if movie["year"] == year:
                print(movie["name"])
                print(movie["director"])
                print(movie["year"])
                break
            else:
                print("")


while option != 4:
    if option == 1:
        add_movie()
        print("Movie details added successfully! ")
        cont = input("Would you like to continue y/n: ")
        if cont == "y":
            intro()
            option = int(input("Enter the number here: "))
        else:
            break
    elif option == 2:
        view_movie()
        cont = input("Would you like to continue y/n: ")
        if cont == "y":
            intro()
            option = int(input("Enter the number here: "))
        else:
            break
    elif option == 3:
        search_movie()
        cont = input("Would you like to continue y/n: ")
        if cont == "y":
            intro()
            option = int(input("Enter the number here: "))
        else:
            break


