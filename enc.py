from cryptography.fernet import Fernet
import os
import sys

# Function to encrypt files
def encryptFiles(key,files):
    for filePath in files:
        with open(filePath,'rb') as binFile:
            content = binFile.read()
        encryptContent = Fernet(key).encrypt(content)
        with open(filePath,'wb') as binFile:
            binFile.write(encryptContent)

# Function to list files
def listFiles(baseDir):
    allFiles = []
    for entry in os.listdir(baseDir):
        fullPath = os.path.abspath(os.path.join(baseDir, entry))
        if os.path.isdir(fullPath):
            allFiles += listFiles(fullPath)
        elif os.path.isfile(fullPath) and entry is not ignoreFileList:
            allFiles.append(fullPath)
    return allFiles


def main():
    global ignoreFileList
    ignoreFileList = [os.path.basename(__file__), 'key.key', 'enc.py', 'dec.py']

    if len(sys.argv) > 1:
        dir = sys.argv[1]
    else:
        dir = 'Archives'
sss
    files = listFiles(dir)
    key = Fernet.generate_key()

    with open('key.key','wb') as keyFile:
        keyFile.write(key)

    encryptFiles(key,files)

    if files:
        print('All files were encrypted')
        for file in files:
            print(f'{file}')
    else:
        print('No file was found to be encrypted')


if __name__ == '__main__':
    main()
