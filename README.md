# Reddit on Messenger

A personal use inteded facebook messenger bot that takes commands to interface with reddit and reply with posts as messages.

  - Send a command to the bot on messenger
  - Replies with what you want from reddit

 ![img](https://raw.githubusercontent.com/jml63/Reddit-on-Messenger/master/ss1.png) ![img](https://raw.githubusercontent.com/jml63/Reddit-on-Messenger/master/ss2.png)

### Tech

The tech used in making this:

* [Python] - The backend is made in Python 3
* [Pymessenger] - A python wrapper for facebook messenger
* [Flask] - A micro web framework written in Python
* [Praw] - A python wrapper for reddit api

Also used is [Pythonanywhere] to host the backend and [Facebook for Developers] to set up the bot

### Set it up yourself

Setup an app and page for the bot on [Facebook for Developers] and setup webhooks and tokens.
Setup an app on [Reddit] to get a client_id and client_secret for [Praw].
Host the code locally or on a service like [Pythonanywhere] with dependencies installed.

The current hardcoded commands are:
!reddit : returns usage information
!reddit <subreddit> : returns top 3 posts
!reddit <subreddit> <num> : returns top n posts with a postID and points for each
!reddit -g <postID> <num> : returns nth top level comment for a given postID

E.g:
**!reddit leagueoflegends 1** would return **(8xn4fg) 33pts - Free Talk...Tuesday? - July 10th**
Then using the id **!reddit -g  8xn4fg 0** would return the first comment on that post: **"Last monday I started my new job at..."**


[//]: #


[Python]: <https://www.python.org/>
[Pymessenger]:  <https://github.com/davidchua/pymessenger>
[Flask]: <https://github.com/pallets/flask>
[Praw]: <https://github.com/praw-dev/praw>
[Reddit]: <https://www.reddit.com/>

[Pythonanywhere]: <https://www.pythonanywhere.com>
[Facebook for Developers]: <https://developers.facebook.com>
