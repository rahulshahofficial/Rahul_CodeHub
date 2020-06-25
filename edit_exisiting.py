import os
import shutil
from distutils.dir_util import copy_tree
originaldirectory = 'C:/Users/AnOrgasm/Desktop/TestFolder1/'
os.chdir(originaldirectory)
print(os.listdir())
sum = 0
def FolderSize(folder):
    global sum
    for item in os.listdir(folder):
        if os.path.isfile(item) is True:
            sum = sum + os.path.getsize(item)
    print(sum)
    for item in os.listdir(folder):
        if os.path.isdir(item) is True:
            print(folder + str(item))
            FolderSize((folder + str(item)))
    return sum

FolderSize('C:/Users/AnOrgasm/Desktop/TestFolder1/')

os.chdir('C:/Users/AnOrgasm/Desktop/TestFolder1/')
def copyfile(folder, location):
    for item in os.listdir(folder):
        if item not in os.listdir(location):
            if os.path.isfile(item) is True:
                print(folder)
                print(location)
                print("copying file")
                shutil.copy(item, location)
                # print("{:.2f}% copying done".format((Length2/Length1)*100))
                print(item)
def copyfolder(folder, location):
    for item in os.listdir(folder):
        if item not in os.listdir(location):
            if os.path.isdir(item) is True:
                print(folder)
                print("copying folder")
                os.mkdir(location + str(item))
                print((folder + str(item) + "/"))
                print((location + str(item) + "/"))
                copyfile((folder + str(item) + "/"), (location + str(item)+"/"))


copyfile(('C:/Users/AnOrgasm/Desktop/TestFolder1/'), ('C:/Users/AnOrgasm/Desktop/TestFolder2/'))
copyfolder(('C:/Users/AnOrgasm/Desktop/TestFolder1/'), ('C:/Users/AnOrgasm/Desktop/TestFolder2/'))


        # else:
        #     fromDirectory = 'C:/Users/AnOrgasm/Desktop/TestFolder1'
        #     toDirectory = 'C:/Users/AnOrgasm/Desktop/TestFolder2'
        #     print("copying directory")
        #     copy_tree(fromDirectory, toDirectory)
        #     Length2 += 1
        #     print("{:.2f}% copying done".format((Length2/Length1)*100))
        #     print(item)


