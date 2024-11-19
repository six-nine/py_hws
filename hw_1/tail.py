import sys


def main():
    files = []
    if len(sys.argv) > 1:
        files = sys.argv[1:len(sys.argv)]

    if files:
        for file in files:
            print(f"===> {file} <===")
            with open(file, "r") as in_f:
                print("".join(in_f.readlines()[-10:]))
    else:
        print("".join(sys.stdin.readlines()[-17:]))


if __name__ == "__main__":
    main()
