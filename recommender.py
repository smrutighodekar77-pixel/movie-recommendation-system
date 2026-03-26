import pickle
import pandas as pd

# Load Saved Files

movies = pickle.load(open("outputs/movies.pkl", "rb"))
similarity = pickle.load(open("outputs/similarity.pkl", "rb"))


# Recommendation Function

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"]

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies