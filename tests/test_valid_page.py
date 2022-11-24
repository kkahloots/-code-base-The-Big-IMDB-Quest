# Copyright (c) @kkahloots


import unittest
from utils import get_config
from scraper import request_page

class TestValidPage(unittest.TestCase):
    config = None
    parser = None

    def setUpClass():
        TestValidPage.config = get_config()
        top_url = f"{TestValidPage.config['base_url']}{TestValidPage.config['top_path']}"
        TestValidPage.parser = request_page(top_url)

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
