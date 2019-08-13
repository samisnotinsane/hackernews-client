from hackernews import HackerNews
import json

def main():
    print('Ready')

def prettify(jsonPayload):
    return json.dumps(jsonPayload, indent=4)

if __name__ == "__main__":
    main()
    hn = HackerNews()
    storyList = hn.topstories(max=5)
    print(prettify(storyList[0]))
