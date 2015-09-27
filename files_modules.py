import sys


def writeToFile(filename):
    l = range(100)
    with open(filename, 'w') as f:
        for num in l:
            f.write(str(num) + '\n')


def readFromFile(filename):
    with open(filename, 'r') as f:
        results = []
        for line in f:
            results.append(int(line.strip()))
        print sum(results)


def main():
    if len(sys.argv) != 3:
        print 'usage: ./fileTest.py { --read | --write } filename'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == "--read":
        readFromFile(filename)
    elif option == "--write":
        writeToFile(filename)
    else:
        print "Unknown option: " + option
        sys.exit(1)


if __name__ == '__main__':
    main()