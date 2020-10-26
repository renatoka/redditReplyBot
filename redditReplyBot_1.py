import praw
import time
import random

reddit = praw.Reddit(
    client_id = "",
    client_secret = "",
    user_agent = "",
    password = "",
    username = "")


#Change to your own subreddit of choice.
#Just type its name after r/
subreddit = reddit.subreddit("all")

#Edit your own reply phrase.
reply_phrase = "Your reply phrase"
#This will end your while loop
already_exist = True

#Change this limit to whichever you like, also you can change to check
##subreddit.hot, subreddit.new, subreddit.top
for submission in subreddit.new(limit = 5):
    ## THIS PART IS KNOWN TO GET BUGGY SO IF YOU DON'T WANT TO CHECK
    ## POST TITLE'S JUST COMMENT OUT FROM HERE
    for post_title in submission.title:
        while (already_exist != False):
            #Edit your own trigger TITLE word 
            if "your trigger word" in submission.title:
                submission.reply(reply_phrase)
                print("One trigger word was found in this title: {0}".format(submission.title))
                print("I replied with my phrase : {0}".format(reply_phrase))
                print("---------------")
                already_exist = False
                time.sleep(10)
            else:
                print("Already commented on it or post with trigger words doesn't exist.")
                already_exist = False
    ## TO HERE ^^
    
    ##This part works normally and it checks if there are your target words
    ##inside of post comments.
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if (reply_phrase in comment.body):
                print("Reply phrase already found, skipping this comment.")
                
            #Edit your trigger comment word here.
            elif("your trigger comment word" in comment.body):
                comment.reply(reply_phrase)
                print("Trigger word was found in this comment : {0}".format(comment_lower))
                print("---------------")
                print("I replied on thread named : {0}".format(submission.title))
                print("---------------")
                time.sleep(800)
