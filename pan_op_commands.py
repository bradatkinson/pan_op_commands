#!/usr/bin/env python3
#
#  AUTHOR: Brad Atkinson
#    DATE: 1/17/2021
# PURPOSE: To run operational commands such as 'show' commands on a provided
# list of Palo Alto Networks devices

import argparse
import xmltodict
import json
from panos import base
import config


def connect_device(fw_ip):
    """Connect To Device
    
    Returns:
        fw_conn (PanDevice): A panos object for device
    """
    username = config.paloalto['username']
    password = config.paloalto['password']
    fw_conn = base.PanDevice.create_from_device(
        hostname=fw_ip,
        api_username=username,
        api_password=password)
    return fw_conn


def operational_commands(fw_conn, cmd):
    """Operational Command

    Args:
        fw_conn (PanDevice): A panos object for device
        cmd (str): [description]

    Returns:
        xml_output (Element): XML results from firewall
    """
    xml_output = fw_conn.op(cmd=cmd, xml=True, cmd_xml=True)
    return xml_output


def process_op_commands(xml_output):
    """Process Operational Command

    Args:
        xml_output (Element): XML results from firewall

    Returns:
        json_output (dict): Results in JSON output
    """
    obj_dict = xmltodict.parse(xml_output)
    json_output = json.dumps(obj_dict)
    return json_output


def main():
    """Function Calls
    """
    parser = argparse.ArgumentParser(description='To run operational commands')
    parser.add_argument('-l', '--list',
                        type=str,
                        metavar='',
                        required=True,
                        help='A list of IP addresses in a text file')
    parser.add_argument('-a', '--api',
                        type=str,
                        metavar='',
                        required=True,
                        help='The API command to run')
    args = parser.parse_args()

    with open(args.list, 'r') as ip_file:
        ip_list = ip_file.read().splitlines()

    for fw_ip in ip_list:
        fw_conn = connect_device(fw_ip)
        xml_output = operational_commands(fw_conn, args.api)
        json_output = process_op_commands(xml_output)
        print(json_output)


if __name__ == '__main__':
    main()
