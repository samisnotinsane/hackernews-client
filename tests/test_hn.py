import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from hackernews.hn import NewsClient
from hackernews.hn import Item

class TestTopStories(unittest.TestCase):
    
    def setUp(self):
        self.client = NewsClient()

    def test_top_stories(self):
        top_stories = self.client.stories(fetchMax=5, type='topstories')
        self.assertIsInstance(top_stories, list)
        self.assertIsInstance(top_stories[0], Item)
        self.assertIsNotNone(top_stories) 

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()