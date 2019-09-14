import tweepy


class TwitterAccess():

    def __init__(self, consumer_key, consumer_secret, access_token=None, access_token_secret=None):
        auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
        if (access_token is None) and (access_token_secret is None):
            self._request_access_token(auth_handler)
        else:
            auth_handler.set_access_token(access_token, access_token_secret)

        self._API = tweepy.API(auth_handler)

    @property
    def API(self):
        return self._API

    def _request_access_token(self, oatuh_handler):
        raise NotImplementedError()
