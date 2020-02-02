#############################################
# RUN THESE FILES OFF WordCloudGenerator.py #
#############################################

import csv
import ExclusionDictionary
from TweetScraper import getTweets
from textblob import TextBlob

# Library that separates strings into individual words
TweetBlob = TextBlob

tweetCount = 0
TweetBox = []  # array of string objects
WordBox = []
fileName = ""  
imageName=""
wordMap = ""

###########
# METHODS #
###########

# Returns a dictionary of words and their frequency 
def WordCounter(str):
    counts = dict()
    words = str
    for word in words:
        if '\\' in word or '/' in word or '@' in word:
            continue
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    # Returns a dictionary
    return counts

# Cleans up the CSV Files and removes the white spaces and unicode 
def DataCleaner(file):
    with open(file, 'r+', errors='ignore') as f:
        # Converts the lines in the file into string lists
        lines = f.readlines()
        # For each line, removes the foreign characters and reassigns the line 
        for i in range(0, len(lines)):
            lines[i] = lines[i].translate({ord(x): None for x in 'œâ€™ðÿ‘ðÿ¼ðÿ‡ºðÿ‡¸ðÿ’Ÿ˜Ÿ'})
        f.seek(0)
        # Removes the whitespaces
        f.writelines(line for line in lines if line.strip())
        f.truncate()
        f.close()

# INCOMING: BLOCK OF CODE (too lazy to do it any better, my b)

# Parses through presidential candidates and retrieves datasets
def CSVfilename(candidateName):
    if candidateName == 'michaelbennet':
        fileName =  'MichaelBennet_Tweets.csv'
        return fileName
    elif candidateName == 'joebiden':
        fileName = 'JoeBiden_Tweets.csv'
        return fileName
    elif candidateName == 'mikebloomberg':
        fileName = 'MikeBloomberg_Tweets.csv'
        return fileName
    elif candidateName == 'petebuttigieg':
        fileName = 'PeteButtigieg_Tweets.csv'
        return fileName
    elif candidateName == 'tulsigabbard':
        fileName = 'TulsiGabbard_Tweets.csv'
        return fileName
    elif candidateName == 'amyklobuchar':
        fileName = 'AmyKlobuchar_Tweets.csv'
        return fileName
    elif candidateName == 'devalpatrick':
        fileName = 'DevalPatrick_Tweets.csv'
        return fileName
    elif candidateName == 'berniesanders':
        fileName = 'BernieSanders_Tweets.csv'
        return fileName
    elif candidateName == 'tomsteyer':
        fileName = 'TomSteyer_Tweets.csv'
        return fileName
    elif candidateName == 'elizabethwarren':
        fileName = 'EWarren_Tweets.csv'
        return fileName
    elif candidateName == 'andrewyang':
        fileName = 'AndrewYang_Tweets.csv'
        return fileName
    elif candidateName == 'donaldtrump':
        fileName = 'RealDonaldTrump_Tweets.csv'
        return fileName
    elif candidateName == 'joewalsh':
        fileName = 'WalshFreedom_Tweets.csv'
        return fileName
    elif candidateName == 'williamweld':
        fileName = 'GovBillWeld_Tweets.csv'
        return fileName
    else:
        print("No candidate recognized, double check the name.")

# Parses through presidential candidates and retrieves image files        
def imageProcessor(candidateName):
    if candidateName == 'michaelbennet':
        imageName = 'MichaelBennet.png'
        return imageName
    elif candidateName == 'joebiden':
        imageName = 'JoeBiden.png'
        return imageName
    elif candidateName == 'mikebloomberg':
        imageName = 'MikeBloomberg.png'
        return imageName
    elif candidateName == 'petebuttigieg':
        imageName = 'PeteButtigieg.png'
        return imageName
    elif candidateName == 'tulsigabbard':
        imageName = 'TulsiGabbard.png'
        return imageName
    elif candidateName == 'amyklobuchar':
        imageName = 'AmyKlobuchar.png'
        return imageName
    elif candidateName == 'devalpatrick':
        imageName = 'PatrickDeval.png'
        return imageName
    elif candidateName == 'berniesanders':
        imageName = 'BernieSanders.png'
        return imageName
    elif candidateName == 'tomsteyer':
        imageName = 'TomSteyer.png'
        return imageName
    elif candidateName == 'elizabethwarren':
        imageName = 'EWarren.png'
        return imageName
    elif candidateName == 'andrewyang':
        imageName = 'AndrewYang.png'
        return imageName
    elif candidateName == 'donaldtrump':
        imageName = 'RealDonaldTrump.png'
        return imageName
    elif candidateName == 'joewalsh':
        imageName = 'WalshFreedom.png'
        return imageName
    elif candidateName == 'williamweld':
        imageName = 'GovBillWeld.png'
        return imageName
    else:
        print("No image file found, try again." )

###################
# FILE PROCESSING #
###################

# List of 2020 presidential candidates
candidates = ["MichaelBennet", "JoeBiden", "MikeBloomberg", "PeteButtigieg", "TulsiGabbard",
              "AmyKlobuchar", "DevalPatrick", "BernieSanders", "TomSteyer", "EWarren",
              "AndrewYang", "RealDonaldTrump", "WalshFreedom", "GovBillWeld"]


# Menu, Collection of Tweets and Candidate Choice
print()
print("Welcome to the 2020 Presidential Candidates' \"Word Clout\"")
print("A comprehensive word cloud generator of each candidate's tweets")
collectTweets = input("Would you like to collect the latest presidential tweets? It may take a few minutes: " + "(" + "type yes/no" + ") ")
print()
if collectTweets == 'yes':
    for x in candidates:
        getTweets(x)
        
candidateName = input("Choose your candidate: ")

    
# Normalizes the name answers and assign files
candidateName = candidateName.lower().replace(" ", "")
fileName = CSVfilename(candidateName)
imageName = imageProcessor(candidateName)
fileName = 'Tweets Scraped/' + fileName
DataCleaner(fileName)
    
with open(fileName) as csv_file:
    TestData2 = csv.reader(csv_file, delimiter=',')
    for lines in TestData2:
        TweetBox.append(lines[2])
    for i in range(1, len(TweetBox)):
        wordsAdding = TweetBox[i].strip()
        wordsAdding = (wordsAdding.split(' '))
        for j in range(0, len(wordsAdding)):
            WordBox.append(wordsAdding[j].lower())
            WordBox[j].lower()
                
# Removes the excluded words from the dictionary (ie articles and auxiallary verbs) 
WordBox = ExclusionDictionary.removeExcluded(WordBox, ExclusionDictionary.excludedDictionary)
        
candidateDictionary = WordCounter(WordBox)
        
for word in candidateDictionary:
    for occurrence in range (0, candidateDictionary[word]):
        wordMap += (word + " ")