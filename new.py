import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title("Movie Recommender System")


# movies_list = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
(movies)
)

if st.button('Recommend'):
    recommendencence = recommend(selected_movie_name)
    for movies in recommendencence:
        st.write(movies)