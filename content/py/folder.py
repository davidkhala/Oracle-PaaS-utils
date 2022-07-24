from content.py import Base
from content.py.http_request import Request


class Folder(Base):

    def base_url(self):
        return super().url() + '/documents/api/1.2/folders/'

    def get(self, folder_id: str):
        url = self.base_url() + folder_id

        request = Request(url, self.auth)
        return request.get()

    def list(self, folder_id='self'):
        url = self.base_url() + folder_id + '/items'
        request = Request(url, self.auth)
        return request.get()['items']

    def create(self, name: str, description='', parent_id='self'):
        options = {
            'name': name,
            'description': description
        }
        url = self.base_url() + parent_id

        request = Request(url, self.auth)
        result = request.post(options)

        if result['errorCode'] != '0':
            raise Exception(result)
        return {
            'name': result['name'],
            'id': result['id']
        }

    def delete(self, folder_id: str):
        # /documents/api/1.2/folders/{folderId}
        url = self.base_url() + folder_id
        request = Request(url, self.auth)
        result = request.delete()
        if result['errorCode'] != '0':
            raise Exception(result)
