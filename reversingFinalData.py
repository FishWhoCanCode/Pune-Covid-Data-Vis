import pandas as pd

file = open('C:\\Users\\arvni\\OneDrive\\Desktop\\Tweepy Test\\file.csv', 'r', encoding = 'utf-8')

df = pd.read_csv('C:\\Users\\arvni\\OneDrive\\Desktop\\Tweepy Test\\file.csv', dtype = str, index_col = 0)
df_new = df.reindex(index = df.index[::-1])
df_new.to_csv('C:\\Users\\arvni\\OneDrive\\Desktop\\Tweepy Test\\orderedFile.csv')