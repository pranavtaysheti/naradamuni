class Naradamuni():
    """
    Naradamuni Class
    ======================
    
    Represents a naradamuni object and provides all functions for end user
    
    Functions
    -------------------------
    
    :auth_twitter: authenticates for use with twitter api (uses tweepy)
    :auth_reddit: authenticates for use with reddit api (uses praw)
    :get_twitter: returns an 'twitter' object.
    :get_reddit: returns an 'reddit' object.

    Variables
    --------------------------
    :reddit_object: praw object is stored after authenticating reddit.
    :twitter_objet: tweepy object is stored after authenticating twitter.
    """

    def __init__(self):
        
        self.reddit_object = None
        self.twitter_object = None

    def auth_twitter(self, *args, **kwargs):
        pass

    def auth_reddit(self, *args, **kwargs):
        pass