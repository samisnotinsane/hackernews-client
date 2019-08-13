from hackernews import HackerNews
import json

def main():
    hn = HackerNews()
    print('hackernews-client v0.1')
    
    print('------------------ BEST STORIES ------------------')
    storyList = hn.stories(fetchMax=1, type='beststories')
    print(prettify(storyList[0]))

    print('------------------ TOP STORIES ------------------')
    storyList = hn.stories(fetchMax=1, type='topstories')
    print(prettify(storyList[0]))

    print('------------------ NEW STORIES ------------------')
    storyList = hn.stories(fetchMax=1, type='newstories')
    print(prettify(storyList[0]))

def prettify(jsonPayload):
    return json.dumps(jsonPayload, indent=4)

if __name__ == "__main__":
    main()
