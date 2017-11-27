# _*_ coding:UTF-8 _*_
from pycipher import Caesar


def en():
    caesarinput = input('input:\n')
    key = input('key(int):\n')
    output = Caesar(int(key)).encipher(caesarinput, keep_punct=True)
    print(output)


def de():
    caesarinput = input('input:\n')
    key = input('key(int):\n')
    output = Caesar(int(key)).decipher(caesarinput, keep_punct=True)
    print(output)


def brute():
    caesarinput = input('input:\n')
    for i in range(26):
        print('%s:' % i, end='')
        output = Caesar(int(i)).encipher(caesarinput, keep_punct=True)
        print(output)
