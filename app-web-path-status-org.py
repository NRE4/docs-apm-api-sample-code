#
# Print web path status for all web paths (grouped by org then web app group)
#
from api_fns import *

r1 = get_org()
if r1.status_code == requests.codes.ok:
	for organization in r1.json():
		print('Org ({}) name --> {}'.format(organization['id'], organization['displayName']))

		r2 = get_web_app_group(organization['id'])
		if r2.status_code == requests.codes.ok:
			for group in r2.json():
				print('   Web app group ({}) name - {} -- org id ({})'.format(group['id'], group['name'], group['orgId']))

				r3 = get_web_path(group['id'])
				if r3.status_code == requests.codes.ok:
					for web_path in r3.json():
						print('      Web path ({}) status --> {}'.format(web_path['id'], web_path['status']))
						# pp_json(web_path)
				else:
					print_err(r3)
		else:
			print_err(r2)
else:
	print_err(r1)
