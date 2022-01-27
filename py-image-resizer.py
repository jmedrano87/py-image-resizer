import argparse
from pathlib import Path
import PIL
from PIL import Image

ArgParser = argparse.ArgumentParser(
    description="Resize all images with extension type in source directory and save "
    + "output to destination directory. Default type is jpg."
)
ArgParser.add_argument("-c", "--coefficient", type=float, default=0.5)
ArgParser.add_argument("-t", "--type", type=str, default="jpg")
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
    if item.suffix == "." + Args.type:
        dest = Args.Destination.joinpath(item.name)
        if Args.verbose:
            print("Resizing", item.name, "by", Args.coefficient, "and saving to", dest)
        ResizeImage(item, dest, Args.coefficient)
