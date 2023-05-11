#!/usr/bin/env python
# coding: utf-8

import tweepy
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os
import requests
import random
import datetime
import random
import time
from datetime import datetime


api_key = os.environ.get("TWITTER_API_KEY")
api_secret = os.environ.get("TWITTER_API_SECRET")
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")


chat = ChatOpenAI(temperature = 0.8)
words = ["ear", "writer", "nose", "hand", "eyes", "skin", "pizza", "shoes", "laptop", "phone", "space", "population", "actor", "stars", "earth", "day", "door", "window", "life", "soul", "animal", "zoo", "manager", "tale", "soap", "miracle", "house", "roof", "tradition", "car", "school", "emphasis", "boy", "map", "smoke", "lock", "temperature", "key", "farmer", "foot", "horse", "lion", "information", "courage", "mouse", "speech", "jungle", "doctor", "depression", "engineer", "effort", "businessman", "wool", "book", "list", "servant", "mixture", "egg", "chicken", "library", "nation", "boat", "health", "extent", "bike", "reception", "menu", "tea", "leaf", "pet", "mat", "solution", "trainer", "opportunity", "tomato", "pen", "mode", "crow", "bonus", "cow", "moment", "birthday", "bee", "sympathy", "selection", "teacher", "grape", "wax", "measurement", "cent", "accident", "button", "situation", "management", "chocolate", "card", "system", "cart", "stick", "beach", "mountain", "bean", "fingers", "juice", "hat", "tongue", "diamond", "gun", "hot", "chair", "clock", "pie", "time", "message", "preference", "variety", "poet", "fly", "connection", "tiger", "entertainment", "imagination", "significance", "marriage", "rat", "elephant", "cat", "dog", "team", "table", "top", "picture", "department", "communication", "coffee", "up", "personality", "charity", "down", "left", "tight", "right", "lawyer", "poetry", "region", "roll", "distribution", "beer", "cute", "mask", "pot", "comparison", "shop", "soup", "length", "dear", "debt", "oval", "tree", "baseball", "grass", "football", "collection", "plant", "woman", "neck", "socks", "salad", "blanket", "category", "truck", "hat", "face", "blood", "member", "spider", "committee", "funeral", "advice", "hat", "housing", "cabinet", "beak", "supermarket", "bus", "candy", "pig", "beat", "lizard", "square", "homework", "math", "bug", "volume", "jail", "employer", "bench", "basket", "oven", "airport", "rainbow", "monkey", "impression", "statement", "quality", "desk", "ant", "tail", "pencil", "refrigerator", "sister", "resolution", "hall", "two", "membership", "banana", "gene", "snow", "efficiency", "restaurant", "bridge", "owl", "circle", "finding", "depth", "operation", "color", "bat", "cloud", "literature", "robot", "profession", "dad", "county", "poem", "analyst", "interaction", "curl", "snake", "fog", "frog", "river", "property", "arrow", "bow", "criticism", "year", "law", "judgment", "ballon", "power", "product", "cookie", "signature", "lemon", "food", "crab", "unit", "coat", "orange", "hat", "hotel", "heart", "buyer", "possession", "recording", "resource", "fact", "fire", "box", "meat", "director", "paper", "rain", "water", "float", "story", "cruise", "ship", "midnight", "pie", "news", "dream", "device", "scene", "freedom", "bunny", "rocket", "snail", "sun", "son", "disk", "cell", "daughter", "television", "wife", "version", "love", "meaning", "turtle", "country", "thanks", "reading", "sea", "song", "enthusiasm", "way", "payment", "audience", "virus", "employee", "data", "milk", "corn", "intention", "dragon", "historian", "piano", "entry", "inflation", "movie", "protection", "assumption", "uncle", "camera", "hippo", "tennis", "opinion", "thought", "bird", "tea", "night", "perspective", "man", "memory", "ear", "student", "dirt", "election", "honey", "rock", "method", "construction", "child", "energy", "pollution", "decision", "disaster", "clothes", "percentage",  "internet", "loss", "anxiety", "mud", "instruction", "pillow", "improvement", "reality", "cycle", "replacement", "problem", "candle", "line", "classroom", "reaction", "event", "ladder", "mood", "series", "administration", "comb", "light", "bathroom", "customer", "driver", "hair", "warning", "grandmother", "science", "carrot", "computer", "safety", "cousin", "championship", "way", "youth", "responsibility", "purse", "alcohol", "road", "inspection", "transportation", "database", "hat", "kite", "session", "ratio", "reflection", "throat", "girl",
         "importance", "presentation", "childhood", "contribution", "tooth", "lamp", "height", "variation", "insect", "contract", "vehicle", "gate", "president", "editor", "advertising", "competition", "atmosphere", "discussion", "policy", "shopping", "application", "attitude", "singer", "income", "knowledge", "suit", "error", "case", "sunglasses", "passenger", "combination", "storage", "definition", "recommendation", "potato", "theory", "apple", "development", "proposal", "economics", "industry", "burger", "whale", "ambition", "permission", "assistant", "meal", "growth", "girlfriend", "wedding",
         "recognition", "cigarette", "marketing", "apartment", "emotion", "shirt", "aspect", "context", "town", "strategy", "attention", "addition", "music", "conclusion", "passion", "delivery", "suggestion", "consequence", "client", "reputation", "studio", "sector", "relationship", "inspector", "guidance", "fishing", "drawing", "newspaper", "society", "teaching", "perception", "media", "priority", "drawer", "university", "cancer", "security", "foundation", "article", "control", "ability", "player", "garbage", "ear", "expression", "boyfriend", "location", "departure", "breath", "basis"
"Cars", "Effect", "Baby", "Curtain", "Smile", "Cube", "Triangle", "Excitement", "Swing", "Person", "Cherry", "Biscuit", "Friction", "Ground", "Basin", "Penalty", "Mango", "Bowl", "Holiday", "Mall", "Amount", "Horn", "Basketball", "Pan", "Ghost", "Office", "Creature", "Price", "Sort", "Need", "Twist", "User", "Balls", "Understanding", "Fight", "Drum", "Spot", "Toys", "Climate", "Bikes", "Wash", "Disgust", "Breakfast", "Fish", "Goat", "Tank", "Airplane", "Jar", "Boys", "Head", "Tension", "Cactus", "Top", "Note", "Flower", "Sugar", "Sock", "Cellar", "Crayon", "Magic", "Flag", "Octopus", "Friendship", "Appliance", "Establishment", "Bottle", "Loaf", "Bed", "Cattle", "Wrist", "King", "Question", "Chalk", "Steak", "Broom", "Bells", "Chimney", "Daimon", "Volleyball", "Temper", "Brush", "college", "Sky", "island", "Aunt", "family", "Grade", "Mom", "Word", "Sign", "Lift", "Response", "Association", "Letter", "bone", "Chairs", "moon", "Game", "Stage", "Rainstorm", "Stew", "ball", "Reason", "Village", "bread", "Swim", "angel", "ocean", "Difficulty", "cup", "Badge", "Kitten", "Cabbage", "Crown", "Quilt", "Hole", "Lady", "Number", "Clover", "Brothers" 
        ]

# Get the current day of the year
# today = datetime.datetime.today()
# day_of_year = today.timetuple().tm_yday
# print(today)
# print(day_of_year)

# Select a random object keyword based on the day of the year

random.seed(datetime.now().timestamp())
selected_keyword = words[random.randint(0, len(words) - 1)]
print(selected_keyword)

input_word = selected_keyword

prompt = PromptTemplate(
    input_variables = ["object"],
    template = "Tell me a dad joke about {object} or related to {object}."
)

print(prompt.format(object = input_word))

chain = LLMChain(llm = chat, prompt = prompt)

generated_joke = chain.run(input_word)
generated_joke

tags = "\n#dadjokes #funnyAIbot"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret) 
api = tweepy.API(auth)


# Check if the tweeted_dad_jokes.txt file exists
if os.path.exists('tweeted_dad_jokes.txt'):
    # Load already tweeted dad jokes from a file
    with open('tweeted_dad_jokes.txt', 'r') as f:
        tweeted_dad_jokes = f.read().splitlines()
else:
    tweeted_dad_jokes = []

joke = generated_joke

if joke not in tweeted_dad_jokes:
    # post a tweet
    tweet_content = joke + tags
    print(tweet_content)
    response = client.create_tweet(text = tweet_content)
#     print(response)
    if not response.errors:
        # tweet was tweeted successfully
        with open('tweeted_dad_jokes.txt', 'a') as f:
            f.write('\n' + joke)
else:
    print("entering else branch")
    word1 = random.choice(words)
    print(prompt.format(object = word1))
    chain = LLMChain(llm = chat, prompt = prompt)
    generated_joke1 = chain.run(word1) 
    tweet_content1 = generated_joke1 + tags
    print(tweet_content1)
    response = client.create_tweet(text = tweet_content1)
    if not response.errors:
        # tweet was tweeted successfully
        with open('tweeted_dad_jokes.txt', 'a') as f:
            f.write('\n' + generated_joke1)
