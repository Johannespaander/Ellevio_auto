import pynetbox

# Initialize the NetBox API client
nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

# site = nb.dcim.sites.get()

# print(site)

# Retrieve all sites
sites = nb.dcim.sites.all()

# Print the list of sites
# for site in sites:
#     print(f"Site Name: {site.name}, Site ID: {site.id}")
    
prefix2 = nb.ipam.prefixes.filter(q="10.14", status="reserved")

# print(list(prefix2)[0])

test = list(prefix2)[0]

print(test.id)

# print(test)

# print(nb.ipam.prefixes.update([{"id": test.id, "status": "active"}]))

