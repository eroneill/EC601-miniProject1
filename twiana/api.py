import tweepy
import os
import pathlib
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


class TwitterAccess:
    def __init__(
        self, consumer_key, consumer_secret, access_token=None, access_token_secret=None
    ):
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


class GCPAccess:
    def __init__(self, path_of_keys):
        if not os.path.isfile(path_of_keys):
            raise TypeError(
                f"path_of_keys should be a valid path of private keys file."
            )

        path_of_keys = str(pathlib.Path(path_of_keys).resolve())
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path_of_keys

        self._lang_client = language.LanguageServiceClient()

    @property
    def LanguageClient(self):
        return self._lang_client

    def sentiment_analyze(self, content):
        sentiment_html = self.LanguageClient.analyze_sentiment(
            document=types.Document(
                content=content, type=enums.Document.Type.PLAIN_TEXT
            )
        ).document_sentiment

        return sentiment_html
