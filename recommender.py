import pandas as pd
import ast
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

ps = PorterStemmer()



# Helper Functions


def stem(text):
    return " ".join([ps.stem(word) for word in text.split()])


def convert(text):
    try:
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name'])
        return L
    except:
        return []


def convert_cast(text):
    try:
        L = []
        counter = 0
        for i in ast.literal_eval(text):
            if counter != 3:
                L.append(i['name'])
                counter += 1
            else:
                break
        return L
    except:
        return []


def fetch_director(text):
    try:
        L = []
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
        return L
    except:
        return []



# Load and Prepare Data


def load_and_prepare_data():
    movies = pd.read_csv("data/movie_dataset.csv")

    # Fill missing values
    movies['genres'] = movies['genres'].fillna("[]")
    movies['keywords'] = movies['keywords'].fillna("[]")
    movies['cast'] = movies['cast'].fillna("[]")
    movies['crew'] = movies['crew'].fillna("[]")
    movies['overview'] = movies['overview'].fillna("")

    # Keep only required columns
    movies = movies[['title', 'genres', 'keywords', 'overview', 'cast', 'crew']]

    # Convert JSON-like columns
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert_cast)
    movies['crew'] = movies['crew'].apply(fetch_director)

    # Convert overview to list
    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    # Remove spaces inside words
    movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

    # Create tags column
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

    new_df = movies[['title', 'tags']].copy()

    # Convert tags list to string
    new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
    new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

    # Stemming
    new_df['tags'] = new_df['tags'].apply(stem)

    return new_df



# Build Similarity


def build_similarity():
    new_df = load_and_prepare_data()

    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    vectors = tfidf.fit_transform(new_df['tags']).toarray()

    similarity = cosine_similarity(vectors)

    return new_df, similarity


# Build once when app starts
movies, similarity = build_similarity()



# Recommendation Function


def recommend(movie):
    movie = movie.strip().lower()

    matched_titles = movies[movies['title'].str.lower() == movie]

    if matched_titles.empty:
        return []

    movie_index = matched_titles.index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# For dropdown list in app
def get_movie_titles():
    return sorted(movies['title'].tolist())