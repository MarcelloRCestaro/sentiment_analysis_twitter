import tweepy
import pandas as pd
import numpy as np
from tqdm import tqdm

def down_tweets(input_file):
    messages = []

    auth = tweepy.OAuthHandler('NPCJD0mQaAXGNqzFIGHDt6sCm', 'p860wJZ9q2qkyqcpryxJlQQ4AWezkQ1htjFIdNDuyXzifO8JEl')
    auth.set_access_token('968903194473648132-I6C9IbrbP8hWkARR4aM7mblV0M5OdhK', 'CX7AX97vPbns0P9BnfBmLlPbWBuR8SpfLEFahg3Vru6Ns')
    api = tweepy.API(auth)

    with open("output.txt", "w") as f:
        for tt_id in tqdm(list(input_file)):
            try:
                tweet = api.get_status(tt_id)
                f.write(str(tt_id))
                f.write('\t')
                f.write(tweet.text)
                f.write('\n')
                messages.append(tweet.text)
            except tweepy.error.TweepError:
                f.write('?')
                f.write('\n')


data = pd.read_csv('tweetSentimentBR.txt', sep='\t', header = None)
data.columns = ['ID', 'Hashtag', 'Vetor', '?', 'Sentimento']
id_tweets = list(data['ID'])
np_id = np.array(id_tweets)
down_tweets(np_id)
