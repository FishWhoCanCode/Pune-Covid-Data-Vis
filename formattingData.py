import tweepy as tp
import keyData as key
import pandas as pd

client = tp.Client(bearer_token = key.bearer_token)

#filepath = Path('C:\\Users\\arvni\\OneDrive\\Desktop\\Tweepy Test\\file.csv')
mUser = 'mohol_murlidhar'
mId = 1006227561897185280

def getDataFromTweet(text):
	nums = []
	temp = ''
	for t in text:
		code = ord(t)
		if t == '\n' or t == '(':
			nums.append(temp)
			temp = ''
		elif 0x966 <= code <= 0x96f:
			temp += str(code-0x966)
	cleanedNums = [x for x in nums if x != '']
	return cleanedNums

def getData(iterations):
	lastTweetID = client.get_users_tweets(id = mId, max_results = 5).data[0]['id']
	numbersList = []

	for i in range(iterations):
		rawTweets = client.get_users_tweets(id = mId, exclude = 'retweets', max_results = 100, until_id = lastTweetID, tweet_fields = 'created_at')
		lastTweetID = rawTweets.meta['oldest_id']
		for twt in rawTweets.data:
			#print(twt.data)
			t = twt['text']
			if t.startswith('पुणे कोरोना अपडेट'):
				dataWithDate = getDataFromTweet(t)
				dataWithDate = [twt['created_at']] + dataWithDate
				numbersList.append(dataWithDate)
		print(f'Progress: {(i+1)*100/iterations:.2f}%', end = '\r')
	return numbersList

covidData = getData(29)
df = pd.DataFrame(covidData, columns = \
				 ['Formatted Date', 'Date', 'Treatment started', 'New Patients', 'NP Total',\
				  'Discharged', 'Dis Total', 'Tests', 'T Total',\
				  'Deaths', 'D Total'])
#print(df)

df.to_csv('C:\\Users\\arvni\\OneDrive\\Desktop\\Tweepy Test\\file.csv')