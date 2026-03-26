import streamlit as st
from recommender import recommend, get_movie_titles


# Page Config

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="centered")

# Custom Styling

st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p, div, label {
        color: white !important;
    }
    .movie-box {
        background-color: #1f2937;
        padding: 12px;
        margin: 10px 0;
        border-radius: 10px;
        color: white;
        font-size: 18px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)


# Title

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get top 5 similar movie recommendations.")


# Dropdown

movie_list = get_movie_titles()
selected_movie = st.selectbox("Choose a movie", movie_list)

# Recommend Button

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    if recommendations:
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.markdown(f"<div class='movie-box'>{movie}</div>", unsafe_allow_html=True)
    else:
        st.error("Movie not found. Please try another title.")