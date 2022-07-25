import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Request:
    def __init__(self, url: str, auth: dict = None):
        self.url = url
        if auth is not None:
            self.auth = HTTPBasicAuth(auth['username'], auth['password'])

    def get(self, params=None, **kwargs):
        kwargs.setdefault('auth', getattr(self, 'auth', None))
        return requests.get(self.url, params, **kwargs).json()

    def post(self, json=None, data=None, **kwargs):
        kwargs.setdefault('auth', getattr(self, 'auth', None))
        if data is not None:
            m = MultipartEncoder(data)
            kwargs.setdefault('headers', {'Content-Type': m.content_type})
            data = m
        return requests.post(self.url, data, json, **kwargs).json()

    def delete(self, **kwargs):
        kwargs.setdefault('auth', getattr(self, 'auth', None))
        return requests.delete(self.url, **kwargs).json()
