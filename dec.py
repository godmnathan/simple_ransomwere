from cryptography.fernet import Fernet
import os
import sys

dirDefault = 'Archives'
ignoreFileList = [os.path.basename(__file__), 'key.key', 'enc.py', 'dec.py']
keyPath = 'key.key'

def listFiles(baseDir):
    allFiles = []
    for entry in os.listdir(baseDir):
        fullPath = os.path.abspath(os.path.join(baseDir, entry))
        if os.path.isdir(fullPath):
            allFiles += listFiles(fullPath)
        elif os.path.isfile(fullPath) and entry is not ignoreFileList:
            allFiles.append(fullPath)
    return allFiles

def readKey(keyPath):
    if not os.path.isfile(keyPath):
        print(f'Cryptography key not found: {keyPath}')
        sys.exit(1)
    with open(keyPath,'rb') as keyFile:
        key = keyFile.read()
    return key

def decryptFiles(key,allFiles):
    filesToDecrypt = []

    for file in allFiles:
        try:
            with open(file,'rb') as encryptedFile:
                fileContent = encryptedFile.read()
            decryptedFileContent = Fernet(key).decrypt(fileContent)
            with open(file,'wb') as decryptedFile:
                decryptedFile.write(decryptedFileContent)
            filesToDecrypt.append(file)
        except Exception as e:
            print(f'Error when decrypting file: {e}')
    return filesToDecrypt

def main():
    dir = sys.argv[1] if len(sys.argv) > 1 else dirDefault
    archives = listFiles(dir)

    key = readKey(keyPath)

    decryptedFiles = decryptFiles(key,archives)

    print(f'{decryptedFiles}')

if __name__ == '__main__':
    main()