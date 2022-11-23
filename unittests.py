# Copyright (c) @kkahloots

import os
import unittest
from tqdm import tqdm
from prefect import task
from utils import logger

@task
@logger
def run_unittests():
    os.system('python -m unittests')


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
