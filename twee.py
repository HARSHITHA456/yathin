import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "1nRclHdluZLpdyVsqviy9jvVJ",
    "consumer_secret"     : "y2IzB0luQahPnDUgPzFtByyY0kRzGC8fWpeo8bVihmksUCPwX2",
    "access_token"        : "968402862513491968-f1FLb7lFJimtFNQoODPDGtwTWtm10Is",
    "access_token_secret" : "Aqp1Sf4mAUlsvvyVSl7ssX11uFx9w6C9hL7mYu7mJQiRW" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
