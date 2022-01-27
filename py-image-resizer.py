import argparse
from pathlib import Path
import PIL
from PIL import Image

ArgParser = argparse.ArgumentParser(
    description="Resize all JPG files in source directory and save to destination directory."
)
ArgParser.add_argument("-c", "--coefficient", type=float, default=0.5)
ArgParser.add_argument("-v", "--verbose", action="store_true")
ArgParser.add_argument("Source", type=Path)
ArgParser.add_argument("Destination", type=Path)
Args = ArgParser.parse_args()


def ResizeImage(originalFile, newFile, multiplier):
    try:
        img = Image.open(originalFile)
    except PIL.UnidentifiedImageError as e:
        print("Error when trying to open file:", originalFile)
        print(e)
    else:
        x = int(img.size[0] * multiplier)
        y = int(img.size[1] * multiplier)
        NewImg = img.resize((x, y), resample=Image.LANCZOS)
        try:
            NewImg.save(newFile)
        except OSError as e:
            print("Error when attempting to write file:", newFile)
            print(e)
        finally:
            img.close()


for item in Path(Args.Source).iterdir():
    if item.match("*.jpg") or item.match("*.jpeg"):
        dest = Args.Destination.joinpath(item.name)
        if Args.verbose:
            print("Resizing", item.name, "by", Args.coefficient, "and saving to", dest)
        ResizeImage(item, dest, Args.coefficient)
