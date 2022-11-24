# Copyright (c) @kkahloots

import numpy as np
from utils import logger

@logger
def adjust_rating(movie_df):
    deviation = int(1e5)
    rating_diff = movie_df['num_ratings'].max() - movie_df['num_ratings']
    movie_df['adjusted_rating'] = movie_df['rating'] - \
        ((rating_diff/deviation).apply(np.floor))*0.1

    return movie_df
