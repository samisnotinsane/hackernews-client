import requests

class NewsClient(object):
    hn_base_url = 'https://hacker-news.firebaseio.com/v0'
    response_format = '.json'
    
    def __init__(self):
        pass

    def sendRequest(self, url):
        return requests.get(url).json()


    def get_item_by_id(self, id):
        """
        Fetches the data from url: https://hacker-news.firebaseio.com/v0/item/<item_id>.json

        Args:
            id (int): unique item id of Hacker News story
        Returns:
            `Item` representing Hacker News story
        """
        url = 'https://hacker-news.firebaseio.com/v0/item/'
        response = self.sendRequest(url + str(id) + '.json')
        return Item(response)
    
    def item(self, id):
        item = self.sendRequest(self.hn_base_url + '/item/' + str(id) + self.response_format)
        return item

    def stories(self, fetchMax, type):
        if type == 'topstories':
            idList = self.sendRequest(self.hn_base_url + '/topstories' + self.response_format)
        elif type == 'newstories':
            idList = self.sendRequest(self.hn_base_url + '/newstories' + self.response_format)
        elif type == 'beststories':
            idList = self.sendRequest(self.hn_base_url + '/beststories' + self.response_format)
        idListLength = len(idList)
        storyList = []
        if fetchMax < idListLength:
            for i in range(fetchMax):
                id = idList[i]
                if id is not None:
                    story = self.item(id)
                    storyList.append(story)
        return storyList


class Item(object):

    def __init__(self, response_data):
        self.id = response_data.get('id')
        self.deleted = response_data.get('deleted')
        self.type = response_data.get('type')
        self.by = response_data.get('by')
        self.time = response_data.get('time')
        self.text = response_data.get('text')
        self.dead = response_data.get('dead')
        self.parent = response_data.get('parent')
        self.poll = response_data.get('poll')
        self.kids = response_data.get('kids')
        self.url = response_data.get('url')
        self.score = response_data.get('score')
        self.title = response_data.get('title')
        self.parts = response_data.get('parts')
        self.descendants = response_data.get('descendants')
