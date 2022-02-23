#!/usr/bin/env python3

import tweepy
import csv

#authorisation
client = tweepy.Client(bearer_token = "AAAAAAAAAAAAAAAAAAAAAL91YwEAAAAA5XlWqJ5GrnjeYCrdVBNbIduUwRA%3DtPho0u7yju3sE0VoEs0L2EJdBDyFp97rOEUgOVaRRGLpn8siJt" , wait_on_rate_limit = True)

#for reading text file containing hashtags and appending to a list
Hashtags = []
with open("/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with Tweets/Hashtags.txt", "r") as infile:
	hashtags = infile.readlines()
	for hash in hashtags:
		Hashtags.append(hash)

#for opening csv file to write to
with open("/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with Tweets/Tweets_Data.csv", "a") as outfile:
	csvWriter = csv.writer(outfile)
	csvWriter.writerow(["Index","Sub-Index","Hashtag","ID","Text"])
	
	#for indexing the csv file
	i = 1
	
	for hash in Hashtags:
		count = 1
		#for pulling tweets, no need to put limit as default is max
		for tweet in tweepy.Paginator(client.search_recent_tweets,query=hash + " lang:en -is:retweet",max_results=100).flatten(limit=25000): 
			
			#for writing to csv
			csvWriter.writerow([i,count,hash,tweet.id,tweet.text])
			
			#for printing on the output terminal
			print(i,'\n')
			
			count += 1
			i += 1
			
with open("/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with Tweets/Tweets_Data.txt","w") as outfile:
	for hash in Hashtags:
		for tweet in tweepy.Paginator(client.search_recent_tweets, query=hash + " lang:en -is:retweet", max_results=100).flatten(limit=25000):
			outfile.write(tweet.text)
	
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import os

stemmer=SnowballStemmer("english")
STOPWORDS = set(stopwords.words("english"))

def write_counts(counts, filepath):
	with open(filepath, "w") as outfile:
		for word in counts.keys():
			to_write = word + " : " + str(counts[word]) + "\n"
			outfile.write(to_write)
			
			
def get_counts(infilename):
	with open(infilename,"r", encoding="utf8", errors='ignore') as infile:
		text=infile.read()
		
	tokens = word_tokenize(text)
	words = [word.lower() for word in tokens if word.isalpha()]
	words=[stemmer.stem(word) for word in words if word not in STOPWORDS]
	
	counts = {}
	for word in words:
		counts[word] = counts.get(word, 0) + 1
		
	sorted_tuples = sorted(counts.items(), key=lambda item: item[1], reverse=True)
	sorted_counts = {k: v for k, v in sorted_tuples}
	return sorted_counts

counts=get_counts("/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with Tweets/Tweets_Data.txt")
write_counts(counts,"/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with Tweets/Word_count.txt")

	