import pytest
import jsonpickle
from configparser import ConfigParser
from pathlib import Path
from twiana.api import TwitterAccess
from twiana.api import GCPAccess


@pytest.fixture(scope="module")
def twitter_access():
    test_conf = ConfigParser()
    test_conf.read(Path("./test.conf"))
    t_path = test_conf["PATH"]["twitter_keys_path"]

    if t_path.startswith("~/"):
        twitter_keys_path = Path(Path.home(), t_path[2:])
    else:
        twitter_keys_path = Path(t_path)

    twitter_keys_conf = ConfigParser()
    twitter_keys_conf.read(twitter_keys_path)

    access = TwitterAccess(
        consumer_key=twitter_keys_conf["CONSUMER"]["key"],
        consumer_secret=twitter_keys_conf["CONSUMER"]["secret"],
        access_token=twitter_keys_conf["ACCESS"]["key"],
        access_token_secret=twitter_keys_conf["ACCESS"]["secret"],
    )

    return access


@pytest.fixture(scope="module")
def gcp_access():
    test_conf = ConfigParser()
    test_conf.read(Path("./test.conf"))
    g_path = test_conf["PATH"]["gcp_keys_path"]

    if g_path.startswith("~/"):
        keys_path = Path(Path.home(), g_path[2:])
    else:
        keys_path = Path(g_path)

    gcp = GCPAccess(keys_path)

    return gcp


def test_twitter_api(twitter_access):
    tweets = twitter_access.API.home_timeline()

    # print(jsonpickle.encode(tweets))

    with open("./home_timeline_sample", "w") as f:
        for t in tweets:
            f.write(jsonpickle.encode(t) + "\n")


def test_gcp_sentiment(gcp_access):
    _test_str = "The quick brown fox jumps over the lazy dog."

    with open("./gcp_sentiment_sample", "w") as f:
        f.write(f"TEXT: {_test_str}")
        sentiment = gcp_access.sentiment_analyze(_test_str)
        f.write(
            f"Sentiment:\nSCORE: {sentiment.score}\nMAGNiTUDE: {sentiment.magnitude}"
        )
