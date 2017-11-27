# _*_ coding:UTF-8 _*_
import base64

def en64():
    b64input = input('input:\n')
    output = base64.b64encode(b64input.encode())
    print(output.decode())

def de64():
    b64input = input('input:\n')
    output = base64.b64decode(b64input.encode())
    print(output.decode())

def en32():
    b32input = input('input:\n')
    output = base64.b64encode(b32input.encode())
    print(output.decode())

def de32():
    b32input = input('input:\n')
    output = base64.b64decode(b32input.encode())
    print(output.decode())

def en16():
    b16input = input('input:\n')
    output = base64.b16encode(b16input.encode())
    print(output.decode())

def de16():
    b16input = input('input:\n')
    output = base64.b16decode(b16input.encode())
    print(output.decode())