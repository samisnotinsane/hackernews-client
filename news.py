from hackernews import hn

def printBestStories(news_client, n=10):
    best_story_list = news_client.get_best_story(n)
    i = 1
    for best_story in best_story_list:
        printItem(i, best_story)
        i+=1

def printQueryItem(news_client, item_id):
    found_item = news_client.get_item_by_id(item_id)
    printItem(1, found_item)

def recentStories(news_client, n=10):
    pass

def main():
    print('hackernews-client v0.1\n\nExamples:\n\n')
    news_client = hn.NewsClient()

    print('* BEST STORIES ')
    how_many = 3
    print('  / showing '+ str(how_many) + ' best stories /\n')
    printBestStories(news_client, how_many)

    query = 8863 # this is of item type 'story'
    print('* SEARCH ')
    print('  / showing story with id: '+ str(query) + ' /\n')
    printQueryItem(news_client, query)

    query = 2921983 # this is of item type 'comment'
    print('  / showing comment with id: '+ str(query) + ' /\n')
    printQueryItem(news_client, query)

    print('* LAST 5 STORIES \n')
    recentStories(news_client, n=5)

    print('\nExiting')

def printStory(serial_no, item):
    print(
        '    ' + str(serial_no) + ' -> ' + item.title + '\n' +
        '          ' + 'by: ' + item.by + '\n' +
        '          ' + 'url: ' + item.url + '\n'
    )

def printJob(serial_no, item):
    print('printJob not yet implemented')

def printComment(serial_no, item):
    print(
        '    ' + str(serial_no) + ' -> ' + 'user: ' + item.by + '\n' +
        '          ' + 'comment: ' + item.text + '\n'
        )

def printPoll(serial_no, item, withParts=False):
    print('printPoll not yet implemented')

def printItem(serial_no, item):
    if item.type == 'story':
        printStory(serial_no, item)
    if item.type == 'comment':
        printComment(serial_no, item)
    if item.type == 'job':
        printJob(serial_no, item)
    if item.type == 'poll':
        printPoll(serial_no, item, withParts=True)


if __name__ == "__main__":
    main()
