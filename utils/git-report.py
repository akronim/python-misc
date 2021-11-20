#!/usr/bin/env python

import subprocess
import os
import argparse

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest='author', type=str, help="github username")
parser.add_argument(dest='directory', type=str,
                    help="/full/path/to/the/repos/dir/")

# Parse and print the results
args = parser.parse_args()

AUTHOR = args.author
DIR_PATH = args.directory

dir_paths = os.listdir(DIR_PATH)

repos = []

def search_dirs():
    for dir_path in dir_paths:
        file = os.path.join(DIR_PATH, dir_path)
        if(os.path.isdir(file)):
            print(file)
            if(os.path.exists(os.path.join(file, ".git"))):
                repos.append(os.path.join(DIR_PATH, dir_path))


def show_logs():
    commits = ""
    for dir in repos:
        command = 'cd ' + dir + ' && git log --branches=* ' + \
            '--author="' + AUTHOR + \
            '" --since="1 month ago" --reverse --pretty=format:"%h (%cs) %s  <%an>" '

        commits = subprocess.getstatusoutput(command)[1]

        if(
            len(commits) > 0 and
            "Not a directory" not in commits and
            "Not a git repository" not in commits
        ):

            print(os.path.relpath(dir, DIR_PATH))

            commits = [' '.join(['-'] + commit.split(' '))
                       for commit in commits.split('\n')]

            print('\n'.join(commits) + '\n')


search_dirs()
show_logs()
