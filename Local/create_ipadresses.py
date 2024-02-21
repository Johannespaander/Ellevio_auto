import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)


address = nb.ipam.ip_addresses.create(address="10.110.0.0/28")

print(dict(address))