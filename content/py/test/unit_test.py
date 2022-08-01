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

    def test_folder_delete(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        folder_id = 'FED63BC68B0829EDA2BFE9137B180A3EF35DA9FF09F7'
        self.folder.delete(folder_id)

    def test_file_upload(self):
        self.file.login('david.yx.liu@oracle.com', os.getenv('password'))
        path = 'dummy.txt'
        _id = self.file.upload(path)
        tags = ['file', 'metadata']
        self.file.tag(_id, tags)
        print(_id)

    def test_file_delete(self):
        self.file.login('david.yx.liu@oracle.com', os.getenv('password'))
        _id = 'D13EE6B35047D33B7343AE232D9F80F75672606D174E'
        self.file.delete(_id)

    def test_meta_create(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.create(self.collection_name)

    def test_meta_delete(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.delete(self.collection_name)


if __name__ == '__main__':
    unittest.main()
