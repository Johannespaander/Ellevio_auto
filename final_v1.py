import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)
dev_name = input()

# # Define the device details
device_data = {
    "name": dev_name,
    "device_type": 1,  # ID of the device type (you need to replace it with the actual device type ID)
    "role": 1,  # ID of the device role (you need to replace it with the actual device role ID)
    "site": 1,         # ID of the site (you need to replace it with the actual site ID)
    "status": "active"
}

# Create device
nb_device = nb.dcim.devices.create(device_data)

# # Define the module details.
module_data = {
            "device": nb.dcim.devices.get(name=dev_name).id,
            "module_bay": nb.dcim.module_bays.get(device=dev_name).id,
            "module_type": 1,
            "description": "",
            "tags": [],
            "custom_fields": {},
}
# Create module for device.
nb.dcim.modules.create(module_data)

# Add Loopback adress to module
prefix = nb.ipam.prefixes.get(prefix="10.11.192.0/18")

interf = nb.dcim.interfaces.get(name="loopback",device=dev_name).id

ipadd = prefix.available_ips.create()

ipadd.update({"assigned_object_id":interf,"assigned_object_type":"dcim.interface"})

primary = nb.dcim.devices.update([{"id":nb_device.id,"primary_ip4":ipadd.id}])

# Add Vlan adress to module
#prefix2 = nb.ipam.prefixes.get(prefix="10.12.192.0/18")
prefix2 = list(nb.ipam.prefixes.filter(q="10.14", status="reserved"))[0]

int2 = nb.dcim.interfaces.get(name="vlan1",device=dev_name).id

ipadd2 = prefix2.available_ips.create()

ipadd2.update({"assigned_object_id":int2,"assigned_object_type":"dcim.interface"})

nb.ipam.prefixes.update([{"id":prefix2.id,"status":"active", "site":1}])

