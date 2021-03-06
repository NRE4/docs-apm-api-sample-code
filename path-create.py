#
# Create paths from info in "paths.csv"
# (Note: No space before or after commas in paths.csv)
# (Requests status codes -
#   https://github.com/requests/requests/blob/master/requests/status_codes.py)
#

import csv
from api_fns import *

with open('paths.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # pp_json(row)

        r1 = create_network_path(row['org_id'], row['source_mp'],
                                 row['target'])
        if r1.status_code == requests.codes.created:
            print('Created: org/src/targ {}/{}/{}'
                  .format(row['org_id'], row['source_mp'], row['target']))
        else:
            print('Unable to create: {}'.format(r1.json()['messages'][0]))

        network_path_id = get_network_path_id(row['org_id'], row['source_mp'],
                                              row['target'])

        r2 = add_network_path_location(network_path_id, row['location'])
        if r2.status_code == requests.codes.ok:
            print('Added location successfully: {}.'.format(row['location']))
        else:
            print('Unable to add location: {}.'.format(row['location']))
