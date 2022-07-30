import requests

from content.py.http_request import Request


class Base:
    tenancy_name: str
    instance_name: str
    auth: dict

    def __init__(self, tenancy_name: str, instance_name: str):
        self.tenancy_name = tenancy_name
        self.instance_name = instance_name

    def url(self):
        return "https://{}-{}.cec.ocp.oraclecloud.com".format(self.instance_name, self.tenancy_name)

    @staticmethod
    def throw_if_error(r: requests.Response):
        if r.status_code == 401:
            raise Exception(r)
        else:
            _json = r.json()
            if _json['errorCode'] != '0':
                raise Exception(r)

        return _json

    def _get(self, url: str, params=None):
        request = Request(url, self.auth)
        r = request.get(params)
        return Base.throw_if_error(r)

    def _post(self, url: str, json, data=None):
        request = Request(url, self.auth)
        r = request.post(json, data)
        return Base.throw_if_error(r)

    def _delete(self, url: str):
        request = Request(url, self.auth)
        r = request.delete()
        return Base.throw_if_error(r)

    # TODO @deprecated Basic AuthN should be migrated to OAuth2
    def login(self, username, password):
        if password is None:
            raise Exception('missing password')

        if hasattr(self, 'auth'):
            return
        url = self.url() + '/documents/api/1.2/folders/self'
        auth = {
            'username': username,
            'password': password,
        }
        request = Request(url, auth)

        r = request.get()
        if r.status_code == 401 and hasattr(self, 'auth'):
            del self.auth
        else:
            self.auth = auth
