#recorrer un directorio
import os
rootDir = os.getcwd()
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Directorio encontrado: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
