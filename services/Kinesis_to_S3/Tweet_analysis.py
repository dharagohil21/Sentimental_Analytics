import boto3
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
import json

class TweetStreamListener(StreamListener):
    # on success
    def on_data(self, data):
        """Overload this method to have some processing on the data before putting it into kiensis data stream
        """
        tweet = json.loads(data)


        try:
            blob = TextBlob(tweet['text'])
            payload = {
                'id': str(tweet['id']),
                'username':tweet['user']['name'],
                'screen_name':tweet['user']['screen_name'],
                'tweet':str(tweet['text'].encode('ascii','ignore')),
                'polarity':blob.sentiment.polarity
            }
            # only put the record when message is not None
            if (payload):
                # print(payload)
                # note that payload is a list

                print(payload)

                #Data getting deliverd to Kinesis
            
                put_response = kinesis_client.put_record(
                    StreamName='twitter-data-kinesis',
                    Data=json.dumps(payload),
                    PartitionKey=str(tweet['user']['screen_name'])
                )

            return True
        except (AttributeError, Exception) as e:
            print(e)


    def on_error(self, status):
        print(status)


if __name__ == '__main__':
   
    # create the kinesis client
    kinesis_client = boto3.client('kinesis')

    #Twitter Cred.
    consumer_Key='hcbuw2JmDJ9rtsgLwUHQk2qSk'
    consumer_Secret= 'pfkCU47DDWTS9pRc0SB6uYlunj4iFpjnBIBIKqwJ8wZwQ26iY0'
    access_Token= '801976087-T98hn67TUAsXnGPQIvzViJpKm77XFQwPqJP90ryY'
    access_Token_Secret= '07ralL6wVzBjmRqxeYeVkTYJGTvMXf9Z5Si4fWA4uGRXt'


    # set twitter keys/tokens
    auth = OAuthHandler(consumer_Key, consumer_Secret)
    auth.set_access_token(access_Token, access_Token_Secret)

    while True:
        try:
            print('Twitter streaming...')

            # create instance of the tweet stream listener
            myStreamlistener = TweetStreamListener()

            # create instance of the tweepy stream
            stream = Stream(auth=auth, listener=myStreamlistener)

            # search twitter for the keyword
            stream.filter(track=["PETA"], languages=['en'], stall_warnings=True)
        except Exception as e:
            print(e)
            print('Disconnected...')
            time.sleep(5)
            continue