def read_file(fpath):
    BLOCK_SIZE = 1
    with open(fpath, 'r') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


if __name__ == '__main__':
    readFile = read_file("D:\\test.txt")
    for i in readFile:
        print(i)
