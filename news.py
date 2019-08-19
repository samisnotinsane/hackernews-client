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
    max_item_id = news_client.get_max_item_id()
    range_end = max_item_id - n
    i = 1
    for item_id in range(range_end, max_item_id):
        item = news_client.get_item_by_id(item_id)
        printItem(i, item)
        i += 1

def printStory(serial_no, item):
    print(
        '    ' + str(serial_no) + ' -> ' + item.title + '\n' +
        '          ' + 'by: ' + item.by + '\n' +
        '          ' + 'url: ' + item.url + '\n'
    )

def printJob(serial_no, item):
    print(
        '    ' + str(serial_no) + ' -> ' + item.title + '\n' +
        '          ' + 'description: ' + item.text + '\n' +
        '          ' + 'url: ' + item.url + '\n'
    )

def printComment(serial_no, item):
    print(
        '    ' + str(serial_no) + ' -> ' + 'user: ' + item.by + '\n' +
        '          ' + 'comment: ' + item.text + '\n'
        )

def printPoll(serial_no, item, withParts=False):
    if not withParts:
        print(
            '    ' + str(serial_no) + ' -> ' + item.title + '\n' +
            '          ' + 'by: ' + item.by + '\n' +
            '          ' + 'comment count: ' + item.descendants + '\n'
        )
    else:
        client = hn.NewsClient()
        parts_list = item.parts
        print(
                '    ' + str(serial_no) + ' -> ' + item.title + '\n' +
                '          ' + 'by: ' + item.by
        )
        ascii_char = 65 # corresponds to char 'A'
        for part in parts_list:
            part_item = client.get_item_by_id(part)
            print(
                '            ' + chr(ascii_char) + ': ' + part_item.text + ' -> ' + str(part_item.score) + ' votes'
            )
            ascii_char += 1
    print('\n')

def printItem(serial_no, item):
    if item.type == 'story':
        printStory(serial_no, item)
    if item.type == 'comment':
        printComment(serial_no, item)
    if item.type == 'job':
        printJob(serial_no, item)
    if item.type == 'poll':
        printPoll(serial_no, item, withParts=True)

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

    query = 126809 # this is of item type 'poll'
    print('  / showing poll with id: '+ str(query) + ' /\n')
    printQueryItem(news_client, query)

    query = 192327 # this is of item type 'job'
    print('  / showing job with id: '+ str(query) + ' /\n')
    printQueryItem(news_client, query)

    how_many = 3
    print('* LAST ' + str(how_many) + ' ITEMS \n')
    print('  / showing last '+ str(how_many) + ' items /\n')
    recentStories(news_client, n=how_many)

    print('\nExiting')

if __name__ == "__main__":
    main()
