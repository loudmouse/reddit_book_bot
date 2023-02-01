from bot import Bot
from configparser import ConfigParser

config = ConfigParser()
config.read('praw.ini')
config = config["DEFAULT"]

failures = 0
while True:
    try:
        bot = Bot()
        bot.listen_to_subreddit(config["subreddit"])
    except Exception as e:
        failures += 1