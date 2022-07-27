import praw
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("time to wait for the program fucker")
engine.runAndWait()

reddit = praw.Reddit(client_id='QAuhXYE8V2hdDqfwFRGu7w',
                     client_secret='26bYFu-karUAS03kINKF6AxpKvcvWg',
                     user_agent='tutorial')


def reply_thread(reply_adult):
    print("by " + reply_adult.author.name)
    print(reply_adult.body)
    if len(reply.replies) > 0:
        for reply_child in reply_adult.replies:
            print("----")
            print("reply to " + reply_adult.author.name)
            reply_thread(reply_child)


# subreddit_name = input("enter subreddit(input is underscore and case sensitive):")
subreddit = reddit.subreddit("relationship_advice").top(time_filter="day", limit=3)

# file_name = input("input file name")
f = open("test3.txt", "a")

for submission in subreddit:
    if submission.stickied:
        continue
    print(submission.url)

    title = submission.title
    body = submission.selftext
    print(title)

    engine.say(submission.author.name + " Posted " + title)
    engine.runAndWait()
    print(body)
    engine.say(body)
    engine.runAndWait()
    f.write(submission.url)
    f.write(title)
    f.write(body)
    f.close()

    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        single_comment = comment.body
        comment_author = comment.author
        if comment_author is None or comment_author.name == "AutoModerator":
            continue
        print("-----------------------------")
        print(comment_author)
        print(single_comment)
        engine.say(comment_author.name + " states " + single_comment)
        engine.runAndWait()
        if len(comment.replies) > 0:
            for reply in comment.replies:
                print("----")
                print("reply to " + comment.author.name)
                reply_thread(reply)
