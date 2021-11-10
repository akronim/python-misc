# Pythono3 code to rename multiple
# files in a directory or folder

import os
import re

# Function to rename multiple files

def main():
    for count, filename in enumerate(os.listdir()):
        x = re.search("^app_\d{1,5}\_", filename)
        if x:
            dst = filename.replace(x.group(), '')
            os.rename(filename, dst)

# Driver Code
if __name__ == '__main__':
    main()
