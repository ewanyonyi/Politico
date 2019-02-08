""" The main module to run the server """
import os
import unittest
import coverage
import app

COV = coverage.coverage(
    branch=True,
    include='develop/*',
    omit=[
        'tests/*',
        'config.py'
    ]
)

COV.start()


def cov():
    """
    Runs the coverage unit test
    """
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        basedir = os.path.abspath(os.path.dirname(__file__))
        coveragedir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=coveragedir)
        print('HTML version: file://%s/index.html' % coveragedir)
        COV.erase()
        return 0
    return 1

if __name__ == '__main_