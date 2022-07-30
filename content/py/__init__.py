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
    def throw_if_error(r: dict):
        if r['errorCode'] != '0':
            raise Exception(r)

    def get(self, url: str, params=None):
        request = Request(url, self.auth)
        r = request.get(params)
        Base.throw_if_error(r)
        return r

    def post(self, url: str, json, data=None):
        request = Request(url, self.auth)
        r = request.post(json, data)
        Base.throw_if_error(r)
        return r

    def delete(self, url: str):
        request = Request(url, self.auth)
        r = request.delete()
        Base.throw_if_error(r)
        return r

    # TODO @deprecated Basic AuthN should be migrated to OAuth2
    def login(self, username, password):
        if password is None:
            raise Exception('missing password')
        url = self.url() + '/documents/api/1.2/folders/self'
        self.auth = {
            'username': username,
            'password': password,
        }
        request = Request(url, self.auth)
        return request.get()
