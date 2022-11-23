# Copyright (c) @kkahloots

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./tests', pattern='test_*.py')
    result = BeautifulReport(test_suite)
    result.report(
        filename='unittest_report',
        description='The Big IMDB quest test report',
        report_dir='reports',
        theme='theme_default'
        )
