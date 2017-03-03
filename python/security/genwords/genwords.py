import string
import sys
import itertools


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
whitespace = ' '
digit = string.digits


def genwords(alphabet, wordsize):
    tmp = list(itertools.product(alphabet, alphabet, repeat=wordsize))

    match = 'daniel'
    count = 0
    for i in tmp:
        word = ''.join(i)
        print(word)
#        if match == word:
#            print('matched at', count, 'tries.')
#            sys.exit(0)
        count = count + 1


genwords(lowercase, 3)
