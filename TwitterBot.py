import tweepy, random

ACCESS_TOKEN = 'enter_acces_token_here'
ACCESS_TOKEN_SECRET = 'enter_acces_token_secret_key_here'
API_KEY = 'enter_api_key_here'
API_SECRET_KEY = 'enter_api_secret_key_here'

#setting up the api
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

substring = '#raiseawareness'

#create list of articles 
articles = []
file = open("articles.text")
for line in file:
	articles.append(line.rstrip())

#read the file containing the latest tweet id
with open("id_file.text") as f:
	last_seen_id = f.readline().rstrip()

#returns the 20 most recent mentions, including retweets. (basically anytime someone @'s you)
mentions = api.mentions_timeline(last_seen_id)

#check if there are any new tweets and reply if conditions are met
try: 
	last_seen_id = mentions[0].id 
	if last_seen_id:
		counter = 0
		for mention in mentions:
			if substring in mention.text.lower():
				article = random.choice(articles)
				api.update_status("Here's todays article. \n" + article, mention.id, True)
				counter+=1
		print("Replied to " + str(counter) + " tweets")		
except:
	print("No new tweets contain the specified hashtag")

with open("id_file.text", "w") as f:
	f.write(str(last_seen_id))



	
