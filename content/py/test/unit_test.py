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

    def test_folder(self):
        self.folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        create_recipe = self.folder.create('new-folder1')
        print(create_recipe)
        new_created = create_recipe['id']
        self.folder.delete(new_created)
        result = self.folder.list('self')
        print(result)

    def test_file(self):
        self.file.login('david.yx.liu@oracle.com', os.getenv('password'))
        path = 'dummy.txt'
        _id = self.file.upload(path)
        tags = ['file', 'metadata']
        self.file.tag(_id, tags)
        result = self.file.tag_list(_id)
        print(result)
        self.file.delete(_id)

    def test_meta_create(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.create(self.collection_name)

    def test_meta_delete(self):
        self.meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        self.meta.delete(self.collection_name)


if __name__ == '__main__':
    unittest.main()
