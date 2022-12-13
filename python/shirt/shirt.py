import sys
import os

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        root1, ext1 = os.path.splitext(sys.argv[1])
        root2, ext2 = os.path.splitext(sys.argv[2])

        if not check_ext(ext1):
            sys.exit("Invalid input")
        elif not check_ext(ext2):
            sys.exit("Invalid output")
        elif ext1 != ext2:
            sys.exit("Input and output have different extensions")

        shirt = Image.open("shirt.png")
        muppet = Image.open(sys.argv[1])

        cropped = ImageOps.fit(muppet, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

        cropped.paste(shirt, box=None, mask=shirt)

        cropped.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")



def check_ext(ext):
    ext = ext.lower()
    if ext == ".jpg" or ext == ".jpeg" or ext == ".png":
        return True
    else:
        return False

if __name__ == "__main__":
    main()