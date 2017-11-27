# _*_ coding:UTF-8 _*_
from modules import base
from modules import url
from modules import caesar

def start():
    print('''
1. base64 Encode
2. base64 Decode
3. base32 Encode
4. base32 Decode
5. base16 Encode
6. base16 Decode
7. URL    Encode
8. URL    Decode
9. Caesar    Encode
10.Caesar    Brute_Decode
    ''')
    choice = input('Select：')
    return int(choice)

def main():
    try:
        while True:
            main_choice = start()
            if main_choice == 1:
                base.en64()
            elif main_choice == 2:
                base.de64()
            elif main_choice == 3:
                base.en32()
            elif main_choice == 4:
                base.de32()
            elif main_choice == 5:
                base.en16()
            elif main_choice == 6:
                base.de16()
            elif main_choice == 7:
                url.en()
            elif main_choice == 8:
                url.de()
            elif main_choice == 9:
                caesar.en()
            elif main_choice == 10:
                caesar.brute()
                
            elif main_choice == 0:
                exit(0)

            again = input('\nContinue？(1/0)')
            if again == '0':
                break
    except Exception as e:
        print('ERROR:',e)

if __name__ == '__main__':
    main()