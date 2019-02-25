#
# Print network path stats for all web paths (grouped by organization)
#
from api_fns import *

r1 = get_org()
if r1.status_code == requests.codes.ok:
	for organization in r1.json():
		print('Org ({}) name --> {}'.format(organization['id'], organization['displayName']))

		r2 = get_network_path_stats(organization['id'])
		if r2.status_code == requests.codes.ok:
			for network_path_stats in r2.json():
				print('   Network path ({})'.format(network_path_stats['pathId']))
				#pp_json(network_path_stats)

				for test in network_path_stats['data']['totalCapacity']:
					print('      Start time={}   Total Capacity value={}'.format(time.ctime(test['start']/1000), test['value']))
					#pp_json(test)
		elif r2.status_code == requests.codes.bad_request:
			print_err_json(r2.json())
		else:
			print_err(r2)
else:
	print_err(r1)
