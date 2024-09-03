import tweepy
import openai
import openai
import random

# Twitter API credentials
consumer_key = 'nb3alljifdsafKqlXanIBUw5wDrwr05'
consumer_secret = 'qOKUHBIDFUE8H4IUoATENnZhjgyabyz9PVwIDT9AuDXXHMSwwMTbPdJdjci'
access_token = '1646544692622897153-6lrxqpT3OzfkJXE41xnNLQKqSM7WNG'
access_token_secret = 'iT0ekNl2987adfJakQepIeCleBBKW7WqBgdm6ZwskCnQLVBV47txKh'


openai.organization = "org-5C6asdfads&**(089uf4AEk80qDqB1nDKJLMLKR8NMvNhu"
openai.api_key = 'sk-k445qds9PoImHSsdpjiznQT3BlbkFJ9fpJK9840dxUHOqqgcift7jZkD6ND'
openai.Model.list()


# OpenAI API credentials
model_engine = "text-davinci-002"

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Cache for storing generated text
cache = {}

# Function to generate random text with GPT-3
def generate_text(prompt):
    if prompt in cache:
        return cache[prompt]
    
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    text = response.choices[0].text.strip()
    cache[prompt] = text
    
    return text

# Function to tweet a message
def tweet(message):
    try:
        api.update_status(message)
        print("Tweeted: " + message)
    except tweepy.TweepError as e:
        print(e)

# Function to schedule a tweet every day at a specific time
def schedule_tweet():
    my_list = ['about the nature', 'about animals', 'about the king cobra', 'about the brown bear', 'about hunting', 'about bow hunting being the best sport']
    prompt = 'generate a tweetable statement ' + random.choice(my_list)
    tweet(generate_text(prompt))
    #schedule.every().day.at("12:00").do(tweet, message)

# Schedule the tweets
schedule_tweet()
