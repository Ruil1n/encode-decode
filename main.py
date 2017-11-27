# _*_ coding:UTF-8 _*_
from modules import b64
from modules import url

def start():
    print('''
1.base64 Encode
2.base64 Decode
3.URL    Encode
4.URL    Decode
    ''')
    choice = input('Select：')
    return int(choice)

def main():
    try:
        while True:
            main_choice = start()
            if main_choice == 1:
                b64.en()
            elif main_choice == 2:
                b64.de()
            elif main_choice == 3:
                url.en()
            elif main_choice == 4:
                url.de()

            elif main_choice == 0:
                exit(0)

            again = input('\nContinue？(0/1)')
            if again == '0':
                break
    except Exception as e:
        print('ERROR:',e)

if __name__ == '__main__':
    main()