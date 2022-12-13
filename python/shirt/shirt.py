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

        if not check_ext(ext1) and not check_ext(ext2):
            sys.exit("")



def check_ext(ext):
    ext = ext.lower()
    if ext == ".jpg" or ext == ".jpeg" or ext == ".png":
        return True
    else:
        return False

if __name__ == "__main__":
    main()