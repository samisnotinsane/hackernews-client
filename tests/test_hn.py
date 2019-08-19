import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from hackernews.hn import NewsClient
from hackernews.hn import Item
from hackernews.hn import User

class TestTopStories(unittest.TestCase):
    
    def setUp(self):
        self.client = NewsClient()

    def test_get_story_item_by_id(self):
        item = self.client.get_item_by_id(8863)
        self.assertIsInstance(item, Item)
        self.assertEqual(item.by, 'dhouston')
        self.assertEqual(item.id, 8863)
        self.assertEqual(item.descendants, 71)
        self.assertSetEqual(set(item.kids), set([8952, 9224, 8917, 8884, 8887, 8943, 8869, 8958, 9005, 9671, 8940, 9067, 8908, 9055, 8865, 8881, 8872, 8873, 8955, 10403, 8903, 8928, 9125, 8998, 8901, 8902, 8907, 8894, 8878, 8870, 8980, 8934, 8876]))
        # self.assertEqual(item.score, ...) # not making assertions as this changes over time
        self.assertEqual(item.time, 1175714200)
        self.assertEqual(item.title, 'My YC app: Dropbox - Throw away your USB drive')
        self.assertEqual(item.type, 'story')
        self.assertEqual(item.url, 'http://www.getdropbox.com/u/2/screencast.html')

    def test_get_comment_item_by_id(self):
        item = self.client.get_item_by_id(2921983)
        self.assertIsInstance(item, Item)
        self.assertEqual(item.by, 'norvig')
        self.assertEqual(set(item.kids), set([2922097, 2922429, 2924562, 2922709, 2922573, 2922140, 2922141]))
        self.assertEqual(item.parent, 2921506)
        self.assertEqual(item.text, "Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?")
        self.assertEqual(item.time, 1314211127)
        self.assertEqual(item.type, 'comment')

    def test_get_ask_item_by_id(self):
        item = self.client.get_item_by_id(121003)
        self.assertIsInstance(item, Item)
        self.assertEqual(item.by, 'tel')
        self.assertEqual(item.descendants, 16)
        self.assertEqual(item.id, 121003)
        self.assertEqual(set(item.kids), set([121016, 121109, 121168]))
        self.assertEqual(item.text, "<i>or</i> HN: the Next Iteration<p>I get the impression that with Arc being released a lot of people who never had time for HN before are suddenly dropping in more often. (PG: what are the numbers on this? I'm envisioning a spike.)<p>Not to say that isn't great, but I'm wary of Diggification. Between links comparing programming to sex and a flurry of gratuitous, ostentatious  adjectives in the headlines it's a bit concerning.<p>80% of the stuff that makes the front page is still pretty awesome, but what's in place to keep the signal/noise ratio high? Does the HN model still work as the community scales? What's in store for (++ HN)?")
        self.assertEqual(item.time, 1203647620)
        self.assertEqual(item.title, 'Ask HN: The Arc Effect')
        self.assertEqual(item.type, 'story')
        self.assertFalse(item.url)
    
    def test_get_job_item_by_id(self):
        item = self.client.get_item_by_id(192327)
        self.assertIsInstance(item, Item)
        self.assertEqual(item.by, 'justin')
        self.assertEqual(item.text, "Justin.tv is the biggest live video site online. We serve hundreds of thousands of video streams a day, and have supported up to 50k live concurrent viewers. Our site is growing every week, and we just added a 10 gbps line to our colo. Our unique visitors are up 900% since January.<p>There are a lot of pieces that fit together to make Justin.tv work: our video cluster, IRC server, our web app, and our monitoring and search services, to name a few. A lot of our website is dependent on Flash, and we're looking for talented Flash Engineers who know AS2 and AS3 very well who want to be leaders in the development of our Flash.<p>Responsibilities<p><pre><code>    * Contribute to product design and implementation discussions\n    * Implement projects from the idea phase to production\n    * Test and iterate code before and after production release \n</code></pre>\nQualifications<p><pre><code>    * You should know AS2, AS3, and maybe a little be of Flex.\n    * Experience building web applications.\n    * A strong desire to work on website with passionate users and ideas for how to improve it.\n    * Experience hacking video streams, python, Twisted or rails all a plus.\n</code></pre>\nWhile we're growing rapidly, Justin.tv is still a small, technology focused company, built by hackers for hackers. Seven of our ten person team are engineers or designers. We believe in rapid development, and push out new code releases every week. We're based in a beautiful office in the SOMA district of SF, one block from the caltrain station. If you want a fun job hacking on code that will touch a lot of people, JTV is for you.<p>Note: You must be physically present in SF to work for JTV. Completing the technical problem at <a href=\"http://www.justin.tv/problems/bml\" rel=\"nofollow\">http://www.justin.tv/problems/bml</a> will go a long way with us. Cheers!")
        self.assertEqual(item.time, 1210981217)
        self.assertEqual(item.title, "Justin.tv is looking for a Lead Flash Engineer!")
        self.assertEqual(item.type, 'job')
        self.assertFalse(item.url)

    def test_get_user_by_id(self):
        user = self.client.get_user_by_id('jl')
        self.assertIsInstance(user, User)
        self.assertEqual(user.about, 'This is a test')
        self.assertEqual(user.created, 1173923446)
        self.assertEqual(user.delay, None)
        self.assertEqual(user.id, 'jl')
        # not making assertions about below as this changes over time
        # self.assertEqual(user.karma, ...)
        # self.assertEqual(set(user.submitted), set([8265435, 8168423, 8090946, ... ]))

    def test_get_max_item_id(self):
        id = self.client.get_max_item_id()
        self.assertIsNotNone(id)

    def test_get_top_story_ids(self):
        top_story_ids = self.client.get_top_story_ids(limit=10)
        self.assertEqual(len(top_story_ids), 10)

    def test_get_new_story_ids(self):
        new_story_ids = self.client.get_new_story_ids(limit=10)
        self.assertEqual(len(new_story_ids), 10)
    
    def test_get_best_story_ids(self):
        best_story_ids = self.client.get_best_story_ids(limit=10)
        self.assertEqual(len(best_story_ids), 10)

    def test_get_ask_story_ids(self):
        ask_story_ids = self.client.get_ask_story_ids(limit=10)
        self.assertEqual(len(ask_story_ids), 10)

    def test_get_show_story_ids(self):
        show_story_ids = self.client.get_show_story_ids(limit=10)
        self.assertEqual(len(show_story_ids), 10)

    def test_get_job_story_ids(self):
        job_story_ids = self.client.get_job_story_ids(limit=10)
        self.assertEqual(len(job_story_ids), 10)

    def test_get_new_story(self):
        new_story_items = self.client.get_new_story(fetchMax=10)
        self.assertEqual(len(new_story_items), 10)
        self.assertIsNotNone(new_story_items[0])

    def test_get_show_story(self):
        show_story_items = self.client.get_show_story(fetchMax=2)
        self.assertTrue(show_story_items)
        self.assertEqual(len(show_story_items), 2)
        self.assertIsNotNone(show_story_items[0])
        self.assertIsInstance(show_story_items[0], Item)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()