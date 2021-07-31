#!/usr/bin/env python3
import fileinput
import sys
import argparse
import json
import boto3

# accept piped stdin
# parse json
# create_record(zone, name, ip)
#   input['control_plane_names'][0]['value']
#   input['control_plane_ips'][0]['value']
# delete_record(zone, name)
#
def create_record():
    pass

def collect_input():
    raw = None
    for line in fileinput.input(sys.argv[2:]):
        raw = line

    try:
        cooked = json.loads(raw)
    except json.decoder.JSONDecodeError as e:
        print(f"Error: Unable to parse input as json: {e}")
        sys.exit(1)
    return cooked

def main():
    parser = argparse.ArgumentParser(description='Manage lightsail dns records')
    parser.add_argument('-c', '--create', action='store_true', help='create a record')
    parser.add_argument('-d', '--delete', action='store_true', help='delete a record')
    args = parser.parse_args()

    data = collect_input()
    print(data)
    if args.create:
        create_record()
    if args.delete:
        print(args.delete)


if __name__ == '__main__':
    main()
