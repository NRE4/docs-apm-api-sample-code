#
# Show any paths that match those found in the "paths.csv" file
#

import csv
from api_fns import *

with open('paths.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # pp_json(row)

        r1 = get_network_path(row['org_id'])
        if r1.status_code == requests.codes.ok:
            for network_path in r1.json():
                if (network_path['sourceAppliance'] == row['source_mp']
                        and network_path['target'] == row['target']):
                    print('Match:   org/src/targ {}/{}/{} -> id/name {}/{}'
                          .format(row['org_id'],
                                  network_path['sourceAppliance'],
                                  network_path['target'],
                                  network_path['id'],
                                  network_path['pathName']))
                    # pp_json(network_path)
        else:
            print_err(r1)
