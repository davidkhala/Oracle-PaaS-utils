import os
from content.py.folder import Folder

folder = Folder('hktwlab', 'cx')

folder.login('david.yx.liu@oracle.com', os.getenv('password'))
createRecipe = folder.create('new-folder1')
print(createRecipe)
newCreated = createRecipe['id']
folder.delete(newCreated)
result = folder.list('self')
print(result)
