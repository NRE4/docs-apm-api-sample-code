#
# Print network path info (grouped by organization)
#
from api_fns import *

r1 = get_org()
if r1.status_code == requests.codes.ok:
    for organization in r1.json():
        print('Org ({}) name --> {}'.format(organization['id'],
              organization['displayName']))

        r2 = get_network_path(organization['id'])
        if r2.status_code == requests.codes.ok:
            for network_path in r2.json():
                if network_path['asymmetric']:
                    instrumentation = "Dual-ended,  "
                else:
                    instrumentation = "Single-ended,"
                print('   Network path ({}) {} name - {}'
                      .format(network_path['id'],
                              instrumentation, network_path['pathName']))
                # pp_json(network_path)
        else:
            print_err(r2)
else:
    print_err(r1)
