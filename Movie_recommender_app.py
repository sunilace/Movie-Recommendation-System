import streamlit as st
import pickle
import pandas as pd
import requests


def recommend_movie(movie_n):
    movie_name = []
    movie_poster = []
    ind = movies[movies['title'] == movie_n].index[0]
    distance = similarity[ind]
    sort = sorted(list(enumerate(distance)),  key=lambda x: x[1], reverse=True)
    for i in range(1, 6):
        name = movies['title'][sort[i][0]]
        movie_name.append(name)
        inx = movies[movies['title'] == name].index[0]
        inx = movies.iloc[inx, 0]
        movie_poster.append(poster(inx))
    return movie_name, movie_poster


def poster(movie_ids):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_ids}"
                            f"?api_key=7c108b39140f32a8a2e86d3c466ac5a8&language=en-US")
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


st.title('Movies Recommender System')
movie_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_list)
Selected_movie = st.selectbox('Choose the movie based on which you want recommendations?', movies['title'])
if st.button('Suggest'):
    movie, poster = recommend_movie(Selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie[0])
        st.image(poster[0])
    with col2:
        st.text(movie[1])
        st.image(poster[1])
    with col3:
        st.text(movie[2])
        st.image(poster[2])
    with col4:
        st.text(movie[3])
        st.image(poster[3])
    with col5:
        st.text(movie[4])
        st.image(poster[4])
