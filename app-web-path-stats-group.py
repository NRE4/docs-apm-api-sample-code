#
# Print web path stats for all web paths (grouped by web app group)
#
from api_fns import *

r1 = get_web_app_group(None)
if r1.status_code == requests.codes.ok:
    for group in r1.json():
        print('Web app group ({}) name - {} -- org id ({})'.format(group['id'],
              group['name'], group['orgId']))

        r2 = get_web_path(group['id'])
        if r2.status_code == requests.codes.ok:
            for web_path in r2.json():
                print("   Web path id ({})".format(web_path['id']))

                r3 = get_web_path_stats_id(group['id'], web_path['id'])
                if r3.status_code == requests.codes.ok:
                    for web_path_stats in r3.json()['milestones']:
                        for test in web_path_stats['networkTiming']:
                            print('      Start time={} Network Timing value={}'
                                  .format(time.ctime(test['start']/1000),
                                          test['value']))
                            # pp_json(test)

                else:
                    print_err(r3)
        else:
            print_err(r2)
else:
    print_err(r1)
