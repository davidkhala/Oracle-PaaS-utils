import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Request:
    def __init__(self, url: str, auth: dict = None):
        self.url = url
        if auth is not None:
            self.auth = HTTPBasicAuth(auth['username'], auth['password'])

    def get(self, params=None, **kwargs):
        if hasattr(self, 'auth'):
            kwargs.setdefault('auth', self.auth)
        try:
            r = requests.get(self.url, params, **kwargs)
        except Exception as e:
            print(e)
        else:
            r.json()

    def post(self, json=None, data=None, **kwargs):
        if hasattr(self, 'auth'):
            kwargs.setdefault('auth', self.auth)
        if data is not None:
            m = MultipartEncoder(data)
            kwargs.setdefault('headers', {'Content-Type': m.content_type})
            data = m
        return requests.post(self.url, data, json, **kwargs).json()

    def delete(self, **kwargs):
        if hasattr(self, 'auth'):
            kwargs.setdefault('auth', self.auth)
        return requests.delete(self.url, **kwargs).json()
