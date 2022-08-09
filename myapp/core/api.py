import requests

URL = "https://graph.facebook.com/v13.0/"


def get_accounts_info(_token):
    params = {
        'access_token': _token,
        'fields': 'name, instagram_business_account, about, category'
    }
    url = URL + '/me/accounts'
    r = requests.get(url, params)
    return r.json()


def get_insta_content_and_comments(ig_id, _token):
    params = {
        'access_token': _token,
        'fields': 'comments{replies, text}, media_url'
    }
    url = URL + '{}/media'.format(ig_id)
    r = requests.get(url, params)
    ####
    m = requests.get(f"https://graph.facebook.com/v13.0/{ig_id}/conversations?platform=instagram&access_token={_token}")
    print(m.json())
    return r.json()


def make_access_redirect_link(user_id):
    url = 'https://www.facebook.com/v13.0/dialog/oauth?'
    params = {
        'client_id': '404560484397002',
        'redirect_uri': 'https://gromauto.com.ua/local/redirect/',
        'state': '{user={}}'.replace('{}', str(user_id)),
        'scope': 'instagram_basic,public_profile,pages_manage_metadata,instagram_manage_insights,instagram_content_publish,instagram_manage_messages',

    }
    for key, val in params.items():
        url += f'{key}={val}&'

    return url


def get_access_code(code):
    url = 'https://graph.facebook.com/v13.0/oauth/access_token?'
    params = {
        'client_id': '404560484397002',
        'redirect_uri': 'https://gromauto.com.ua/local/redirect/',
        'client_secret': 'e0e4e19359e18684aa0a5cfe25b735e8',
        'code': code,
    }
    r = requests.get(url, params)
    print(r.json())
    return r.json()

