import pynetbox

nb = pynetbox.api(
    'http://localhost:8000',
    token='5fc88bccf4a50a4c1de248a45bd96595dd883186'
)

site_name = input()

site_data = {
    "name": site_name,
    "slug": site_name,
}

# Create site
nb.dcim.sites.create(site_data)