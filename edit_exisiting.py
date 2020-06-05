import os
import shutil
from distutils.dir_util import copy_tree
print(os.getcwd())
os.chdir('C:/Users/AnOrgasm/Desktop/TestFolder1')
print(os.getcwd())
print(os.listdir())
Length1 = len(os.listdir('C:/Users/AnOrgasm/Desktop/TestFolder1'))
Length2 = len(os.listdir('C:/Users/AnOrgasm/Desktop/TestFolder2'))

for item in os.listdir():
    if item not in os.listdir('C:/Users/AnOrgasm/Desktop/TestFolder2'):
        if os.path.isfile(item) is True:
            shutil.copy(item, 'C:/Users/AnOrgasm/Desktop/TestFolder2')
            Length2 += 1
            print("{}% copying done".format(Length2/Length1))
            print(item)
        else:
            fromDirectory = 'C:/Users/AnOrgasm/Desktop/TestFolder1'
            toDirectory = 'C:/Users/AnOrgasm/Desktop/TestFolder2'
            copy_tree(fromDirectory, toDirectory)
            Length2 += 1
            print("{}% copying done".format(Length2/Length1))
            print(item)


