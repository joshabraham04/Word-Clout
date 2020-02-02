import csv
import ExclusionDictionary
from TweetScraper import getTweets
from textblob import TextBlob

# Library that seperates strings into individual words
TweetBlob = TextBlob

tweetCount = 0
TweetBox = []  # array of string objects
WordBox = []
fileName = ""  
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
            lines[i] = lines[i].translate({ord(x): None for x in 'rtœrtâ€™ðÿ‘ðÿ¼ðÿ‡ºðÿ‡¸ðÿ’Ÿ˜Ÿ'})
        f.seek(0)
        # Removes the whitespaces
        f.writelines(line for line in lines if line.strip())
        f.truncate()
        f.close()

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
    elif candidateName == 'tulsiGabbard':
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
        print("No candidate recognized, double check the name." )

###################
# FILE PROCESSING #
###################

# List of 2020 presidential candidates
candidates = ["MichaelBennet", "JoeBiden", "MikeBloomberg", "PeteButtigieg", "TulsiGabbard",
              "AmyKlobuchar", "DevalPatrick", "BernieSanders", "TomSteyer", "EWarren",
              "AndrewYang", "RealDonaldTrump", "WalshFreedom", "GovBillWeld"]

# Collect tweets into datasets
#for x in candidates:
 #   getTweets(x)

# Menu and Candidate Choice
while True:
    try:
        candidateName = input("Choose your candidate: ")
        break
    except ValueError:
        print("That's not a valid name! Try again!")
    
# Normalizes the name answers and assign files
candidateName = candidateName.lower().replace(" ", "")
fileName = CSVfilename(candidateName)
DataCleaner(fileName)

with open("Tweets Scraped/" + fileName) as csv_file:
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
        for occurence in range (0, candidateDictionary[word]):
            wordMap +=  (word + " ")
        
    #print(wordMap)
    
    
    
    
    
    
    
    
    
    
    