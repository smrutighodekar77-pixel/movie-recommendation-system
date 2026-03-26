import streamlit as st
import pickle
from recommender import recommend


# Page Configuration

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)


# Custom Styling

st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #ff4b4b;
    }

    .sub-text {
        text-align: center;
        font-size: 18px;
        color: #d3d3d3;
        margin-bottom: 20px;
    }

    .recommend-box {
        background-color: #f5f5f5;
        color: #000000;   /* FIXED: black text */
        padding: 14px;
        border-radius: 12px;
        margin-bottom: 12px;
        font-size: 20px;
        font-weight: 600;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.15);
    }

    .footer-text {
        text-align: center;
        color: #aaaaaa;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)


# Load Movies for Dropdown

movies = pickle.load(open("outputs/movies.pkl", "rb"))


# UI

st.markdown('<div class="main-title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Find movies similar to your favorite one </div>', unsafe_allow_html=True)

movie_list = sorted(movies['title'].unique())
selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Top 5 Recommended Movies")
    for idx, movie in enumerate(recommendations, start=1):
        st.markdown(f'<div class="recommend-box">{idx}. {movie}</div>', unsafe_allow_html=True)

st.write("---")
