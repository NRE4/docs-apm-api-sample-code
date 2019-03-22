#
# Print network path status (grouped by organization then by group)
#
from api_fns import *

r1 = get_org()
if r1.status_code == requests.codes.ok:
    for organization in r1.json():
        print('Org ({}) name --> {}'.format(organization['id'],
              organization['displayName']))

        r2 = get_groups(organization['id'])
        if r2.status_code == requests.codes.ok:
            for group in r2.json():
                print('   Group ({}) name --> {}'.format(group['id'],
                      group['name']))
                # pp_json(saved_lists)
                for network_path_id in group['paths']:

                    r3 = get_network_path_status_id(network_path_id)
                    if r3.status_code == requests.codes.ok:
                        print('      Network path ({}) status --> {}'
                              .format(network_path_id, r3.json()))
                    else:
                        print_err(r3)
        else:
            print_err(r2)
else:
    print_err(r1)
