import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="start a flask project or app")
    parser.add_argument("name", help="flask project or app name")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.cmd == 'startproject':
        print(f'Will create Flask project with name {args.name}')
    elif args.cmd == 'startapp':
        print(f'Will create Flask app with name {args.name}')
