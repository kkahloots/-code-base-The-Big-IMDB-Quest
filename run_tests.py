# Copyright (c) @kkahloots

import unittest
from tqdm import tqdm

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(
        descriptions='The Big IMDB quest test report',
        verbosity=3
        )
    for all_suites in \
        tqdm(loader.discover('./tests', pattern='test_*.py'), desc='all test suites'):
        for test_suite in tqdm(all_suites, desc='running test suite'):
            runner.run(test_suite)
