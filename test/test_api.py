import pytest
import jsonpickle
from configparser import ConfigParser
from pathlib import Path
from twiana.api import TwitterAccess

@pytest.fixture(scope='module', autouse=True)
def twitter_access():
    test_conf = ConfigParser()    
    test_conf.read(Path('./test.conf'))
    t_path = test_conf['PATH']['twitter_keys_path']
    
    if t_path.startswith('~/'):
        twitter_keys_path = Path(Path.home(), t_path[2:])
    else:
        twitter_keys_path = Path(t_path)

    twitter_keys_conf = ConfigParser()
    twitter_keys_conf.read(twitter_keys_path)
    
    access = TwitterAccess(
        consumer_key=twitter_keys_conf['CONSUMER']['key'],
        consumer_secret=twitter_keys_conf['CONSUMER']['secret'],
        access_token=twitter_keys_conf['ACCESS']['key'],
        access_token_secret=twitter_keys_conf['ACCESS']['secret']
    )
    
    return access


def test_api(twitter_access):
    tweets = twitter_access.API.home_timeline()

    print(jsonpickle.encode(tweets))

    # with open('./home_timeline_sample', 'w') as f:
    #     for t in tweets:
    #         f.write(jsonpickle.encode(t) + '\n')    