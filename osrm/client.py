import functools
import requests

import osrm.exceptions

try:  # Python 3
    from urllib.parse import urlencode
except ImportError:  # Python 2
    from urllib import urllencode

_DEFAULT_BASE_URL = "http://router.project-osrm.org/"
_DEFAULT_API_VERSION = "v1"
_SUPPORTED_VERSION = [_DEFAULT_API_VERSION]
_HTTP_OK = 200


class Client:
    def __init__(self, profile,
                 api_version=_DEFAULT_API_VERSION,
                 base_url=_DEFAULT_BASE_URL,
                 requests_session=None):

        if api_version not in _SUPPORTED_VERSION:
            raise ValueError(f"Unsupported api version:{api_version}, must be any of {','.join(_SUPPORTED_VERSION)}")

        if not base_url.endswith("/"):
            base_url = f"{base_url}/"

        self.profile = profile
        self.base_url = base_url
        self.api_version = api_version
        self.session = requests_session or requests.Session()

    pass

    def _request(self, url, params, **kwargs):
        try:
            response = self.session.get(url, params=params, **kwargs)
        except requests.exceptions.Timeout:
            raise osrm.exceptions.Timeout()
        except Exception as e:
            raise osrm.exceptions.RequestError(e)

        if response.status_code != _HTTP_OK:
            raise osrm.exceptions.HTTPError(response.status_code)
        return response.json()
        pass


from osrm.route import route


def make_api_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


Client.route = make_api_call(route)
