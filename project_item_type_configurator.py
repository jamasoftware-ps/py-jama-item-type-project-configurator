import configparser
import datetime
import json
import logging
import os
import sys
import csv

from py_jama_rest_client.core import Core, CoreException

global path_to_config
global instance_url

logger = logging.getLogger(__name__)


def init_logging():
    try:
        os.makedirs('logs')
    except FileExistsError:
        pass
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    log_file = 'logs/project_item_type_configurator_' + str(current_date_time) + '.log'
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def parse_config():
    # allow the user to shorthand this and just look for the 'config.ini' file
    if len(sys.argv) == 1:
        current_dir = os.path.dirname(__file__)
        path_to_config = 'config.ini'
        if not os.path.isabs(path_to_config):
            path_to_config = os.path.join(current_dir, path_to_config)

    # use the config file location
    if len(sys.argv) == 2:
        current_dir = os.path.dirname(__file__)
        path_to_config = sys.argv[1]
        if not os.path.isabs(path_to_config):
            path_to_config = os.path.join(current_dir, path_to_config)

    # Parse config file.
    configuration = configparser.ConfigParser()
    try:
        with open(path_to_config, encoding="utf8", errors='ignore') as file:
            configuration.read_file(file)
    except Exception as e:
        logger.error("Unable to parse configuration file. exception: " + str(e))
        exit(1)

    return configuration


def create_jama_core(config: configparser.ConfigParser):
    url = None
    user_id = None
    user_secret = None
    oauth = None
    try:
        url = config.get('CLIENT_SETTINGS', 'jama_connect_url').strip()
        while url.endswith('/') and url != 'https://' and url != 'http://':
            url = url[0:len(url) - 1]

        if not (url.startswith('https://') or url.startswith('http://')):
            url = 'https://' + url

        oauth = config.getboolean('CLIENT_SETTINGS', 'oauth')
        user_id = config.get('CLIENT_SETTINGS', 'user_id').strip()
        user_secret = config.get('CLIENT_SETTINGS', 'user_secret').strip()

    except configparser.Error as config_error:
        logger.error("Unable to parse CLIENT_SETTINGS from config file because: {}, "
                     "Please check config file for errors and try again."
                     .format(str(config_error)))
        exit(1)

    return Core(url, (user_id, user_secret), oauth=oauth)


def update_project_item_types(config: configparser.ConfigParser):
    # Get script settings from config
    csv_file_path = None

    # try and grab the settings from the config file
    try:
        csv_file_path = config.get('SCRIPT_SETTINGS', 'csv_file_path')

    except configparser.Error as config_error:
        logger.error("Unable to parse SCRIPT_SETTINGS because: {} Please check settings and try again."
                     .format(str(config_error)))
        exit(1)

    csv_lines_read = 0
    csv_errors = 0

    # Open the CSV file for reading, use the utf-8-sig encoding to deal with excel file type outputs.
    with open(str(csv_file_path), encoding='utf-8-sig') as open_csv_file:
        csv_dict_reader = csv.DictReader(open_csv_file)
        # Begin processing the data in the CSV file.
        for row_number, row_data in enumerate(csv_dict_reader):
            # For each row in the CSV file, we will append an object to a list for later processing
            csv_lines_read += 1

            project_id = row_data['Project ID']
            item_type_id = row_data['Item Type ID']

            api_response = jama_core.put('projects/{}/itemtypes/{}'.format(project_id, item_type_id),
                          headers={'content-type': 'application/json'})

            if api_response.status_code in range(200, 300):
                logger.info('Successfully added item type {} to project: {}'.format(item_type_id, project_id))
            else:
                logger.error("Unable to add item type {} to project: {}. Reason: {}"
                             .format(item_type_id, project_id, json.loads(api_response.text)))
                csv_errors += 1

    logger.info('Processed ' + str(csv_lines_read) + ' rows.')
    logger.info('There were ' + str(csv_errors) + ' errors.')


if __name__ == "__main__":
    # Setup logging
    init_logging()

    # Get Config File Path
    conf = parse_config()

    # Create Jama Client
    jama_core = create_jama_core(conf)

    # Begin business logic
    update_project_item_types(conf)

    logger.info("Done")