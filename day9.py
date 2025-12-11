# main_characters = [
#     ("BoJack Horseman", "Will Arnett", "Horse"),
#     ("Princess Carolyn", "Amy Sedaris", "Cat"),
#     ("Diane Nguyen", "Alison Brie", "Human"),
#     ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
#     ("Todd Chavez", "Aaron Paul", "Human")
# ]


# for character,actor,species in main_characters:
#     print(f"{character} is a {species} voiced by {actor}")


student_name,student_id,(major_subject,minor_subject) = ("John Smith", 11743, ("Computer Science", "Mathematics"))
# print(student_name)
# print(student_id)
# print(major_subject)
# print(minor_subject)


movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men",
    "Bahuballi The Beginning"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen",
]


complete_movies = list(zip(movie_titles,movie_directors))
# print(complete_movies)