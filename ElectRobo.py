import csv
import pandas
from textblob import TextBlob
import ExclusionDictionary

tweetCount = 0
TweetBox = []  # array of string objects
WordBox = []

UniqueDictionary = []
Dictionary = []
TweetBlob = TextBlob
TestData = pandas.read_csv('SampleCSV.csv', delimiter=',', encoding='utf8')


def WordCounter(str):
    counts = dict()
    words = str
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def DataCleaner(file):
    bad_chars = ['\\xe2\\x80\\xa6', '\\xe2\\x80\\x94', '\\xe2\\x80\\x99s']
    with open(file, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()
        for x in f:
            for i in bad_chars:
                lines.replace(lines)
        f.close()


DataCleaner('JoeBiden_Tweets.csv')

with open('JoeBiden_Tweets.csv') as csv_file:
    TestData2 = csv.reader(csv_file, delimiter=',')
    # print(TestData2)
    for lines in TestData2:
        TweetBox.append(lines[2])
    for i in range(1, len(TweetBox)):
        wordsAdding = TweetBox[i].strip()
        wordsAdding = (wordsAdding.split(' '))
        for j in range(0, len(wordsAdding)):
            WordBox.append(wordsAdding[j].lower())
            WordBox[j].lower()
    WordBox = ExclusionDictionary.removeExcluded(WordBox, ExclusionDictionary.excludedDictionary)
    # print(WordBox)
    print(WordCounter(WordBox))
