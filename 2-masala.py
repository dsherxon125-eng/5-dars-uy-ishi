import os
os.system("cls")

movies = {
    "Titanic": 1997,
    "Avatar": 2009,
    "Inception": 2010,
    "Interstellar": 2014
}

for movie, year in movies.items():
    if year > 2000:
        print(movie)
