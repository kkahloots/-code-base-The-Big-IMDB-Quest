# Copyright (c) @kkahloots

import re

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from utils import logger


@logger
def request_page(url):
    header = {'User-Agent':
              'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15'
              ' (KHTML, like Gecko) Mobile/15E148'}
    req_content = requests.get(url, headers=header).content
    lxml_parser = BeautifulSoup(req_content, 'lxml')
    return lxml_parser


@logger
def scrape(base_url, top_path, top_n):
    movies_page = request_page(url=f'{base_url}{top_path}')
    movies = movies_page.select('td.titleColumn')
    movie_id = [
        b.attrs.get('href') for b in
        tqdm(movies_page.select('td.posterColumn a'))
    ]
    oscar_df = pd.DataFrame(columns=[0])

    for movie in tqdm(movie_id[:top_n]):
        movie_url = f"{base_url}{movie}"
        movie_page = request_page(movie_url)
        awards = [
            b for b in
            tqdm(
                movie_page.find(
                    'a',
                    attrs={
                        'class':
                            'ipc-metadata-list-item__label ipc-metadata-list-item__label--link',
                        'href': re.compile('awards')
                    })
            )
        ]
        oscar_df.loc[len(oscar_df)] = awards

    oscar_df = oscar_df[0].str.split(' ', 5, expand=True)
    for c in tqdm(oscar_df):
        if str(oscar_df[c].dtype) in ('object', 'string_', 'unicode_'):
            oscar_df[c].fillna(value='', inplace=True)

    oscar_df[1] = np.where((oscar_df[1] == "for") | (
        oscar_df[1] == ""), 0, oscar_df[1])
    oscar_nr = oscar_df[1].to_dict()

    # split ratings and number of ratings from text field
    rating = [
        b.attrs.get('title') for b in
        tqdm(movies_page.select('td.ratingColumn strong'))
    ]

    rating_df = pd.DataFrame(rating)
    rating_df = rating_df[0].str.split(' ', 5, expand=True)
    rating_nr = rating_df[3].str.replace(',', '').astype(int).to_dict()

    # it will be the final df
    movie_df = pd.DataFrame(
        columns=['title', 'num_ratings', 'num_oscars', 'rating'])

    for ix in tqdm(range(top_n)):
        movie_string = movies[ix].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        if ix > 9:
            movie_title = movie[len(str())+3:-7]
        else:
            movie_title = movie[len(str())+2:-7]
        data = [movie_title, rating[ix][:3], rating_nr[ix], oscar_nr[ix]]

        movie_df.loc[len(movie_df)] = data

    return movie_df.sort_index(ascending=False).reset_index(drop=True) \
        .astype({'rating': float, 'num_oscars': int, 'num_ratings': float})
