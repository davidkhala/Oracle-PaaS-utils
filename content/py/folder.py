from content.py import Base


class Folder(Base):

    def base_url(self):
        return super().url() + '/documents/api/1.2/folders/'

    def get(self, folder_id: str):
        url = self.base_url() + folder_id
        return self._get(url)

    def list(self, folder_id='self'):
        url = self.base_url() + folder_id + '/items'
        return self._get(url)['items']

    def create(self, name: str, description='', parent_folder_id='self'):
        data = {
            'name': name,
            'description': description
        }
        url = self.base_url() + parent_folder_id

        result = self._post(url, data)

        if result['errorCode'] != '0':
            raise Exception(result)
        return {
            'name': result['name'],
            'id': result['id']
        }

    def delete(self, folder_id: str):
        url = self.base_url() + folder_id
        result = self._delete(url)
        if result['errorCode'] != '0':
            raise Exception(result)
