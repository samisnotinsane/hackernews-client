class User(object):
    
    def __init__(self, response_data):
        self.id = response_data.get('id')
        self.delay = response_data.get('delay')
        self.created = response_data.get('created')
        self.karma = response_data.get('karma')
        self.about = response_data.get('about')
        self.submitted = response_data.get('submitted')
        