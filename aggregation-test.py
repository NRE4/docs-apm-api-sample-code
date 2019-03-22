#
#  Network paths - See how data is aggregated by changing hours_back and
#                  hour_range and seeing how Period changes.
#

import math
from api_fns import *

count = 0
metric = 'availablecapacity'

org_id = '11111'      # organization ID
path_id = 222222      # network path ID
hours_back = 24*0     # the number of hours ago the range ends
hour_range = 24*10    # the number of hours in the range

if (hours_back == 0) & (hour_range == 0):
    start = end = None
else:
    if (hour_range == 0):
        hour_range = 1
    end = math.floor(time.time()-(60*60*hours_back))
    start = (end - math.floor(60*60*hour_range))

print('Start time: {} ({})'.format(time.ctime(start), start))
print('End time:   {} ({})'.format(time.ctime(end), end))
print('Org id:     ({})'.format(org_id))
print('Path id:    ({})'.format(path_id))

r1 = get_network_path_stats_id(org_id, path_id, start, end, metric)
if r1.status_code == requests.codes.ok:
    for network_path_stats in r1.json():
        print('   Network path ({})'.format(network_path_stats['pathId']))
        # pp_json(network_path_stats)

        if network_path_stats['pathId'] == path_id:
            # pp_json(network_path_stats)
            if network_path_stats['instrumentation'] == "ONE_WAY":
                # Single-ended paths have data within 'data'
                for test in network_path_stats['data']['availableCapacity']:
                    count += 1
                    print('      Single-ended path -> Start time={}' +
                          '   Period={}  Available Capacity value={} count={}'
                          .format(time.ctime(test['start']/1000),
                                  test['period'],
                                  math.floor(test['value']), count))
                    # pp_json(test)
            else:
                # Dual-ended paths have data within
                # 'dataInbound' and 'dataOutbound'
                for test in network_path_stats['dataInbound']['availableCapacity']:
                    count += 1
                    print('      Dual-ended path   -> Start time={}' +
                          '   Period={}  Available Capacity value={} count={}'
                          .format(time.ctime(test['start']/1000),
                                  test['period'],
                                  math.floor(test['value']), count))
                    # pp_json(test)

elif r1.status_code == requests.codes.bad_request:
    print_err_json(r1.json())
else:
    print_err(r1)

print('Start time: {} ({})'.format(time.ctime(start), start))
print('End time:   {} ({})'.format(time.ctime(end), end))
