# Sample code for AppNeta APM API

The files in this repository contain sample Python code for accessing the AppNeta APM API. Use them as a basis for understanding in order to create your own code.

To use these files:

1. Clone the repository to your local system (e.g. git clone https://github.com/appneta/docs-apm-api-sample-code.git).
	* A local directory is created.
1. Update the credentials.py file with your APM server URL (e.g. app-01.pm.appneta.com) and APM API credentials ([access token](https://docs.appneta.com/api-access-tokens.html)).
1. [Download and install Python](https://www.python.org/downloads/).
1. Run the sample programs and view the code files to see what they do and how they do it:
	* The "app-..." files (e.g. python3 app-organizations.py) retrieve a variety of APM system data.
	* The "path-..." files create/delete/show network paths identified in "paths.csv" file.
		* Update "paths.csv" with valid information then run any of the "path-..." files (e.g. python3 path-create.py) to see what they do.
	* "aggregation-test.py" is used to show how data is aggregated over time.
	* Functions used in the program files are defined in api_fns.py.
1. Modify any of these files or create your own code to use the APM API.

|**Filename**                           |**Description**                      |
|---------------------------------------|-------------------------------------|
|credentials.py                         |User credentials and server name     |
|api_fns.py                             |Functions to access the APM API      |
|   |   |
|app-appliances.py                      |Prints monitoring point info         |
|app-mp-status.py                       |Prints monitoring point status       |
|app-network-path-info.py               |Prints network path info             |
|app-network-path-stats.py              |Prints network path stats            |
|app-network-path-status.py             |Prints network path status           |
|app-network-path-status-group.py       |Prints network path status by group  |
|app-network-path-status-saved-list.py  |Prints network path status by saved list            |
|app-organizations.py                   |Prints organization info             |
|app-web-path-info.py                   |Prints web path info                 |
|app-web-path-stats-group.py            |Prints web path stats info by group  |
|app-web-path-stats.py                  |Prints web path stats info           |
|app-web-path-status-org.py             |Prints web path status by organization  |
|app-web-path-status.py                 |Prints web path status               |
|   |   |
|paths.csv                              |List of paths to create/delete/show  |
|path-create.py                         |Create paths in "paths.csv" file     |
|path-delete.py                         |Delete paths in "paths.csv" file     |
|path-show.py                           |Show paths in "paths.csv" file       |
|   |   |
|aggregation-test.py                    |Shows how data is aggregated         |
