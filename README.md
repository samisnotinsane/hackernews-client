# hackernews-client

[![CircleCI](https://circleci.com/gh/samisnotinsane/hackernews-client/tree/master.svg?style=svg)](https://circleci.com/gh/samisnotinsane/hackernews-client/tree/master)
[![codebeat badge](https://codebeat.co/badges/651aecbd-aba5-4631-9246-fce7bca9a382)](https://codebeat.co/projects/github-com-samisnotinsane-hackernews-client-master)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://opensource.org/licenses/mit-license.php)

Use this wrapper library to download Hacker News headlines into your Python program. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need the python-requests library so we can make HTTP calls. Install with pip:

```
pip install requests
```

### Installing

Using pip

```
pip install hackernews-client==0.1.2b1
```

From sources

```
git clone https://github.com/samisnotinsane/hackernews-client.git
cd hackernews-client
```

Run the example script: `news.py`

```
python news.py
```

this fetches:
  - Best stories
  - Search
    - story
    - comment
    - poll
    - job
  - Most recent items (last `n` items)

You may make another copy of this script

```
cp news.py ./my_copy_news.py
python my_copy_news.py
```

modifying it to suit your use case.

Make sure your setup is working by opening IDLE and importing the library (see Usage section below) if you have installed via pip.

## Running the tests

This package contains tests which verifies the integrity of the internal logic.

### Unit tests

To run all unit tests, make sure you're in the root directory (`hackernews-client`). Use Python's built in `unittest` library

```
python -m unittest -v
```

If you have clone from `master` branch, these should always pass. At the time of testing, sometimes these tests failed with `SSLErrors` due to too many requests being made to the Hacker News API too quickly. Wait ~20 secs before running the unit tests again.

Alternatively, it could be that a breaking change was made to the Web API which would require updating this library. Feel free to raise an [Issue](https://github.com/samisnotinsane/hackernews-client/issues) or a [Pull Request](https://github.com/samisnotinsane/hackernews-client/pulls) to remediate the problem.

## Usage

Begin by importing the library. This example assumes you're working within `news.py` in the root directory of the repo.

```
from hackernews import hn
```

The client is then initialised in the following way

```
news_client = hn.NewsClient()
```

In this case, `news_client` object gives access to all available methods. The data contained in the methods and the instances returned all closely follow the [HackerNews API](https://github.com/HackerNews/API).

Try to print the headline of the best story today. First open IDLE, then

```
print(str(news_client.get_best_story(fetchMax=10)[0].title))
```

If you can read the headline, you're good to go!

Full documentation with examples are provided below.

## Documentation

### Class: `NewsClient`

- `get_item`

**Parameters:**


| Name       | Type | Required | Description                                   | Default
| ---------- | ---- | -------- | --------------------------------------------- | -------
| `item_id`  | int  | Yes      | unique item id of Hacker News story, comment etc | None

Returns:
a list of `Item` (each of type `dict`). See class documentation for `Item` which contains a full description of each property.


- `get_top_story`

**Parameters:**

| Name        | Type    | Required    | Description                             | Default
| ----------- | ------- | ----------- | --------------------------------------- | -------
| `fetchMax`  | int     | Yes         | Number of stories to fetch, max value = 500 | 500

Returns:
a list of top stories as `Item` from the url `https://hacker-news.firebaseio.com/v0/topstories.json`

- `get_ask_story`

**Parameters:**

| Name        | Type    | Required    | Description                             | Default
| ----------- | ------- | ----------- | --------------------------------------- | -------
| `fetchMax`  | int     | Yes         | Number of stories to fetch, max value = 200 | 200

Returns:
a list of Ask HN stories as `Item` from the url `https://hacker-news.firebaseio.com/v0/askstories.json`

- `get_new_story`

**Parameters:**

| Name        | Type    | Required    | Description                             | Default
| ----------- | ------- | ----------- | --------------------------------------- | -------
| `fetchMax`  | int     | Yes         | Number of stories to fetch, max value = 500 | 500

Returns:
a list of new stories as `Item` from the url `https://hacker-news.firebaseio.com/v0/newstories.json`

- `get_show_story`

**Parameters:**

| Name        | Type    | Required    | Description                             | Default
| ----------- | ------- | ----------- | --------------------------------------- | -------
| `fetchMax`  | int     | Yes         | Number of stories to fetch, max value = 200 | 200

Returns:
a list of Show HN stories as `Item` from the url `https://hacker-news.firebaseio.com/v0/showstories.json`

- `get_best_story`

**Parameters:**

| Name        | Type    | Required    | Description                             | Default
| ----------- | ------- | ----------- | --------------------------------------- | -------
| `fetchMax`  | int     | Yes         | Number of stories to fetch, max value = 200 | 200

Returns:
a list of best stories as `Item` from the url `https://hacker-news.firebaseio.com/v0/beststories.json`

- `get_job_story`

**Parameters:**

| Name        | Type    | Required    | Description                             | Default
| ----------- | ------- | ----------- | --------------------------------------- | -------
| `fetchMax`  | int     | Yes         | Number of stories to fetch, max value = 200 | 200

Returns:
a list of job stories as `Item` from the url `https://hacker-news.firebaseio.com/v0/jobstories.json`

- `get_max_item_id`

**Parameters:** None

Returns:
`int` of the largest item id from the url: `https://hacker-news.firebaseio.com/v0/maxitem.json`

- `get_item_by_id`

**Parameters:**

| Name  | Type | Required | Description                           | Default
| ----- | ---- | -------- | ------------------------------------- | -------
| `id`  | int  | Yes      | unique `Item` id of Hacker News story | None

Returns:
`Item` representing the Hacker News story with given `id` fetched
from url: `https://hacker-news.firebaseio.com/v0/item/<item_id>.json`

- `get_user_by_id`

**Parameters:**

| Name  | Type | Required | Description                           | Default
| ----- | ---- | -------- | ------------------------------------- | -------
| `id`  | int  | Yes      | unique `Item` id of Hacker News story | None

Returns:
`User` representing the Hacker News user with given `id` fetched
from url: `https://hacker-news.firebaseio.com/v0/user/<user_id>.json`

### Class: `Item`

Stories, comments, jobs, Ask HNs and even polls are just items. They're identified by their ids, which are unique integers.

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
kids | list of `Item` of this item's comments, in ranked display order.
url | The URL of the story.
score | The story's score, or the votes for a pollopt.
title | The title of the story, poll or job.
parts | A list of related pollopts, in display order.
descendants | In the case of stories or polls, the total comment count.

### Class: `User`

Users are identified by case-sensitive ids. Only users that have public activity (comments or story submissions) on the site are available through the API.

Field | Description
------|------------
**id** | The user's unique username. Case-sensitive. Required.
delay | Delay in minutes between a comment's creation and its visibility to other users.
**created** | Creation date of the user, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
**karma** | The user's karma.
about | The user's optional self-description. HTML.
submitted | List of the user's stories, polls and comments.

## Screenshot

![Hacker News Client](/screenshots/hackernews-client-screenshot.png?raw=true "Bash shell running example.py script")

## Authors

* **Sameen Islam** - [samisnotinsane](https://github.com/samisnotinsane)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* Author of [haxor](https://github.com/avinassh/haxor) whose library inspired me to make my first Python library
* Author of [python-packaging](http://veekaybee.github.io/2017/09/26/python-packaging/) whose tutorial helped me get my head around the Python import system
