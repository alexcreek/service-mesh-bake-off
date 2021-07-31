#!/usr/bin/env python3
import fileinput
import sys
import argparse
import json
import boto3

# create_record(zone, name, ip)
#   input['control_plane_names'][0]['value']
#   input['control_plane_ips'][0]['value']
# delete_record(zone, name)

def collect_input():
    """
    Reads piped json from stdin
    :return cooked: dict of parsed json
    """
    raw = None
    for line in fileinput.input(sys.argv[2:]):
        raw = line

    try:
        cooked = json.loads(raw)
    except json.decoder.JSONDecodeError as e:
        print(f"Error: Unable to parse input as json: {e}")
        sys.exit(1)
    return cooked

def create_records(data):
    """
    Upserts dns records
    :param data: dict containing hostnames and ips
    """

def delete_records(data):
    """
    Deletes dns records
    :param data: dict containing hostnames and ips
    """

def main():
    parser = argparse.ArgumentParser(description="Manage lightsail dns records using piped tf output")
    parser.add_argument('-c', '--create', action='store_true', help='create records')
    parser.add_argument('-d', '--delete', action='store_true', help='delete records')
    args = parser.parse_args()

    if args.create:
        data = collect_input()
        create_records(data)
    if args.delete:
        data = collect_input()
        delete_records(data)


if __name__ == '__main__':
    main()
