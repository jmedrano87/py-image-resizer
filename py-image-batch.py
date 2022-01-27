import argparse
from pathlib import Path
from PIL import Image

ArgParser = argparse.ArgumentParser(
    description="Resize all JPG files in source directory."
)
ArgParser.add_argument("-c", "--coefficient", type=float, default=0.5)
ArgParser.add_argument("Source", type=Path)
ArgParser.add_argument("Destination", type=Path)
Args = ArgParser.parse_args()


def ResizeImage(originalFile, newFile, multiplier):
    img = Image.open(originalFile)
    x = int(img.size[0] * multiplier)
    y = int(img.size[1] * multiplier)
    NewImg = img.resize((x, y), resample=Image.LANCZOS)
    NewImg.save(newFile)


SourceDirectory = Args.Source

for item in Path(SourceDirectory).iterdir():
    if item.match("*.jpg") or item.match("*.jpeg"):
        dest = Args.Destination.joinpath(item.name)
        print("Resizing", item.name, "by", Args.coefficient, "and saving to", dest)
        ResizeImage(item, dest, Args.coefficient)
