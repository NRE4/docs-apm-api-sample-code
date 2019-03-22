#
# Print organization info
#
from api_fns import *

r = get_org()
if r.status_code == requests.codes.ok:
    for organization in r.json():
        print('Org ({}) name --> {} -- parent({})'.format(organization['id'],
              organization['displayName'], organization['parentId']))
        # pp_json(organization)
else:
    print_err(r)
