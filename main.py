import sys
from pyigdiff import pyigdiff

def main():
    if len(sys.argv) == 1:
        raise ValueError('Zip file was not provided')
    report = pyigdiff(sys.argv[1])
    print(report) 


if __name__ == "__main__":
    main()
