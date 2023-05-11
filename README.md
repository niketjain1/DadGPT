# DadGPT

DadGPT is a twitter bot that posts dad jokes on your twitter account. It is capable of posting jokes on a variety of subjects and ensures that duplicate jokes are not posted.
This project uses OpenAI ChatGPT APIs to generate dad jokes and tweepy python package to post them on Twitter.
To get this running, ensure that the following environment variables are set:

```
OPENAI_API_KEY  
TWITTER_API_KEY   
TWITTER_API_SECRET  
TWITTER_BEARER_TOKEN  
TWITTER_ACCESS_TOKEN  
TWITTER_ACCESS_TOKEN_SECRET  
```

Alternatively, you can also set these environment variables from the python script like so `os.environ['OPENAI_API_KEY']='YOUR_API_KEY'`
