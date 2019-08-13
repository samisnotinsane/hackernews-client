import requests

class HackerNews:
    hn_base_url = 'https://hacker-news.firebaseio.com/v0'
    response_format = '.json'
    
    def __init__(self):
        pass

    def item(self, id):
        itemRequest = requests.get(self.hn_base_url + '/item/' + str(id) + self.response_format)
        return itemRequest.json()

    def topstories(self, max):
        topStoriesRequest = requests.get(self.hn_base_url + '/topstories' + self.response_format)
        topStoriesIdsList = topStoriesRequest.json()
        # use the ids to get the items
        idListLength = len(topStoriesIdsList)
        storyList = []
        if max < idListLength:
            for i in range(max):
                id = topStoriesIdsList[i]
                if id is not None:
                    story = self.item(id)
                    storyList.append(story)
        return storyList

        