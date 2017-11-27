# _*_ coding:UTF-8 _*_


def change(c, i):
    c = c.lower()
    num = ord(c)
    if num >= 97 and num <= 122:
        num = 97 + ((num - 97) + i) % 26
    return chr(num)


def en():
    caesarinput = input('input:\n')
    key = input('key(int):\n')
    caesarinput = str(caesarinput)
    key = int(key)
    output = ''
    for s in caesarinput:
        output += change(s, key)

    print(output)


def brute():
    caesarinput = input('input:\n')
    caesarinput = str(caesarinput)
    for i in range(26):
        output = ''
        i=int(i)+1
        for s in caesarinput:
            output += change(s, i)
        print(output)
