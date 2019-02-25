#
# Print monitoring point info (grouped by organization)
#
from api_fns import *

r1 = get_org()
if r1.status_code == requests.codes.ok:
	for organization in r1.json():
		print('Org ({}) name --> {}'.format(organization['id'], organization['displayName']))

		r2 = get_appliance(organization['id'])
		if r2.status_code == requests.codes.ok:
			for appliance in r2.json():
				print('   MP: {}, {}, {}'.format(appliance['id'], appliance['resolvedIp'], appliance['name']))
				# pp_json(appliance)
		else:
			print_err(r2)
else:
	print_err(r1)
