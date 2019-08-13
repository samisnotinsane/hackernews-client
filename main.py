from hackernews import HackerNews
import json

def main():
    hn = HackerNews()
    print('hackernews-client v0.1')
    
    print('------------------ BEST STORIES ------------------')
    storyList = hn.stories(fetchMax=1, type='beststories')
    bestStoryJsonDict = storyList[0]
    print(bestStoryJsonDict['title'] + ' | score: ' + str(bestStoryJsonDict['score']))
    print(bestStoryJsonDict['url'])

    print('------------------ TOP STORIES ------------------')
    storyList = hn.stories(fetchMax=1, type='topstories')
    topStoryJsonDict = storyList[0]
    print(topStoryJsonDict['title'] + ' | score: ' + str(topStoryJsonDict['score']))
    print(topStoryJsonDict['url'])

    print('------------------ NEW STORIES ------------------')
    storyList = hn.stories(fetchMax=1, type='newstories')
    newStoryJsonDict = storyList[0]
    print(newStoryJsonDict['title'] + ' | score: ' + str(newStoryJsonDict['score']))
    print(newStoryJsonDict['url'])

def prettify(jsonPayload):
    return json.dumps(jsonPayload, indent=4)

if __name__ == "__main__":
    main()
