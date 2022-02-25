# Item Type Project Configurator

This project is allow users to add multiple item types to multiple Jama projects using a provided CSV file.

Jama Software is focused on maximizing innovation success. Numerous firsts for humanity in fields such as fuel cells, electrification, space, autonomous vehicles, surgical robotics, and more all rely on Jama Connect® to minimize the risk of product failure, delays, cost overruns, compliance gaps, defects, and rework. Jama Connect uniquely creates Live Traceability™ through siloed development, test, and risk activities to provide end-to-end compliance, risk mitigation, and process improvement. Our rapidly growing customer base of more than 12.5 million users across 30 countries spans the automotive, medical device, life sciences, semiconductor, aerospace & defense, industrial manufacturing, financial services, and insurance industries.

## Installation
This section contains information on how to install the required dependencies for this script.

### Pre-Requisites
* [Python 3.7+](https://www.python.org/downloads/release/python-377/) If using pipenv you must use a python 3.7.X 
version.  If installing requirements manually you may use any python version including 3.8+ however testing has only
been done against python 3.7


* Enable the REST API on your Jama Connect instance

### Pipenv installation (Recommended)
If you do not already have Pipenv installed on your machine you can learn how to install it here: 
[https://pypi.org/project/pipenv/](https://pypi.org/project/pipenv/)


The required dependencies for this project are managed with Pipenv and can be installed by opening a terminal application
to the project directory and entering the following command:
```bash
    pipenv install
```

### Manual installation
If you do not wish to use Pipenv, you may manually install the required dependencies with pip.
```bash
pip install --user py-jama-rest-client
```

Or you can use the requiremnts.txt file as follows
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

## Running the script

1) Open a terminal to the project directory.
2) If using pipenv enter the following (otherwise skip to step 3):
   ```bash
   pipenv shell 
   ``` 
3) Enter the following command into your terminal (Note that the script accepts one parameter and that is the path to
the config file created above):  
   ```bash 
   python project_item_type_configurator.py config.ini
   ```

## Output
Execution logs will be output to the terminal as well as output to a log file in the /logs folder located next to the 
script.