import datetime
from pprint import pprint

import requests
import time
#https://www.facebook.com/v13.0/dialog/oauth?client_id=404560484397002&redirect_uri=https://gromauto.com.ua&state=st=state123abc,ds=123456789&scope=public_profile

class Token:
    def __init__(self):
        self._token = ''
        self._expires_at = 0

    def check_token(self, _token=None):
        if _token is None:
            _token = self._token

        debug_result = self._debug_token(_token=_token)
        if 'error' in debug_result:
            return
        else:
            expires_at = debug_result['data']['expires_at']
            return expires_at

    @staticmethod
    def _debug_token(_token=None):

        url = f'https://graph.facebook.com/debug_token?input_token={_token}&access_token={_token}'
        response = requests.get(url)

        return response.json()

    @property
    def expired(self):
        return self._expires_at

    @property
    def token(self):
        if self.expired < time.time() - 60:
            self._token = ''
        return self._token



def get_ig_id(token, page_n=0):
    url = "https://graph.facebook.com/v13.0/me/accounts?access_token={}".format(token)
    r = requests.get(url)
    page_id = r.json()['data'][page_n]['id']

    url = "https://graph.facebook.com/v13.0/{}?fields=instagram_business_account&access_token={}".format(page_id, token)
    r = requests.get(url)
    return r.json()['instagram_business_account']['id']


def get_insta_media(ig_id, token):
    url = "https://graph.facebook.com/v13.0/{}/media?access_token={}".format(ig_id, token)
    r = requests.get(url)
    pprint(r.json())


if __name__ == '__main__':
    token = Token()
    ig_id = get_ig_id(token.token)
    get_insta_media(ig_id, token.token)
