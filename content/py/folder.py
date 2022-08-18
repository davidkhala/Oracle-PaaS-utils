from content.py import Base
from content.py.metadata import Metadata


class Folder(Base):

    def base_url(self):
        return super().url() + '/documents/api/1.2/folders/'

    def define_metadata(self, folder_id: str, collection_name: str, values: dict, is_private=False):
        url = self.base_url() + folder_id + '/metadata/' + Metadata.name(collection_name, is_private)
        r1 = self._post(url, {})
        if values:
            return self.assign_metadata(folder_id, collection_name, values, is_private)
        return r1

    def assign_metadata(self, folder_id: str, collection_name: str, values: dict, is_private=False):
        url = self.base_url() + folder_id + '/metadata'

        _prefix = Metadata.name(collection_name, is_private) + '.'
        data = {}
        for key, value in values.items():
            data[_prefix + key] = Metadata.serialize_value(value)
        return self._post(url, data)

    def get_metadata(self, folder_id: str):
        url = self.base_url() + folder_id + '/metadata'
        r = self._get(url)
        return r['metadata']

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

        _id = result['id']
        file_url = super().url() + '/documents/folder/' + _id + "/_" + name

        return {
            'name': result['name'],
            'id': _id,
            'url': file_url
        }

    def delete(self, folder_id: str):
        url = self.base_url() + folder_id
        result = self._delete(url)
        if result['errorCode'] != '0':
            raise Exception(result)
