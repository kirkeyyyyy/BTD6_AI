import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def popular(ratings_df):
    group = ratings_df.groupby('movieId')
    group = group.count()
    movie_by_popular = group[['rating']]
    movie_by_popular.rename(columns={'rating': 'count'}, inplace=True)
    movie_by_popular = movie_by_popular.sort_values(by = 'count')
    # 5. The Matrix, 4. Silence of the Lambs, 3. Pulp Fiction, 2. Shawshank Redemption, 1. Forrest Gump
    plt.hist(movie_by_popular['count'], bins=15) 
    plt.title("Frequency Distribution For Number of Times Movies is Rated")
    plt.xlabel("# of times rated")
    plt.ylabel("Frequency")
    plt.show() 

ratings_df = pd.read_csv("ml-latest-small/ratings.csv")
train_df, test_df = pd.DataFrame(), pd.DataFrame()
 
for value in ratings_df['userId'].unique():  
    train_values, test_values = train_test_split(ratings_df[ratings_df['userId'] == value], test_size = 0.2, random_state = 2)
    train_df = pd.concat([train_df, train_values])
    test_df = pd.concat([test_df, test_values]) 
movie_ratings = popular(ratings_df)