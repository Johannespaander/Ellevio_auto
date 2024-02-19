import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

i = 0

for x in range (1, 8):
    while i <= 255:
        nb.ipam.prefixes.create(prefix="10.14." + str(x + 16) + "." + str(i) + "/28")
        i = i + 16
    i = 0