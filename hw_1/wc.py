import sys


def main():
    files = []
    if len(sys.argv) > 1:
        files = sys.argv[1:len(sys.argv)]

    total_words = 0
    total_lines = 0
    total_bytes = 0

    in_f = sys.stdin

    if len(files) > 1:
        for file in files:
            words = 0
            lines = 0
            bts = 0
            with open(file, "r") as in_f:
                for line in in_f:
                    lines += 1
                    words += len(line.split())
                    bts += len(line)

                    total_lines += lines
                    total_words += words
                    total_bytes += bts
                print(f"{lines:>6}{words:>6}{bts:>8}  {file}")
    else:
        in_f = open(files[0], "r") if files else sys.stdin
        for line in in_f:
            total_lines += 1
            total_words += len(line.split())
            total_bytes += len(line)

    print(f"{total_lines:>6}{total_words:>6}{total_bytes:>8}{'  total' if len(files) > 1 else ''}")


if __name__ == "__main__":
    main()
