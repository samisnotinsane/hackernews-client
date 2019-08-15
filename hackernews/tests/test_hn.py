import unittest

from hackernews import NewsClient

class TestTopStories(unittest.TestCase):
    
    def setUp(self):
        self.client = hn.NewsClient()

    def test_top_stories(self):
        top_stories = self.client.stories(fetchMax=5, type='topstories')
        self.assertIsInstance(top_stories, list)
        self.assertIsInstance(top_stories[0], hn.Item)
        self.assertIsNotNone(top_stories) 

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()