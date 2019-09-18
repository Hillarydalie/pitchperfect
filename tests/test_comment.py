import unittest
from app.models import Comment

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = new_comment(
            "1",
            "hillarydalie", 
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse", 
            "24th Sept 2019"
            )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
