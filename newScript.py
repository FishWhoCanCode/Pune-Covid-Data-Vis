import tweepy
import keyData as key
import pandas as pd

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
	if 'एक्टिव्ह रुग्णसंख्या' in text:
		cleanedNums.pop(0)
	return cleanedNums

#myClient = tp.Client(bearer_token = key.bearer_token)
auth = tweepy.OAuthHandler(key.api_key, key.api_secret)
auth.set_access_token(key.access_token, key.access_secret)

api = tweepy.API(auth)
#public_tweets = api.home_timeline()
file = open('C:\\Users\\arvni\\OneDrive\\Desktop\\Tweepy Test\\rawTweets.txt', 'a', encoding = 'utf-8')
s = 'mohol_murlidhar'

test_search = api.search_full_archive(label = 'archive', query = 'पुणे कोरोना अपडेट',\
									  toDate = 202004100000, maxResults = 100)
data = []
'''
for twt in test_search:
	if twt.user.screen_name == 'mohol_murlidhar':
		print(str(twt.created_at))
		if hasattr(twt, 'extended_tweet'):
			nums = [str(twt.created_at)] + getDataFromTweet(twt.extended_tweet['full_text'])
			file.write(twt.extended_tweet['full_text'] + '\n')
		else:
			nums = [str(twt.created_at)] + getDataFromTweet(twt.text)
			file.write(twt.text + '\n')
		print(f'{nums} {len(nums)}')
		data.append(nums)
'''
for twt in test_search:
	if twt.user.screen_name == 'mohol_murlidhar':
		print(str(twt.created_at))
		if hasattr(twt, 'extended_tweet'):
			file.write(twt.extended_tweet['full_text'] + '\n\n')
		else:
			file.write(twt.text + '\n\n')


df = pd.DataFrame(data, columns = \
				 ['Formatted Date', 'Date', 'Treatment started', 'New Patients', 'NP Total',\
				  'Discharged', 'Dis Total', 'Tests', 'T Total',\
				  'Deaths', 'D Total'])
#print(df)

df.to_csv('C:\\Users\\arvni\\OneDrive\\Desktop\\Tweepy Test\\file1.csv', mode = 'a', header = False)