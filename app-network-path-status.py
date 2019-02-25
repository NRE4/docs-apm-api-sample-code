#
# Print network path status (grouped by organization)
#
from api_fns import *

r1 = get_org()
if r1.status_code == requests.codes.ok:
	for organization in r1.json():
		print('Org ({}) name --> {}'.format(organization['id'], organization['displayName']))

		r2 = get_network_path_status(organization['id'])
		if r2.status_code == requests.codes.ok:
			for network_path_status in r2.json():
				print('   Network path ({}) status --> {}'.format(network_path_status['pathId'], network_path_status['status']))
				# pp_json(network_path_status)
		else:
			print_err(r2)
else:
	print_err(r1)
