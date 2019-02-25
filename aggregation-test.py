#
#  Network paths - See how data is aggregated by changing days_back and day_range and seeing how Period changes.
#

import math
from api_fns import *

count = 0
org_id = '11111'
path_id = 22222

days_back = 0    # the number of days ago the range ends
day_range = 30   # the number of days in the range

metric = 'availablecapacity'
end = math.floor(time.time()-(60*60*24*days_back))
start = (end - (60*60*24*day_range))

print('Start time: {} ({})'.format(time.ctime(start), start))
print('End time:   {} ({})'.format(time.ctime(end), end))
print('Org id:     ({})'.format(org_id))
print('Path id:    ({})'.format(path_id))


r1 = get_network_path_stats(org_id, start, end, metric)
if r1.status_code == requests.codes.ok:
	for network_path_stats in r1.json():
		print('   Network path ({})'.format(network_path_stats['pathId']))
		#pp_json(network_path_stats)

		if network_path_stats['pathId'] == path_id:
			#pp_json(network_path_stats)
			for test in network_path_stats['data']['availableCapacity']:
				count += 1
				print('      Start time={}   Period={}  Available Capacity value={} count={}'.format(time.ctime(test['start']/1000), test['period'], math.floor(test['value']), count))
				#pp_json(test)

elif r1.status_code == requests.codes.bad_request:
	print_err_json(r1.json())
else:
	print_err(r1)


print('Start time: {} ({})'.format(time.ctime(start), start))
print('End time:   {} ({})'.format(time.ctime(end), end))
