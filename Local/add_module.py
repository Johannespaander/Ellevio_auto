import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

dev_name = input()

# # Define the device details
module_data = {
            "device": nb.dcim.devices.get(name=dev_name).id,
            "module_bay": nb.dcim.module_bays.get(device=dev_name).id,
            "module_type": 1,
            "description": "",
            "tags": [],
            "custom_fields": {},
}

nb.dcim.modules.create(module_data)

