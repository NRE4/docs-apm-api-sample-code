#
# Delete paths matching those in "paths.csv" (Note: No space before or after commas in paths.csv)
# (Requests status codes - https://github.com/requests/requests/blob/master/requests/status_codes.py)
#

import csv
from api_fns import *

with open('paths.csv', mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for row in csv_reader:
		#pp_json(row)

		r1 = get_network_path(row['org_id'])
		if r1.status_code == requests.codes.ok:
			for network_path in r1.json():
				if network_path['sourceAppliance'] == row['source_mp'] and network_path['target'] == row['target']:

					r2 = delete_network_path(row['org_id'], row['source_mp'], row['target'])
					if r2.status_code == requests.codes.no_content:
						print('Deleted successfully: Org id = {}, Source MP = {}, Target = {} -> Network path ({}) ({})'.format(row['org_id'], network_path['sourceAppliance'], network_path['target'], network_path['id'], network_path['pathName']))
					else:
						print('Unable to delete: {}'.format(r2.json()['messages'][0]))
		else:
			print_err(r1)
