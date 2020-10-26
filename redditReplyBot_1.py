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


for submission in subreddit.new(limit = 5):
    for naslov in submission.title:
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





























            #if " omjer cijene " in comment_lower:
            #    print("-------")
            #    print("Name of thread : {0}".format(submission.title))
            #    print("Comment : {0}".format(comment.body))
            #    print("Author of the comment : {0}".format(comment.author))

                #if (reply_phrase in comment.body):
                #    print("Reply phrase found, skipping this comment.")

                #else:
                #    comment.reply(reply_phrase)
                #    print("Word ""omjer cijene"" was found in this comment : {0}".format(comment_lower))
                #    print("---------------")
                #    print("I replied on thread named : {0}".format(submission.title))
                #    print("---------------")
                #    time.sleep(10)


    #for naslov in submission.title:
    #    izabrana_rijec = random.randint(0,len(rijeci))
    #    if str(izabrana_rijec) in submission.title:
    #        submission.reply(reply_phrase)
    #        print("Jedna od rijeci je pronadena u naslovu ovog threada : {0}".format(submission.title))
    #        print("Odgovorio sam na thread pod imenom {0} ".format(submission.title))
    #        print("---------------")
    #        time.sleep(30)

    #for naslov in submission.title:
    #    if "Gdje" in submission.title:
    #        submission.reply("Trazis najbolji omjer cijene i kvalitete? Pa to vec i ptice na grani znaju, Xiaomi.")
    #        time.sleep(780)

