from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy import Cursor
from slistener import *

my_key = 'iAzUoi7PBgAnp2oHBtZ65eWn4'
my_key_secret = 'PR3ugQlELaW99Xbe74E5eWf4EX43n9VWStlT8UAzi76mWO64xd'
access_token = '1159089840631111680-YnveiOy2IdxrHxAIR4h6rpJ9pmEAU9'
access_token_secret = 'eHxIOVC8i6f1vinfZbtgexKmmYMnXxY9b3qdlPgWwpSea'

# Consumer key authentication
auth = OAuthHandler(my_key, my_key_secret)

# Access key authentication
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api = API(auth)

# Set up keywords to track
keywords_to_track = ['#preseason #leagueoflegends']

# Instantiate the SListener object
listen = SListener(api)

# Instantiate the Stream object
stream = Stream(auth, listen)

# Instantiate the Cursor object
#cursor = Cursor(api.search, q='#preseason #leagueoflegends', lang="en", include_retweets=False)

# Begin collecting data
stream.filter(track = keywords_to_track)


# f = open("tweets.txt", "a+", encoding='utf-8')
# for id, tweet in enumerate(cursor.items(200)):
#     #print(tweet.text)
#     f.write(tweet.text)
#     f.write('\n')
# f.close()




