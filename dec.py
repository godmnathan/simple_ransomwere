from cryptography.fernet import Fernet
import os
import sys

dirDefault = 'Archives'
ignoreFileList = [os.path.basename(__file__), 'key.key', 'enc.py', 'dec.py']

def listFiles(baseDir):
    allFiles = []
    for entry in os.listdir(baseDir):
        fullPath = os.path.abspath(os.path.join(baseDir, entry))
        if os.path.isdir(fullPath):
            allFiles += listFiles(fullPath)
        elif os.path.isfile(fullPath) and entry is not ignoreFileList:
            allFiles.append(fullPath)
    return allFiles

def main():sss

    dir = sys.argv[1] if len(sys.argv) > 1 else dirDefault
    archives = listFiles(dir)

    for archive in archives:
        print(f'{archive}')

if __name__ == '__main__':
    main()