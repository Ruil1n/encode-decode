# _*_ coding:UTF-8 _*_
import base64

def en():
    b64input = input('input:\n')
    output = base64.b64encode(b64input.encode())
    print(output.decode())

def de():
    b64input = input('input:\n')
    output = base64.b64decode(b64input.encode())
    print(output.decode())