import sys


# +++your code here+++
# Define print_words(filename) function.
###
def print_words(filename):
    f = open(filename, 'r')
    str_file = f.read()
    word_list = str_file.split()
    words_dict = {}
    for word in word_list:
        if not word.isalpha():
            continue
        elif word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    for item in sorted(words_dict.keys()):
        print item, words_dict[item]
    print ''

    word = raw_input("Enter a word to find: ")
    if word in words_dict:
        print "The word '{}' was found {} time(s)" .format(word, str(words_dict[word]))
    else:
        print "The word '{}' was not found." .format(word)


# This basic command line argument parsing code is provided and
# calls the print_words() function which you must define.
def main():
    if len(sys.argv) != 2:
        print 'usage: ./word_count.py file'
        sys.exit(1)

    filename = sys.argv[1]
    print_words(filename)


if __name__ == '__main__':
    main()