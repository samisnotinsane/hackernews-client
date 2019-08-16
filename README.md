# hackernews-client

[![CircleCI](https://circleci.com/gh/samisnotinsane/hackernews-client/tree/master.svg?style=svg)](https://circleci.com/gh/samisnotinsane/hackernews-client/tree/master)

Use this wrapper library to download Hacker News headlines into your Python program. 

### Prerequisites

requests library is used to wrap around Hacker News' Web API. Therefore you will need this as a dependency.

```
pip install requests
```

## Usage

Initialise the wrapper by instantiating `hn = HackerNews()`. An example of how to use this client can be seen in `examples.py`.

The class supports the following methods:

- `stories`

Parameter | Description
----------|------------
fetchMax | Number of story items to fetch (max: 500)
type | `beststories`: best stories, `topstories`: top stories, `newstories`: new stories

This method returns a list of `Item`. An `Item` is a dict with the following properties (as defined by Hacker News web API):

Field | Description
------|------------
id | The item's unique id.
deleted | `true` if the item is deleted.
type | The type of item. One of "job", "story", "comment", "poll", or "pollopt".
by | The username of the item's author.
time | Creation date of the item, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
text | The comment, story or poll text. HTML.
dead | `true` if the item is dead.
parent | The comment's parent: either another comment or the relevant story.
poll | The pollopt's associated poll.
kids | The ids of the item's comments, in ranked display order.
url | The URL of the story.
score | The story's score, or the votes for a pollopt.
title | The title of the story, poll or job.
parts | A list of related pollopts, in display order.
descendants | In the case of stories or polls, the total comment count.

## Running the tests

Unit tests can be run with the following command

```
python -m unittest -v
```

## Screenshot

![Hacker News Client](/screenshots/hackernews-client-screenshot.png?raw=true "Bash shell running example.py script")

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Author of [haxor](https://github.com/avinassh/haxor) for inspiring me to make my first Python library
* Author of [python-packaging](http://veekaybee.github.io/2017/09/26/python-packaging/) tutorial who helped me get my head around nighmarish Python import system