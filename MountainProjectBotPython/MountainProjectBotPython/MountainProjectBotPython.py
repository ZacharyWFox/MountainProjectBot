
import praw

def mp_search(search_str):
    return search_str

def format_mp_result(search_result):
    return search_result


print("Running app...")
bot = praw.Reddit(user_agent='route_bot 0.1',
                  client_id='z22NNQVWpd926A',
                  client_secret='HG2CfwKP1yKa0oxRXe69knAcndE',
                  username='freesodaforallhumans',
                  password='humansaregreatilovethem'
                  )
print("Reddit Client loaded successfully")

subreddit = bot.subreddit('routebottest')

comments = subreddit.stream.comments()
print("Searching through comments...")
for comment in comments:
    text = comment.body
    author = comment.author
    text = text.lower()
    bot_call_str = '!route_bot' 
    if bot_call_str in text:
        try_split = text.split(bot_call_str)
        search_string = try_split[-1].strip() if len(try_split) >=2 else None
        if search_string:
            # search
            result = mp_search(search_string)
            if result:
                reply_str = format_mp_result(result)
                # reply with result
                comment.reply(reply_str)
            # Don't do anything if we can't find a good result
print("Finished comment search")