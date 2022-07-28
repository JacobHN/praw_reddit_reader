import praw
from text_to_speech import TextToSpeech
from key.config import client_secret, client_id

ts = TextToSpeech(1)

# create a reddit developer account to access praw features and input your given client_id and client_secret
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='tutorial')

subreddit = reddit.subreddit("relationship_advice").top(time_filter="day", limit=3)
f = open("text_files/test3.txt", "a")


# traverse through the reply thread recursively
def reply_thread(reply_adult):
    if reply_adult.author.name is not None:
        print("by " + reply_adult.author.name)
    print(reply_adult.body)
    if len(reply.replies) > 0:
        for reply_child in reply_adult.replies:
            print("----")
            print("reply to " + reply_adult.author.name)
            reply_thread(reply_child)


# loop through given reddit post, print post text, title, author. Then, text to speech post.
for submission in subreddit:
    if submission.stickied:
        continue
    print(submission.url)

    title = submission.title
    body = submission.selftext
    print(title)

    ts.speak(submission.author.name + " Posted " + title)
    print(body)
    ts.speak(body)
    f.write(submission.url + "\n" + title + "\n" + body)

    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        single_comment = comment.body
        comment_author = comment.author
        if comment_author is None or comment_author.name == "AutoModerator":
            continue
        print("-----------------------------")
        print(comment_author)
        print(single_comment)
        ts.speak(comment_author.name + " states " + single_comment)
        if len(comment.replies) > 0:
            for reply in comment.replies:
                print("----")
                print("reply to " + comment.author.name)
                reply_thread(reply)

    ts.stop()
    f.close()
