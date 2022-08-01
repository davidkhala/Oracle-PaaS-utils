import unittest
import os

from content.py.folder import Folder
from content.py.file import File
from content.py.metadata import Metadata


class FolderTest(unittest.TestCase):
    folder = Folder('hktwlab', 'cx')
    file = File('hktwlab', 'cx')
    meta = Metadata('hktwlab', 'cx')
    collection_name = 'testCollection'
    folder_name = 'new-folder1'

    def test_folder_create(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        create_recipe = self.folder.create(self.folder_name)
        folder_id = create_recipe['id']
        print(folder_id)

    def test_file_upload(self):
        self.file.login('david.yx.liu@oracle.com', os.getenv('password'))
        path = 'dummy.txt'
        folder_id = 'F7D9F0B4E6B67303FD06F8718B82328BE2A0E68DE548'  # or 'self'
        _id = self.file.upload(path, folder_id)
        tags = ['file', 'metadata']
        self.file.tag(_id, tags)
        print(_id)

    def test_folder_delete(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        folder_id = 'F7D9F0B4E6B67303FD06F8718B82328BE2A0E68DE548'
        self.folder.delete(folder_id)

    def test_file_delete(self):
        self.file.login('david.yx.liu@oracle.com', os.getenv('password'))
        _id = 'D9AD538FBD36F4393A10C31E49BAC01F45319FD8D0EA'
        self.file.delete(_id)

    def test_meta_create(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.create(self.collection_name, {
            'enable': True
        })

    def test_meta_list(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        r = self.meta.list()
        print(r)

    def test_meta_delete(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.delete(self.collection_name)


if __name__ == '__main__':
    unittest.main()
