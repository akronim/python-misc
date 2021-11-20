#!/usr/bin/env python

import subprocess
import os
import argparse

AUTHOR = ""
BASE_DIR_PATH = ""

repos = []


def search_dirs(dir_paths, iteration):
    iteration += 1

    if(iteration <= 3):
        next_level_list = []
        for dir_path in dir_paths:
            file = os.path.join(BASE_DIR_PATH, dir_path)
            if(os.path.isdir(file)):
                if(os.path.exists(os.path.join(file, ".git"))):
                    repos.append(file)
                else:
                    next_level = []
                    next_level += os.listdir(file)
                    for nl in next_level:
                        next_level_list.append(dir_path + "/" + nl)
        if next_level_list:
            search_dirs(next_level_list, iteration)


def show_logs():
    commits = ""
    for dir in repos:
        command = 'cd ' + dir + ' && git log --branches=* ' + \
            '--author="' + AUTHOR + \
            '" --since="1 month ago" --reverse --pretty=format:"%h (%cs) %s  <%an>" '

        commits = subprocess.getstatusoutput(command)[1]

        if(len(commits) > 0):

            print(os.path.relpath(dir, BASE_DIR_PATH))

            commits = [' '.join(['-'] + commit.split(' '))
                       for commit in commits.split('\n')]

            print('\n'.join(commits) + '\n')


def main(dir_paths):
    search_dirs(dir_paths, 0)
    show_logs()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='author', type=str, help="github username")
    parser.add_argument(dest='directory', type=str,
                        help="/full/path/to/the/repos/dir/")

    args = parser.parse_args()

    AUTHOR = args.author
    BASE_DIR_PATH = args.directory

    dir_paths = os.listdir(BASE_DIR_PATH)
    main(dir_paths)
