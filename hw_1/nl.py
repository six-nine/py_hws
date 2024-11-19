import sys


def main():
    file_name = None
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    in_f = open(file_name) if file_name else sys.stdin

    line_num = 0
    for line in in_f:
        line_num += 1
        print(f"{line_num:>6}  {line}", end="")

    if in_f is not sys.stdin:
        in_f.close()


if __name__ == "__main__":
    main()
