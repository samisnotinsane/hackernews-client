import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from hackernews.hn import NewsClient
from hackernews.hn import Item

class TestTopStories(unittest.TestCase):
    
    def setUp(self):
        self.client = NewsClient()

    def test_get_item_by_id(self):
        item = self.client.get_item_by_id(8863)
        self.assertIsInstance(item, Item)
        self.assertEqual(item.by, 'dhouston')
        self.assertEqual(item.id, 8863)
        self.assertEqual(item.descendants, 71)
        self.assertSetEqual(set(item.kids), set([8952, 9224, 8917, 8884, 8887, 8943, 8869, 8958, 9005, 9671, 8940, 9067, 8908, 9055, 8865, 8881, 8872, 8873, 8955, 10403, 8903, 8928, 9125, 8998, 8901, 8902, 8907, 8894, 8878, 8870, 8980, 8934, 8876]))
        # self.assertEqual(item.score, 111) # not making assertions as this changes over time
        self.assertEqual(item.time, 1175714200)
        self.assertEqual(item.title, 'My YC app: Dropbox - Throw away your USB drive')
        self.assertEqual(item.type, 'story')
        self.assertEqual(item.url, 'http://www.getdropbox.com/u/2/screencast.html')


    # def test_top_stories(self):
    #     top_stories = self.client.stories(fetchMax=5, type='topstories')
    #     self.assertIsInstance(top_stories, list)
    #     self.assertIsInstance(top_stories[0], Item)
    #     self.assertIsNotNone(top_stories) 

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()