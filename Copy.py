import os
import shutil


def FolderSize(source):
    sum = 0
    list = os.listdir(source)
    for item in list:
        path = os.path.join(source, item)
        if os.path.isfile(path):
            sum = sum + os.path.getsize(path)
        if os.path.isdir(path):
            sum = sum + FolderSize(path)
    return sum


print(FolderSize('C:/Users/AnOrgasm/Desktop/TestFolder1'))
print(FolderSize('C:/Users/AnOrgasm/Desktop/TestFolder2'))

Total1 = FolderSize('C:/Users/AnOrgasm/Desktop/TestFolder1')
Total2 = FolderSize('C:/Users/AnOrgasm/Desktop/TestFolder2')


def CopyFolder(source, destination):
    global Total1
    global Total2
    list = os.listdir(source)
    for item in list:
        path = os.path.join(source, item)
        if item not in os.listdir(destination):
            if os.path.isfile(path) is True:
                print("Copying file: ")
                shutil.copy(path, destination)
                Total2 = Total2 + os.path.getsize(path)
                print("Copying status: {:.2f}".format((Total2 / Total1) * 100))
                progress = ((Total2 / Total1) * 100)
                no_of_bars = int(progress/5)
                print((bar)*(no_of_bars) + "{:.2f}".format(progress))
            elif os.path.isdir(path) is True:
                print("Copying folder: ")
                new_directory = os.path.join(destination, item)
                os.mkdir(new_directory)
                CopyFolder(path, new_directory)


CopyFolder('C:/Users/AnOrgasm/Desktop/TestFolder1', 'C:/Users/AnOrgasm/Desktop/TestFolder2')
