import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

#parent = "10.11.192.0/18"
prefix = nb.ipam.prefixes.get(prefix="10.11.192.0/18")

print(prefix.available_ips.list())
# for ip_address in prefix:
#     print(ip_address)