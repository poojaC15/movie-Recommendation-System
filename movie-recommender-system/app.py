import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=312a1df4a0471ce909a2f93c5ec51d13&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Please select a movie, and I will provide you with movie recommendations based on your selection.',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col = st.columns(5)
    for i in range(len(names)):
        with col[i]:
            st.text(names[i])
            st.image(posters[i])