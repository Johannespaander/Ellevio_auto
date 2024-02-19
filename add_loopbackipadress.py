import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)


prefix = nb.ipam.prefixes.get(prefix="10.11.192.0/18")

int = nb.dcim.interfaces.get(name="loopback",device="TESTDEVICE2").id

ipadd = prefix.available_ips.create()

ipadd.update({"assigned_object_id":int,"assigned_object_type":"dcim.interface"})