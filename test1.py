import pynetbox

nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

x = nb.dcim.module_bays.get(device="TESTDEVICE1")
from pprint import pprint

pprint(x.serialize())