#
# Functions to access the AppNeta APM API
#
import requests
import json
import time
from credentials import username, password, apm_server

api_key = "api_key=v3"


#
# Print error response code and error text returned
#
def print_err(resp):
	print('***Response code: {}***'.format(resp.status_code))
	print(resp.text)


#
# Print HTTP response code and error text returned with JSON formatted errors
#
def print_err_json(resp_json):
	print('***HTTP response: {} - {}***'.format(resp_json['httpStatusCode'], resp_json['messages'][0]))
	#pp_json(resp_json)


#
# Pretty print json. Useful to view JSON formatted response data.
#	json_obj - JSON object to be printed
#	sort - whether to sort the JSON data
#	indents - number of spaces for indents
#
def pp_json(json_obj, sort=True, indents=4):
    if type(json_obj) is str:
        print(json.dumps(json.loads(json_obj), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_obj, sort_keys=sort, indent=indents))
    return None


#
# Get organization info (GET /v3/organization)
# - Returns all organizations associated with the current user.
#
def get_org():
	url = "https://{}/api/v3/organization?{}".format(apm_server, api_key)
	return(requests.get(url, auth=(username, password)))


#
# Get appliance (monitoring point) info (GET /v3/appliance (with orgId parameter))
# - Returns appliance info for the specified organization. If org_id is "None" then info for all appliances is returned.
# 	org_id - organization id
#
def get_appliance(org_id=None):
	url = "https://{}/api/v3/appliance?".format(apm_server)
	if org_id != None:
		url += "orgId={}&".format(org_id)
	url += api_key
	return(requests.get(url, auth=(username, password)))


#
# Get appliance (monitoring point) info for the specific appliance (GET /v3/appliance/{id})
# - Returns appliance info for the specified appliance.
# 	appliance_id - appliance id
#
def get_appliance_id(appliance_id):
	url = "https://{}/api/v3/appliance/{}?{}".format(apm_server, appliance_id, api_key)
	return(requests.get(url, auth=(username, password)))


#
# Get web app group info (GET /v3/webApplication)
# - Returns web app group info for the specified organization. If org_id is "None" then info for all web app groups is returned.
# 	org_id - organization id
#
def get_web_app_group(org_id=None):
	url = "https://{}/api/v3/webApplication?".format(apm_server)
	if org_id != None:
		url += "orgId={}&".format(org_id)
	url += api_key
	return(requests.get(url, auth=(username, password)))


#
# Get web app group info for a specified web app group (GET /v3/webApplication/{web_app_grp_id})
# - Returns web app group info for the specified web app group
# 	web_app_grp_id - web app group id
#
def get_web_app_group_id(web_app_grp_id):
	url = "https://{}/api/v3/webApplication/{}?{}".format(apm_server, web_app_grp_id, api_key)
	return(requests.get(url, auth=(username, password)))


#
# Get web path info for paths in a web app group (GET /v3/webApplication/{web_app_grp_id}/monitor)
# - Returns web path info for the paths in the specified web app group.
# 	web_app_grp_id - web app group id
#
def get_web_path(web_app_grp_id):
	url = "https://{}/api/v3/webApplication/{}/monitor?{}".format(apm_server, web_app_grp_id, api_key)
	return(requests.get(url, auth=(username, password)))


#
# Get web path stats (GET /v3/webPath/data)
# - Returns web path stats for the specified organization. If org_id is "None" then info for all organizations is returned.
# 	org_id - organization id
# 	start_time - the start time of the time range in UNIX/epoch time
# 	end_time - the end time of the time range in UNIX/epoch time
# 		If no start or end time, stats for the last hour are returned
#
def get_web_path_stats(org_id=None, start_time=None, end_time=None):
	url = "https://{}/api/v3/webPath/data?".format(apm_server)
	if org_id != None:
		url += "orgId={}&".format(org_id)
	if start_time != None:
		url += "from={}&".format(start_time)
	if end_time != None:
		url += "to={}&".format(end_time)
	url += api_key
	return(requests.get(url, auth=(username, password)))


#
# Get web path stats for a specific web path over a given time range. (GET /v3/webApplication/{web_app_group_id}/monitor/{web_path_id}/data)
# If no time range is specified, data for the last hour is returned.
# - Returns web path stats for the specified web app group / web path
# 	web_app_group_id - web app group id
# 	web_path_id - web path id
# 	start_time - the start time of the time range in UNIX/epoch time
# 	end_time - the end time of the time range in UNIX/epoch time
# 		If no start or end time, stats for the last hour are returned
# 	metric - the type of data to return ("networktiming", "servertiming", "browsertiming").
# 		If no metric is specified, all types are returned.
#
def get_web_path_stats_id(web_app_group_id, web_path_id, start_time=None, end_time=None, metric=None):
	url = "https://{}/api/v3/webApplication/{}/monitor/{}/data?".format(apm_server, web_app_group_id, web_path_id)
	if start_time != None:
		url += "from={}&".format(start_time)
	if end_time != None:
		url += "to={}&".format(end_time)
	if metric != None:
		url += "metric={}&".format(metric)
	url += api_key
	return(requests.get(url, auth=(username, password)))


#
# Get network path info (GET /v3/path)
# - Returns network path info for the specified organization. If org_id is "None" then info for all organizations is returned.
# 	org_id - organization id
#
def get_network_path(org_id=None):
	url = "https://{}/api/v3/path?".format(apm_server)
	if org_id != None:
		url += "orgId={}&".format(org_id)
	url += api_key
	return(requests.get(url, auth=(username, password)))


#
# Determine the network path ID given an org ID, source MP name, and target
# - Returns the network path ID or 0 if it can't be found
#	org_id - organization id
#	source_mp_name - source MP name to match
#	target - target to match
#
def get_network_path_id(org_id, source_mp_name, target):
	r1 = get_network_path(org_id)
	if r1.status_code == requests.codes.ok:
		for network_path in r1.json():
			# pp_json(network_path)
			if network_path['sourceAppliance'] == source_mp_name and network_path['target'] == target:
				return(network_path['id'])
		return(0)
	else:
		return(0)


#
# Get network path status (GET /v3/path/status)
# - Returns network path status for the specified organization. If org_id is "None" then info for all organizations is returned.
# 	org_id - organization id
#
def get_network_path_status(org_id=None):
	url = "https://{}/api/v3/path/status?".format(apm_server)
	if org_id != None:
		url += "orgId={}&".format(org_id)
	url += api_key
	return(requests.get(url, auth=(username, password)))


#
# Get network path status for a specified path (GET /v3/path/{id}/status)
# - Returns network path status (string) for the specified path.
# 	path_id - network path id
#
def get_network_path_status_id(path_id):
	url = "https://{}/api/v3/path/{}/status?{}".format(apm_server, path_id, api_key)
	return(requests.get(url, auth=(username, password)))


#
# Get network path stats (GET /v3/path/data)
# - Returns network path stats for the specified organization. If org_id is "None" then info for all organizations is returned.
# 	org_id - organization id
# 	start_time - the start time of the time range in UNIX/epoch time
# 	end_time - the end time of the time range in UNIX/epoch time
# 		If no start or end time, stats for the last hour are returned
# 	metric - the type of data to return ("totalcapacity", "utilizedcapacity", "availablecapacity", "latency", "datajitter", "dataloss", "voicejitter", "voiceloss", "mos", "rtt", "twamprtt", "twampjitter", "twamploss").
#		If no metric is specified, all types are returned.
#
def get_network_path_stats(org_id=None, start_time=None, end_time=None, metric=None):
	url = "https://{}/api/v3/path/data?".format(apm_server)
	if org_id != None:
		url += "orgId={}&".format(org_id)
	if start_time != None:
		url += "from={}&".format(start_time)
	if end_time != None:
		url += "to={}&".format(end_time)
	if metric != None:
		url += "metric={}&".format(metric)
	url += api_key
	return(requests.get(url, auth=(username, password)))


#
# Create a network path (POST /v3/path (using an org ID, source MP name, and target in request body))
# - Creates the network path using an org ID, source MP name, and target
#	org_id - organization id
#	source_mp_name - source MP
#	target - target
#
def create_network_path(org_id, source_mp_name, target):
	url = "https://{}/api/v3/path?{}".format(apm_server, api_key)
	headers = {
		"Content-Type": "application/json"
	}
	body = {
		"sourceAppliance": source_mp_name,
		"target": target,
		"orgId": org_id
	}
	return(requests.post(url, headers=headers, auth=(username, password), json=body))


#
# Delete a network path (DELETE /v3/path/{id} (with network path ID parameter))
# - Deletes the network path identified using an org ID, source MP name, and target
#	org_id - organization id
#	source_mp_name - source MP name to match
#	target - target to match
#
def delete_network_path(org_id, source_mp_name, target):
	network_path_id = get_network_path_id(org_id, source_mp_name, target)
	url = "https://{}/api/v3/path/{}?{}".format(apm_server, network_path_id, api_key)
	return(requests.delete(url, auth=(username, password)))


#
# Get saved list info (GET /v3/savedList (with orgId parameter))
# - Returns saved list info for the specified organization.
# 	org_id - organization id
#
def get_saved_lists(org_id):
	url = "https://{}/api/v3/savedList?orgId={}&{}".format(apm_server, org_id, api_key)
	return(requests.get(url, auth=(username, password)))


#
# Get group info (GET /v3/group (with orgId parameter))
# - Returns group info for the specified organization. If org_id is "None" then info for all groups is returned.
# 	org_id - organization id
#
def get_groups(org_id=None):
	url = "https://{}/api/v3/group?".format(apm_server)
	if org_id != None:
		url += "orgId={}&".format(org_id)
	url += api_key
	return(requests.get(url, auth=(username, password)))
