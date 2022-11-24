# Copyright (c) @kkahloots


import unittest
from utils import get_config
from scraper import scrape

class TestScraper(unittest.TestCase):
    config = None
    movie_df = None

    def setUpClass():
        TestScraper.config = get_config()
        TestScraper.movie_df = scrape(
            base_url=TestScraper.config['base_url'],
            top_path=TestScraper.config['top_path'],
            top_n=TestScraper.config['top_n']
        )

    def test_scraped_content(self):
        self.assertIsNotNone(TestScraper.movie_df)

    def test_scraped_top_n(self):
        self.assertEqual(TestScraper.config['top_n'], len(TestScraper.movie_df))

    def test_data_structure(self):
        self.assertEqual(
            [c for c in TestScraper.movie_df.columns],
            ['title', 'num_ratings', 'num_oscars', 'rating']
            )

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)
