import sqlite3
import tweepy
from textblob import TextBlob
import csv


def createtable():
	cur.execute('DROP TABLE IF EXISTS TwitterTweets')
	cur.execute("CREATE TABLE TwitterTweets(count INT,Tweet TEXT,SentimentValue Varchar)")
#Inserting to the sql table
def insertvalue(count,tweet,SentimentValue):
	cur.execute("INSERT INTO TwitterTweets(count,Tweet,SentimentValue) values(?,?,?)",(count,tweet,SentimentValue))
	conn.commit()

#writing to the file 
def Fileinsert(count,tweet,SentimentalValue):
	file.write("Tweet {} : {} \n The sentiment analysis value is : {} \n\n".format(count,tweet,SentimentalValue))

#writing to the CSV file
def writecsv(count,tweet,SentimentalValue):
	writer.writerow([count,tweet,SentimentalValue])

#SQl connection
#conn=sqlite3.connect('twittedata.sqlite')
#cur=conn.cursor()
#createtable()

#Twitter authentication
consumer_key= 'Z8eLyPMg1dam34J8T7ZUrqdHM'
consumer_secret= 'Hjt3I4Y2UHfxp2qakE8Rpx8GT9UyuWoAOykAX6I6NPus7HBC44'
access_token= '40830887-4TVWuTQj1PestQJfowBfAh6wNYGLiwywh1tUWvlY7'
acces_token_secret= 'qSctR7rTR5eEYzp1iZ2QN7tKuYVEinNWTRkDiq0EqA3Ye'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acces_token_secret)
api=tweepy.API(auth)

#creating a file
#file=open('tweets.txt','w+')


#CSV CREATION
#csvfile=open('tweets.csv','w')
#writer=csv.writer(csvfile)
#CSV header
#writer.writerow(['count','Tweet','Sentimental_value'])

#Getting user input 
tag=str(input("Enter the Hashtag you want to search in twitter : "))
options=str(input("The formats in which the output can be Generated  \n\t 1.CSV or Excel\n\t 2.Text\n\t 3.SQL database\n What are the formats in which you want the result  : " ).lower().strip().split())


public_tweets=api.search(tag)
count = 1
positive_count=0
negative_count=0
netural_count=0
if('csv' in options and 'text' in options and 'sql' in options):
	#creating a file
	file=open('tweets.txt','w+')
	#CSV CREATION
	csvfile=open('tweets.csv','w')
	writer=csv.writer(csvfile)
	#CSV header
	writer.writerow(['count','Tweet','Sentimental_value'])
	#SQl connection
	conn=sqlite3.connect('twittedata.sqlite')
	cur=conn.cursor()
	createtable()
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		insertvalue(count,tweet.text,Sentimental_value)
		Fileinsert(count,tweet.text,Sentimental_value)
		writecsv(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1
elif('csv' in options and 'text' in options):
	#creating a file
	file=open('tweets.txt','w+')
	#CSV CREATION
	csvfile=open('tweets.csv','w')
	writer=csv.writer(csvfile)
	#CSV header
	writer.writerow(['count','Tweet','Sentimental_value'])
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		Fileinsert(count,tweet.text,Sentimental_value)
		writecsv(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1
	writer.writerow(['positive Tweet %',positive_count])
	writer.writerow(['Negative Tweet %',negative_count])
	writer.writerow(['Netural Tweet %',netural_count])
elif('csv' in options and 'sql' in options):
	#CSV CREATION
	csvfile=open('tweets.csv','w')
	writer=csv.writer(csvfile)
	#CSV header
	writer.writerow(['count','Tweet','Sentimental_value'])
	#SQl connection
	conn=sqlite3.connect('twittedata.sqlite')
	cur=conn.cursor()
	createtable()
	createtable()
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		insertvalue(count,tweet.text,Sentimental_value)
		writecsv(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1
	writer.writerow(['positive Tweet %',positive_count])
	writer.writerow(['Negative Tweet %',negative_count])
	writer.writerow(['Netural Tweet %',netural_count])

elif('text' in options and 'sql' in options):
	#creating a file
	file=open('tweets.txt','w+')
	#SQl connection
	conn=sqlite3.connect('twittedata.sqlite')
	cur=conn.cursor()
	createtable()
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		insertvalue(count,tweet.text,Sentimental_value)
		Fileinsert(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1

elif('csv' in options):
	#CSV CREATION
	csvfile=open('tweets.csv','w')
	writer=csv.writer(csvfile)
	#CSV header
	writer.writerow(['count','Tweet','Sentimental_value'])
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		writecsv(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1
	writer.writerow(['positive Tweet %',positive_count])
	writer.writerow(['Negative Tweet %',negative_count])
	writer.writerow(['Netural Tweet %',netural_count])
elif('text' in options):
	#creating a file
	file=open('tweets.txt','w+')
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		Fileinsert(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1
elif('sql' in options):
	#SQl connection
	conn=sqlite3.connect('twittedata.sqlite')
	cur=conn.cursor()
	createtable()
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		insertvalue(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1
else:
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		Sentimental_value=analysis.sentiment.polarity
		if(Sentimental_value>0.0):
			Sentimental_value='Postivie'
			positive_count += 1
		elif(Sentimental_value<0.0):
			Sentimental_value='Negative'
			negative_count += 1
		elif(Sentimental_value==0.0):
			Sentimental_value='Neutral'
			netural_count += 1 
		print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
		insertvalue(count,tweet.text,Sentimental_value)
		Fileinsert(count,tweet.text,Sentimental_value)
		writecsv(count,tweet.text,Sentimental_value)
		print("Insert query executed ")
		count=count+1
	

'''for tweet in public_tweets:
	analysis=TextBlob(tweet.text)
	Sentimental_value=analysis.sentiment.polarity
	if(Sentimental_value>0.0):
		Sentimental_value='Postivie'
		positive_count += 1
	elif(Sentimental_value<0.0):
		Sentimental_value='Negative'
		negative_count += 1
	elif(Sentimental_value==0.0):
		Sentimental_value='Neutral'
		netural_count += 1 
	print(" Tweet {} : {} \n The sentiment analysis value is : {} ".format(count,tweet.text,Sentimental_value))
	insertvalue(count,tweet.text,Sentimental_value)
	Fileinsert(count,tweet.text,Sentimental_value)
	writecsv(count,tweet.text,Sentimental_value)
	print("Insert query executed ")
	count=count+1'''
print("Postive Tweet %  = {} \nNegative Tweet % = {} \nNetural Tweet % = {}".format(float((positive_count/count)*100),float((negative_count/count)*100),float((netural_count/count)*100)))
print("\tPostive Tweets = {} \n\tNegative Tweets = {} \n\tNetural Tweets = {}".format(positive_count,negative_count,netural_count))



print('The option are ',options)