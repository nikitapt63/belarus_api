import requests

from consts import REQUEST_URL


def get_api_news_data():
    try:
        response = requests.get(REQUEST_URL)
        if not str(response.status_code).startswith('2'):
            raise ValueError
    except ValueError:
        return "Not valid response status_code != 2XX"
    data = response.json()[:20]
    return data
