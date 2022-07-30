import unittest
import os
from content.py.folder import Folder
from content.py.file import File
from content.py.metadata import Metadata


class FolderTest(unittest.TestCase):
    def test_folder(self):
        folder = Folder('hktwlab', 'cx')

        folder.login('david.yx.liu@oracle.com', os.getenv('password'))
        create_recipe = folder.create('new-folder1')
        print(create_recipe)
        new_created = create_recipe['id']
        folder.delete(new_created)
        result = folder.list('self')
        print(result)

    def test_file(self):
        file = File('hktwlab', 'cx')
        file.login('david.yx.liu@oracle.com', os.getenv('password'))
        path = 'dummy.txt'
        _id = file.upload(path)
        tags = ['file', 'metadata']
        file.tag(_id, tags)
        result = file.tag_list(_id)
        print(result)
        file.delete(_id)

    def test_meta(self):
        meta = Metadata('hktwlab', 'cx')
        meta.login('david.yx.liu@oracle.com', os.getenv('password'))
        name = 'testCollection'
        meta.create(name)
        meta.delete(name)


if __name__ == '__main__':
    unittest.main()
