# Copyright (c) @kkahloots


import unittest
import pandas as pd
from review_penalizer import adjust_rating

mimic_movie_df = pd.DataFrame(
    [
        [235461, 8.1],
        [965482, 9.3],
        [233433, 9.5],
        [105484, 8.4]
        ],
    columns=['num_ratings', 'rating'])
expected_adjusted_rating = [7.4, 9.3, 8.8, 7.6]

class TestViewPenalizer(unittest.TestCase):
    adjusted_rating = None

    def setUpClass():
        TestViewPenalizer.adjusted_rating = \
            [ round(r, 1) for r in adjust_rating(mimic_movie_df)['adjusted_rating'].values]

    def test_count_rating_adjusted(self):
        self.assertCountEqual(
            TestViewPenalizer.adjusted_rating,
            expected_adjusted_rating
            )

    def test_value_rating_adjusted(self):
        self.assertListEqual(
            TestViewPenalizer.adjusted_rating,
            expected_adjusted_rating
            )

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)
