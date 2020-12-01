import tweepy

ACCESS_TOKEN = 'enter_acces_token_here'
ACCESS_TOKEN_SECRET = 'enter_acces_token_secret_key_here'
API_KEY = 'enter_api_key_here'
API_SECRET_KEY = 'enter_api_secret_key_here'

#setting up the api
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#read the file containing the latest tweet id
with open("id_file.text") as f:
	last_seen_id = f.readline().rstrip()

#returns the 20 most recent mentions, including retweets. (basically anytime someone @'s you)
mentions = api.mentions_timeline(last_seen_id)

for mention in mentions:
	print(str(mention.id) + '-----' + mention.text.lower())

#store the new latest id in the file 
try: 
	last_seen_id = mentions[0].id 
except:
	print("No new tweets with your mention")
with open("id_file.text", "w") as f:
	f.write(str(last_seen_id))

	
