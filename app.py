import streamlit as st
import pickle
import pandas as pd

#recommend function
def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

        recommend_movies = []
        for i in movie_list:
            movie_id = i[0]#fetch movies poster from APT
            recommend_movies.append(movies.iloc[i[0]].title)

        return recommend_movies

    
# Importing the dataset 
movies_dict = pickle.load(open('movies_new.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


# Title of Page
st.title('Movie Recommendation System')

select_movie_name = st.selectbox(
"How would you like to be contacted?",
movies['title'].values)


#Button
if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i) 

