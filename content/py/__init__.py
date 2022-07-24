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

    # TODO @deprecated Basic AuthN should be migrated to OAuth2
    def login(self, username, password):
        url = self.url() + '/documents/api/1.2/folders/self'
        self.auth = {
            'username': username,
            'password': password,
        }
        request = Request(url, self.auth)
        return request.get()
