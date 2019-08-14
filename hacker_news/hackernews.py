import requests

class HackerNewsClient(object):
    hn_base_url = 'https://hacker-news.firebaseio.com/v0'
    response_format = '.json'
    
    def __init__(self):
        pass

    def sendReq(self, url):
        return requests.get(url).json()
    
    def item(self, id):
        item = self.sendReq(self.hn_base_url + '/item/' + str(id) + self.response_format)
        return item

    def stories(self, fetchMax, type):
        if type == 'topstories':
            idList = self.sendReq(self.hn_base_url + '/topstories' + self.response_format)
        elif type == 'newstories':
            idList = self.sendReq(self.hn_base_url + '/newstories' + self.response_format)
        elif type == 'beststories':
            idList = self.sendReq(self.hn_base_url + '/beststories' + self.response_format)
        idListLength = len(idList)
        storyList = []
        if fetchMax < idListLength:
            for i in range(fetchMax):
                id = idList[i]
                if id is not None:
                    story = self.item(id)
                    storyList.append(story)
        return storyList
