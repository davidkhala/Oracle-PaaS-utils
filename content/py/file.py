from content.py import Base
import os

import json


class File(Base):
    def base_url(self):
        return super().url() + '/documents/api/1.2/files/'

    def upload(self, file_path: str, parent_folder_id='self'):
        url = self.base_url() + 'data'
        fs = open(file_path, 'rb')
        form = {
            'jsonInputParameters': json.dumps({'parentID': parent_folder_id}),
            'primaryFile': (os.path.basename(file_path), fs)
        }

        try:
            r = super().post(url, None, form)
        finally:
            fs.close()
        return r['id']

    def delete(self, file_id: str):
        url = self.base_url() + file_id
        return super().delete(url)

    def tag(self, file_id: str, tags: [str]):
        url = self.base_url() + file_id + '/tags'
        data = {
            'setTags': ','.join(tags)
        }
        return super().post(url, data)

    def tag_list(self, file_id: str):
        url = self.base_url() + file_id + '/tags'
        r = super().get(url)
        return r['tags'].split(',')
