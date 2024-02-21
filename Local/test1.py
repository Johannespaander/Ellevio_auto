import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

loopback = nb.dcim.devices.get(82)

info = dict(loopback)

print (info["primary_ip4"])