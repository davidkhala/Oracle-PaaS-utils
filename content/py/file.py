from content.py import Base
from content.py.http_request import Request
import os

import json


class File(Base):
    def base_url(self):
        return super().url() + '/documents/api/1.2/files'

    def upload(self, file_path: str, parent_folder_id='self'):
        url = self.base_url() + '/data'
        fs = open(file_path, 'rb')
        form = {
            'jsonInputParameters': json.dumps({'parentID': parent_folder_id}),
            'primaryFile': (os.path.basename(file_path), fs)
        }

        request = Request(url, self.auth)
        r = request.post(None, form)
        fs.close()

        if r['errorCode'] != '0':
            raise Exception(r)
        return r['id']

    def delete(self, file_id: str):
        url = self.base_url() + '/' + file_id
        request = Request(url, self.auth)
        r = request.delete()
        if r['errorCode'] != '0':
            raise Exception(r)
