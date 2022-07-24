import os
from content.py import Base

base = Base('hktwlab', 'cx')

base.login('david.yx.liu@oracle.com', os.getenv('password'))
