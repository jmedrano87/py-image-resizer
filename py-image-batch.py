import os
import argparse
import pathlib

ArgParser = argparse.ArgumentParser(
    description="Resize all JPG files in source directory."
)
ArgParser.add_argument("-c", "--coefficient", type=float, default=0.5)
ArgParser.add_argument("Source", type=pathlib.Path)
ArgParser.add_argument("Destination", type=pathlib.Path)
Args = ArgParser.parse_args()

print("Args passed", Args)

SourceDirectory = Args.Source
FileList = []

for item in os.listdir(SourceDirectory):
    if item.endswith((".jpg", ".jpeg")):
        FileList.append(item)

if len(FileList) > 0:
    print("Found jpg files to process:")
    for File in FileList:
        print(File)
    print(
        "New files will be resized to",
        Args.coefficient,
        "and placed in:",
        Args.Destination,
    )
else:
    print("Did not find any jpg files in " + SourceDirectory)
