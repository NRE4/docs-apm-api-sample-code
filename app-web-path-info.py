#
# Print web path info (grouped by web app group)
#
from api_fns import *

r1 = get_web_app_group()
if r1.status_code == requests.codes.ok:
    for group in r1.json():
        print('Web app group ({}) name - {} -- org id ({})'.format(group['id'],
              group['name'], group['orgId']))

        r2 = get_web_path(group['id'])
        if r2.status_code == requests.codes.ok:
            for web_path in r2.json():
                print('   Web path id ({}) MP ({}), target ({}), workflow ({})'
                      .format(web_path['id'],
                              web_path['location']['applianceName'],
                              web_path['target']['url'],
                              web_path['userFlow']['name']))
                # pp_json(web_path)
        else:
            print_err(r2)
else:
    print_err(r1)
