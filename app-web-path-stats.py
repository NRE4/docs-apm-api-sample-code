#
# Print web path stats for all web paths (grouped by organization)
#
from api_fns import *

r1 = get_org()
if r1.status_code == requests.codes.ok:
	for organization in r1.json():
		print('Org ({}) name --> {}'.format(organization['id'], organization['displayName']))

		r2 = get_web_path_stats(organization['id'])
		if r2.status_code == requests.codes.ok:
			for web_path_stats in r2.json():
				print('   Web path ({})'.format(web_path_stats['webPathId']))
				#pp_json(web_path_stats)

				if len(web_path_stats['milestones']) > 0:
					for test in web_path_stats['milestones'][0]['networkTiming']:
						#pp_json(test)
						print('      Start time={}   Network Timing value={}'.format(time.ctime(test['start']/1000), test['value']))

		elif r2.status_code == requests.codes.bad_request:
			print_err_json(r2.json())
		else:
			print_err(r2)
else:
	print_err(r1)
