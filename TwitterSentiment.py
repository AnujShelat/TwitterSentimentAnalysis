import sys, tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# consumer key, consumer secret, access token, access secret.
ckey = ""
csecret = ""
atoken = ""
asecret = ""

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

def percentage(x, y):
    return 100 * float(x)/float(y)

keyword = input("Enter keyword: ")
nSearches = int(500)

tweets = tweepy.Cursor(api.search, q=keyword, lang="English").items(nSearches)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0):
        negative += 1
    elif (analysis.sentiment.polarity > 0):
        positive += 1

neutral = percentage(neutral, nSearches)
negative = percentage(negative, nSearches)
positive = percentage(positive, nSearches)
polarity = percentage(polarity, nSearches)

neutral = format(neutral, '.2f')
negative = format(negative, '.2f')
positive = format(positive, '.2f')


if (polarity == 0):
    print("Neutral")
elif (polarity < 0.00):
    print("Negative")
elif (polarity > 0.00):
    print("Positive")

labels = ['Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]','Positive ['+str(positive)+'%]']
sizes = [neutral, negative, positive]
colors = ['gold', 'red', 'yellowgreen']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('Sentiment Analysis on '+keyword+'')
plt.axis('equal')
plt.tight_layout()
plt.show()