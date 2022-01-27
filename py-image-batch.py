import argparse
from pathlib import Path

ArgParser = argparse.ArgumentParser(
    description="Resize all JPG files in source directory."
)
ArgParser.add_argument("-c", "--coefficient", type=float, default=0.5)
ArgParser.add_argument("Source", type=Path)
ArgParser.add_argument("Destination", type=Path)
Args = ArgParser.parse_args()

print("Args passed", Args)

SourceDirectory = Args.Source
FileList = []

for item in Path(SourceDirectory).iterdir():
    if item.match("*.jpg") or item.match("*.jpeg"):
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
