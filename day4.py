# movies = [
#     (
#         "Eternal Sunshine of the Spotless Mind",
#         "Michel Gondry",
#         2004
#     ),
#     (
#         "Memento",
#         "Christopher Nolan",
#         2000
#     ),
#     (
#         "Requiem for a Dream",
#         "Darren Aronofsky",
#         2000
#     )
# ]


# add_more_movie = True

# for movie in movies:
#     print(f"Movie Name: {movie[0]}, directed by {movie[1]} and released in: {movie[2]}")


movies = []

continue_adding_movie = True

while continue_adding_movie:
    movie_name = input("Enter Movie Name: ")
    movie_director = input("Enter Movie Director: ")
    movie_release_year = input("Enter Movie Released Year: ")
    movie_release_budget = input("Enter Movie Budget: ")
    
    movie_detail = (movie_name,movie_director,movie_release_year,movie_release_budget)
    movies.append(movie_detail)
    
    keep_adding = input("Wanted to add another of your favorite movie detail: ")
    if not keep_adding:
        continue_adding_movie = False
        
        
for movie in movies:
    print(f"Movie Name: {movie[0]}, Movie Director: {movie[1]}, Movie Release Year: {movie[2]}, Movie Total Production Budget: {movie[3]}")
    
    
    
movies.pop(0)
print(movies)