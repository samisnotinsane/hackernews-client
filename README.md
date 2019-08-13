# hackernews-client
A simple Python wrapper for Hacker News web API.

## Usage
Initialise the wrapper by instantiating `hn = HackerNews()`. An example of how to use this client can be seen in `main.py`.

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