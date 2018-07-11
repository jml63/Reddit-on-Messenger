from flask import Flask, request
from pymessenger.bot import Bot
import praw

app = Flask(__name__)
ACCESS_TOKEN = ''
VERIFY_TOKEN = ''
bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        # Before allowing people to message your bot, Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook.
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if "!reddit" in message['message'].get('text'):
                    parsed = message['message'].get('text').split(" ")
                    if len(parsed) == 1:
                        send_message(recipient_id, "Use !reddit <subreddit> or !reddit <subreddit> <number of posts> to get top posts on a subreddit. Then use !reddit -g <postID> <comment number> to get a given comment on the post ID.")
                    if len(parsed) == 2:
                        response_sent_text = get_message(parsed[1], 3)
                        for i in range(len(response_sent_text)):
                            send_message(recipient_id, response_sent_text[i])
                    if len(parsed) == 3:
                        response_sent_text = get_message(parsed[1], parsed[2])
                        for i in range(len(response_sent_text)):
                            send_message(recipient_id, response_sent_text[i])
                    if len(parsed) == 4:
                        if parsed[1] == "-g":
                            response_sent_text = get_comments(parsed[2], parsed[3])
                            for i in range(len(response_sent_text)):
                                send_message(recipient_id, response_sent_text[i])

                if message['message'].get('text') in ["!help" , "help" , "h" , "-h"]:
                    response_sent_text = "Use !reddit"
                    send_message(recipient_id, response_sent_text)
    return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def get_message(arg1, arg2):
    reddit = praw.Reddit(client_id='WeiUoJOkdEKqDQ',
                     client_secret='hv-zHbbNuPfSSNYUpCqmQO8yXq0',
                     user_agent='my user agent')

    a=[]
    try:
        for submission in reddit.subreddit(arg1).hot(limit=int(arg2)):
            a.append('(' + str(submission.id) + ') ' + str(submission.score) + 'pts - ' + submission.title)
    except Exception as e:
        a.append("No such subreddit")
    return a

def get_comments(arg1, arg2):
    reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='my user agent')

    a=[]
    try:
        submission = reddit.submission(id=arg1)
        a.append(submission.comments[int(arg2)].body)
    except Exception as e:
        a.append("No comments found")
    return a


if __name__ == '__main__':
    app.run()