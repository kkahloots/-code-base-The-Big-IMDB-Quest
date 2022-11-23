# Copyright (c) @kkahloots


import unittest
import requests
from bs4 import BeautifulSoup
from utils import get_config

class TestValidPage(unittest.TestCase):
    config = None
    parser = None

    def setUpClass():
        TestValidPage.config = get_config()

        req = requests.get(TestValidPage.config['url']).content
        TestValidPage.parser = BeautifulSoup(req, 'html.parser')

    def test_has_title(self):
        pageTitle = TestValidPage.parser.find('h1').get_text()
        self.assertEqual(TestValidPage.config['title'], pageTitle)

    def test_has_content(self):
        content = [
            tag.attrs.get('title') \
                for tag in TestValidPage.parser.select('td.ratingColumn strong')
                ]
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)
