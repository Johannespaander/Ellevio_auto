import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

dev_name = input()

device_data = {
    "name": dev_name,
    "device_type": 1,  # ID of the device type (you need to replace it with the actual device type ID)
    "role": 1,  # ID of the device role (you need to replace it with the actual device role ID)
    "site": 1,         # ID of the site (you need to replace it with the actual site ID)
    "status": "active"
}

nb.dcim.devices.create(device_data)

