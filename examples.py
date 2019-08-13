from hackernews import HackerNews
import json

def main():
    hn = HackerNews()
    print('hackernews-client v0.1\n\n')
    
    print('------------------ BEST STORIES ------------------\n')
    storyList = hn.stories(fetchMax=1, type='beststories')
    for i in range(len(storyList)):
        bestStoryJsonDict = storyList[i]
        print(str(i+1) + '. ' + bestStoryJsonDict['title'] + ' | score: ' + str(bestStoryJsonDict['score']))
        if 'url' in bestStoryJsonDict:
            print('->' + bestStoryJsonDict['url'])
        print('\n')

    print('------------------ TOP STORIES ------------------\n')
    storyList = hn.stories(fetchMax=5, type='topstories')
    for i in range(len(storyList)):
        topStoryJsonDict = storyList[i]
        print(str(i+1) + '. ' + topStoryJsonDict['title'] + ' | score: ' + str(topStoryJsonDict['score']))
        if 'url' in topStoryJsonDict:
            print('-> ' + topStoryJsonDict['url'])
        print('\n')

    print('------------------ NEW STORIES ------------------\n')
    storyList = hn.stories(fetchMax=3, type='newstories')
    if storyList:
        for i in range(len(storyList)):
            newStoryJsonDict = storyList[i]
            print(str(i+1) + '. ' + newStoryJsonDict['title'] + ' | score: ' + str(newStoryJsonDict['score']))
            if 'url' in newStoryJsonDict:
                print('-> ' + newStoryJsonDict['url'])
            print('\n')
    

def prettify(jsonPayload):
    return json.dumps(jsonPayload, indent=4)

if __name__ == "__main__":
    main()
