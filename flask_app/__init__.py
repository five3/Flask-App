import os
import shutil
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
        dir_name = os.path.dirname(__file__)
        source_dir = os.path.join(dir_name, 'templates', 'project_tmpl')
        dist_dir = os.path.join(os.getcwd(), args.name)
        print(f'Create project at {dist_dir} with name {args.name} Success!')
        shutil.copytree(source_dir, dist_dir)
    elif args.cmd == 'startapp':
        print(f'Will create Flask app with name {args.name}')
        dir_name = os.path.dirname(__file__)
        source_dir = os.path.join(dir_name, 'templates', 'app_tmpl')
        dist_dir = os.path.join(os.getcwd(), args.name)
        print(f'Create app at {dist_dir} with name {args.name} Success!')
        shutil.copytree(source_dir, dist_dir)
