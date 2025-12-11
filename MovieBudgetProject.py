movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]


total_movies = int(input("How many movies would you wanted to add: "))

for number in range(total_movies):
    movie_name = input("Enter Movie Title: ")
    movie_budget = int(input("Movie Budget: "))
    movies.append((movie_name,movie_budget))
    
    
avg_budget = 0


for movie in movies:
    avg_budget += movie[1]
    
avg_movie_budget = avg_budget/len(movies)


total_above_average_budget_movies = 0

print(f"Average Movie Budget Are: {avg_movie_budget}")
for movie in movies:
    if movie[1] > avg_movie_budget:
        print(f"Movie {movie[0]} has budget higher than of average budget with {movie[1] - avg_movie_budget}")
        total_above_average_budget_movies += 1
        
        
print(f"Total Above Average Budget Movies are: {total_above_average_budget_movies}")