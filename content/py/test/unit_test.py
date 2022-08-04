import datetime
import unittest
import os

from content.py.folder import Folder
from content.py.file import File
from content.py.metadata import Metadata
from content.py.share import Share


class FolderTest(unittest.TestCase):
    folder = Folder('hktwlab', 'cx')
    file = File('hktwlab', 'cx')
    meta = Metadata('hktwlab', 'cx')
    share = Share('hktwlab', 'cx')
    collection_name = 'testCollection'
    folder_name = 'text'

    def test_meta_create(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.create(self.collection_name, {
            "personalId": "",
            'address': "",
            "birthday": datetime.datetime.now(),
            "income": 0,
        })

    def test_folder_create(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        create_recipe = self.folder.create(self.folder_name)
        folder_id = create_recipe['id']
        print(folder_id)
        metadata = {
            "personalId": "M123456",
            'address': "HongKong",
            "birthday": datetime.datetime.now(),
            "income": 10000,
        }
        self.folder.define_metadata(folder_id, self.collection_name, metadata)

        self.share.login('david.yx.liu@oracle.com', os.getenv('password'))
        link = self.share.folder(folder_id)
        print(link)

    def test_folder_metadata(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        folder_id = 'FDA759AA8B3E04F584186E0AB6D947009D7EABC47F2A'
        metadata = {
            "personalId": "M123456",
            'address': "HongKong",
            "birthday": datetime.datetime.now(),
            "income": 10000,
        }
        self.folder.assign_metadata(folder_id, self.collection_name, metadata)
        actual = self.folder.get_metadata(folder_id)
        print(actual)

    def test_file_upload(self):
        self.file.login('david.yx.liu@oracle.com', os.getenv('password'))
        path = 'dummy.txt'
        folder_id = 'self'  # or 'self'
        _id = self.file.upload(path, folder_id)
        tags = ['file', 'metadata']
        self.file.tag(_id, tags)
        print(_id)
        self.share.login('david.yx.liu@oracle.com', os.getenv('password'))
        link = self.share.file(_id)
        print(link)

    def test_folder_get(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        folder_id = 'F855DF8440A16C9F8E11734C1E09CB56542DD11642BD'
        r = self.folder.get(folder_id)
        print(r)
        r = self.folder.get_metadata(folder_id)
        print(r)

    def test_folder_delete(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        folder_id = 'F82F1622088E1344EBAAE1D089729FCCA6DE185AC233'
        self.folder.delete(folder_id)

    def test_file_delete(self):
        self.file.login('david.yx.liu@oracle.com', os.getenv('password'))
        _id = 'D9AD538FBD36F4393A10C31E49BAC01F45319FD8D0EA'
        self.file.delete(_id)

    def test_meta_list(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        r = self.meta.list()
        print(r)

    def test_meta_delete(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.delete(self.collection_name)


if __name__ == '__main__':
    unittest.main()
