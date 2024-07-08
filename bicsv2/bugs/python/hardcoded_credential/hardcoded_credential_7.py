import tweepy

def authenticate_twitter_app():
    api_key = "sk-1234567890abcdef1234567890abcdef"
    api_secret = "sk-1234567890abcdef1234567890abcdef"
    access_token = "sk-1234567890abcdef1234567890abcdef"
    access_secret = "sk-1234567890abcdef1234567890abcdef"

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    
    return api
