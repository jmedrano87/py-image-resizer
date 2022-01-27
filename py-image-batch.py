import os

SourceDirectory = os.getcwd()
FileList = []

for item in os.listdir(SourceDirectory):
    if item.endswith((".jpg", ".jpeg")):
        FileList.append(item)

if len(FileList) > 0:
    print("Found jpg files to process:")
    for File in FileList:
        print(File)
else:
    print("Did not find any jpg files in " + SourceDirectory)
