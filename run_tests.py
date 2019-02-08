""" Run the tests """
import unittest

def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('develop/tests/v1', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    test()
    
