import praw
from time import sleep

class Commenter:

    def __init__(self, client):
        self.reddit_client = client


    def reply_if_havent_replied(self, comment, message):
        if not have_replied(comment):
            comment.reply(message)

    def have_replied(self, comment):
        ### sees if the comment supplied has been replied to by this bot
        comment.refresh()
        comment.replies.replace_more(limit=0)
        for re in comment.replies.list():
            if re.author == self.reddit_client.config.username:
                return True
        return False


def mp_search(search_str):
    return search_str

def format_mp_result(search_result):
    return search_result

def get_reddit_client():
    # TODO: configurable
    return praw.Reddit(user_agent='route_bot 0.1',
                      client_id='z22NNQVWpd926A',
                      client_secret='HG2CfwKP1yKa0oxRXe69knAcndE',
                      username='freesodaforallhumans',
                      password='humansaregreatilovethem'
                      )

def Run():
    # Main business logic 
    print("Running app...")
    bot = get_reddit_client()
    commenter = Commenter(bot)
    
    print("Reddit Client loaded successfully")


    # TODO: Make this the right reddit/configurable
    subreddit = bot.subreddit('routebottest')

    comments = subreddit.stream.comments()
    print("Searching through comments...")
    for comment in comments:
        if commenter.have_replied(comment):
            # Skip this comment if we've replied to it
            continue

        text = comment.body.lower()
        bot_call_str = '!route_bot' 

        reply_str = parse_reply(text, bot_call_str)
        if reply_str:
            # reply with result
            comment.reply(reply_str)

        # Don't do anything if we can't find a good result
    print("Finished comment search")

def parse_reply(text, call_str):
    if call_str in text:
        try_split = text.split(call_str)
        search_string = try_split[-1].strip() if len(try_split) >=2 else None
        if search_string:
            # search
            result = mp_search(search_string)
            if result:
                return format_mp_result(result)
    return None

if __name__ == "__main__":
    while(True):
        Run()
        sleep(30)