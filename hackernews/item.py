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
