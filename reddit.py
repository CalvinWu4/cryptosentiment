import praw

def getSubmissionsText(name):
    r = praw.Reddit(client_id='Ad0uCgzte8_czQ',
                    client_secret='GupwwnCEzEFKH9Se926xi_ZY77A',
                    user_agent='cryptoapp by /u/NeonCrayon1')

    submissions = r.subreddit(name).top(limit=50)

    result = ""
    for submission in submissions:
        result += submission.selftext + ". "
        # print "=" * 30

    return result

if __name__ == '__main__':
    print getSubmissionsText()

#     # print submission.title
#     # print submission.url
#
#     print "=" * 30
#     submission.comments.replace_more(limit=0)
#     comments = submission.comments.list()
#
#     # submission.comments = sorted(submission.comments, key=lambda x: x.score)
#     # flat_comments = praw.helpers.flatten_tree(submission.comments)
#
#     for comment in submission.comments[0:6]:
# #     for comment in flat_comments:
#         print comment.body
#         # print "score: " + str(comment)
#         print "#" * 10
#     print "\n" * 3
