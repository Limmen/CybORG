import inspect
# allows import of CybORG class as:
from CybORG.main import Main

path = str(inspect.getfile(Main))
path = path[:-7] + '/version.txt'
with open(path) as f:
    CYBORG_VERSION = f.read()[:-1]
