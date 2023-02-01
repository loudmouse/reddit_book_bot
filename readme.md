# Background

At the start of 2023 the original reddit [goodreads-bot](https://www.reddit.com/user/goodreads-bot/) quit working when Goodreads deactivated the orginal bot's api key. When I saw the bot go down I decided to put something up in its place. This new bot, [thebookbot](https://www.reddit.com/user/thebookbot), is built very much on [the original work](https://github.com/rodohanna/reddit-goodreads-bot) done by [rodohanna](https://github.com/rodohanna). The major change with this new bot is that instead of pulling book data from the Goodreads API it instead pulls book data from the [Open Library API](https://openlibrary.org/developers/api).

## Overview

A Reddit bot that comments ~~GoodReads~~ [Open Library](https://openlibrary.org/developers/api) data when summoned.

Example:

If someone makes a comment like:

> I think you would like {The Bell Jar by Sylvia Plath}

The bot will add a comment with an OpenLibrary link, title of the book, author, number of pages, year published, and a description.

### Found a bug?

If you found a bug feel free to [log an issue here](https://github.com/loudmouse/reddit_book_bot/issues). Please include as much detail as you can when logging an issue.

For example:
1. provide an example of the bug with link and/or screenshot if possible
2. what did you expect to have happened?
3. what actually happened?

### Want to fix a bug?

Take a look at the [open issues](https://github.com/loudmouse/reddit_book_bot/issues). If you see something that looks fun to fix feel free to put up a PR for review. Thanks in advance for any time you put into trying to improve things around here.

### Run the code locally

##### Install dependencies

`pip3 install -r requirements.txt`

##### Start the program

`python3 driver.py`


###### Debugging locally

1. `import ipdb` into your file
2. `ipdb.set_trace()` where you'd like to halt code execution
3. run the program
