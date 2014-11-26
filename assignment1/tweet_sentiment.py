import sys
import json

def hw(scores, tweets):
  for tweet in tweets:
    print sentiment_of_tweet(tweet['text'], scores)

def sentiment_of_tweet(tweet_text, scores):
  words = tweet_text.split(' ')
  sentiment = 0
  for word in words:
    if scores.has_key(word):
      sentiment += scores[word]
  return sentiment

def lines(fp):
  print str(len(fp.readlines()))

def create_scores_dict(fp):
  scores = {}
  for line in fp:
      term, score = line.split('\t')
      scores[term] = int(score)
  return scores

def get_tweets_array(fp):
  tweets = []
  for line in fp:
    json_line = json.loads(line)
    if not json_line.has_key('delete'):
      tweets.append(json_line)
  return tweets

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_scores_dict(sent_file)
    tweets = get_tweets_array(tweet_file)
    hw(scores, tweets)

if __name__ == '__main__':
    main()
