import tweepy
import csv
import json

# List of 2020 presidential candidates
candidates = ["MichaelBennet", "JoeBiden", "MikeBloomberg", "PeteButtigieg", "TulsiGabbard",
              "AmyKlobuchar", "DevalPatrick", "BernieSanders", "TomSteyer", "EWarren",
              "AndrewYang", "RealDonaldTrump", "WalshFreedom", "GovBillWeld"]

# load Twitter API credentials
with open('C:/Users/Josh Abraham/Desktop/SwampHacks/Twitter Analysis/Twitter-Politics-WebScraper/TwitterCredentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['Consumer_Key']
    consumer_secret = info['Consumer_Secret']
    access_key = info['Access_Key']
    access_secret = info['Access_Secret']
    
def getTweets(screenName):
    
    # Authorization and initialization    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    # List for all the tweets
    tweetList = []
    
    # We will get the tweets with multiple requests of 200 tweets each
    newTweets = api.user_timeline(screen_name=screenName, tweet_mode='extended', count=200)
    
    # saving the most recent tweets
    tweetList.extend(newTweets)
    
    # save id of 1 less than the oldest tweet
    oldestTweet = tweetList[-1].id - 1
    
    # grabbing tweets till none are left
    print("Collecting " + screenName + " tweets")
    while len(newTweets):
        
        # The max_id param will be used subsequently to prevent duplicates
        newTweets = api.user_timeline(screen_name=screenName, tweet_mode='extended', count=200, max_id=oldestTweet)
        
        # save most recent tweets
        tweetList.extend(newTweets)
        
        # id is updated to oldest tweet - 1 to keep track
        oldestTweet = tweetList[-1].id - 1
        
        # transforming the tweets into a 2D array that will be used to populate the csv
        outTweets = [[tweet.id_str, tweet.created_at, tweet.full_text] for tweet in tweetList]
    
        #writing to the csv file
        with open(screenName + '_Tweets.csv', 'w', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Timestamp', 'Content'])
            writer.writerows(outTweets)
       
for x in candidates:
    getTweets(x)