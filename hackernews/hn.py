import requests

from hackernews.item import Item
from hackernews.user import User

class NewsClient(object):
        
    def __init__(self):
        self.base_url = 'https://hacker-news.firebaseio.com/v0'
        self.response_format = '.json'

    def sendRequest(self, url):
        return requests.get(url, timeout=5).json()

    def get_item_by_id(self, id):
        """
        Fetches the data from url: https://hacker-news.firebaseio.com/v0/item/<item_id>.json

        Args:
            id (int): unique item id of Hacker News story
        Returns:
            `Item` representing Hacker News story
        """
        endpoint_url = '/item'
        response = self.sendRequest(self.base_url + endpoint_url + '/' + str(id) + self.response_format)
        return Item(response)
    
    def get_user_by_id(self, id):
        """
        Fetches the data from url:  https://hacker-news.firebaseio.com/v0/user/<user_id>.json

        Args:
            id (case sensitive string): unique id of Hacker News user
        Returns:
            `User` representing Hacker News user
        """
        endpoint_url = '/user'
        try:
            response = self.sendRequest(self.base_url + endpoint_url + '/' + id + self.response_format)
        except requests.ConnectionError as e:
            print(str(e))
        return User(response)

    def get_max_item_id(self):
        """
        Fetches the current largest item id from the url: https://hacker-news.firebaseio.com/v0/maxitem.json
        Returns:
            `int` of the largest item id
        """
        endpoint_url = '/maxitem'
        response = self.sendRequest(self.base_url + endpoint_url + self.response_format)
        return response

    def get_top_story_ids(self, limit=500):
        endpoint_url = '/topstories'
        response = self.sendRequest(self.base_url + endpoint_url + self.response_format)
        return response[:limit]

    def get_new_story_ids(self, limit=500):
        endpoint_url = '/newstories'
        response = self.sendRequest(self.base_url + endpoint_url + self.response_format)
        return response[:limit]

    def get_best_story_ids(self, limit=500):
        endpoint_url = '/beststories'
        response = self.sendRequest(self.base_url + endpoint_url + self.response_format)
        return response[:limit]

    def get_ask_story_ids(self, limit=200):
        endpoint_url = '/askstories'
        response = self.sendRequest(self.base_url + endpoint_url + self.response_format)
        return response[:limit]

    def get_show_story_ids(self, limit=200):
        endpoint_url = '/showstories'
        response = self.sendRequest(self.base_url + endpoint_url + self.response_format)
        return response[:limit]

    def get_job_story_ids(self, limit=200):
        endpoint_url = '/jobstories'
        response = self.sendRequest(self.base_url + endpoint_url + self.response_format)
        return response[:limit]

    def get_top_story(self, fetchMax=500):
        """
        Fetches up to 500 of the latest top stories from the url:
        https://hacker-news.firebaseio.com/v0/topstories.json

        Args:
            fetchMax: number of stories to fetch. Note: max value is 500

        Returns
            stories as list of `Item`
        """
        top_story_ids = self.get_top_story_ids(limit=fetchMax)
        top_story_items = []
        for top_story_id in top_story_ids:
            top_story_items.append(self.get_item_by_id(top_story_id))
        return top_story_items

    def get_ask_story(self, fetchMax=200):
        """
        Fetches up to 200 of the latest Ask Hacker News stories from the url: 
        https://hacker-news.firebaseio.com/v0/askstories.json

        Args:
            fetchMax: number of stories to fetch. Note: max value is 200

        Returns:
            stories as list of `Item`
        """
        ask_story_ids = self.get_ask_story_ids(limit=fetchMax)
        ask_story_items = []
        for ask_story_id in ask_story_ids:
            ask_story_items.append(self.get_item_by_id(ask_story_id))
        return ask_story_items

    def get_new_story(self, fetchMax=500):
        new_story_ids = self.get_new_story_ids(limit=fetchMax)
        new_story_items = []
        for new_story_id in new_story_ids:
            new_story_items.append(self.get_item_by_id(new_story_id))
        return new_story_items

    def get_show_story(self, fetchMax=200):
        """
        Fetches up to 200 of the latest Show Hacker News stories from the url: 
        https://hacker-news.firebaseio.com/v0/showstories.json

        Args:
            fetchMax: number of stories to fetch. Note: max value is 200

        Returns:
            stories as list of `Item`
        """
        show_story_ids = self.get_show_story_ids(limit=fetchMax)
        show_story_items = []
        for show_story_id in show_story_ids:
            show_story_items.append(self.get_item_by_id(show_story_id))
        return show_story_items
    
    def get_job_story(self, fetchMax=200):
        job_story_ids = self.get_job_story_ids(limit=fetchMax)
        job_story_items = []
        for job_story_id in job_story_ids:
            job_story_items.append(self.get_item_by_id(job_story_id))
        return job_story_items

    def item(self, id):
        item = self.sendRequest(self.base_url + '/item/' + str(id) + self.response_format)
        return item

    def stories(self, fetchMax, type):
        if type == 'topstories':
            idList = self.sendRequest(self.base_url + '/topstories' + self.response_format)
        elif type == 'newstories':
            idList = self.sendRequest(self.base_url + '/newstories' + self.response_format)
        elif type == 'beststories':
            idList = self.sendRequest(self.base_url + '/beststories' + self.response_format)
        idListLength = len(idList)
        storyList = []
        if fetchMax < idListLength:
            for i in range(fetchMax):
                id = idList[i]
                if id is not None:
                    story = self.item(id)
                    storyList.append(story)
        return storyList
