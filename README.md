# Item Type Project Configurator

This project is allow users to add multiple item types to multiple Jama projects using a provided CSV file.

Jama Software is focused on maximizing innovation success. Numerous firsts for humanity in fields such as fuel cells, electrification, space, autonomous vehicles, surgical robotics, and more all rely on Jama Connect® to minimize the risk of product failure, delays, cost overruns, compliance gaps, defects, and rework. Jama Connect uniquely creates Live Traceability™ through siloed development, test, and risk activities to provide end-to-end compliance, risk mitigation, and process improvement. Our rapidly growing customer base of more than 12.5 million users across 30 countries spans the automotive, medical device, life sciences, semiconductor, aerospace & defense, industrial manufacturing, financial services, and insurance industries.

## Installation
This section contains information on how to install the required dependencies for this script.

### Pre-Requisites
* [Python 3.7+](https://www.python.org/downloads/release/python-377/)

* Enable the REST API on your Jama Connect instance

### Installation
 Install the required dependencies with pip.
```bash
pip install -r requirements.txt
```

## Usage
This section contains information on configuration and execution the script.

### Configuration
Before you can execute the script, you must configure the script via a config file.  The config file is
structured in a standard .ini file format. there is a config.ini file included with this repo that you
will need to modify with your settings.

#### Config.ini Fields:
This section contains settings related to connecting to your Jama Connect REST API.

* jama_connect_url: This is the URL to your Jama Connect instance.

* oauth: Setting this value to 'false' will instruct the client to authenticate via basic authentication.  Setting this 
value to 'true' instructs the client to use OAuth authentication protocols.

* user_id: This should be either your username or clientID if using OAuth.

* user_secret: This should be either your password or client_secret if using OAuth.

* csv_file_path: The local file path to the CSV file to use.


#### CSV File structure
The CSV file should have 2 columns.  The first cloumn should have a header of "Project ID". the second column should have a header of "Item Type ID". The values in the cells should be the API ID's of the project and/or item type.

ex: 
| Project ID     | Item Type ID |
| ---            | ---          |
| 42             | 19           |
| 43             | 19           |
| 43             | 20           |

## Running the script

1) Open a terminal to the project directory.
2) Enter the following command into your terminal (Note that the script accepts one parameter and that is the path to
the config file created above):  
   ```bash 
   python project_item_type_configurator.py config.ini
   ```

## Output
Execution logs will be output to the terminal as well as output to a log file in the /logs folder located next to the 
script.


