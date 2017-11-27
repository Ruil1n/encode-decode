# _*_ coding:UTF-8 _*_
import urllib.parse

def en():
    URLinput = input('input:\n')
    print(''.join('%{:02X}'.format(x) for x in URLinput.encode()))

def de():
    URLinput = input('input:\n')
    print(urllib.parse.unquote(URLinput))