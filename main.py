import requests
import pyfiglet
from termcolor import colored

result = print(colored(pyfiglet.figlet_format("Juicy v1.0", font="doh", width=200 ),'green'))
juicyWord = {'password', 'admin', 'canonical'}

def scanDomains():
    file = input("Give me a subdomains list or type 'exit' to quit: ")
    try:
        with open(file) as f:
            lines = f.readlines()
            print(" ")
            print(f'{"Subdomain":<25}{"Content Type":<30}{"Content Encoding":<20}Is Juicy')
            print('─' * 84)

            for line in lines:
                addr = line.rstrip()
                r = requests.get('https://' + addr)
                status = r.status_code

                if status == 200:
                    isOnce = True
                    cType = r.headers['Content-Type']
                    tText = r.text
                    cEncoding = r.headers['Content-Encoding']

                    for word in juicyWord:
                        if word in tText and isOnce:
                            print(f'{addr:<25}{cType:<30}{cEncoding:20}YES')
                            isOnce = False
                        elif isOnce:
                            print(f'{addr:<25}{cType:<30}{cEncoding:20}NO')
                            isOnce = False
        print('#' * 84)
    except FileNotFoundError:
        print("File not found. Please try again or exit")


def printJuicy():
    i = 0
    for item in juicyWord:
        print(f'{str(i):<5}{item}')
        i = i+1
    print('#' * 84)

while True:

    print(" ")
    print("Select an option or type 'exit' to quit: ")
    caption = colored("1.   Scan subdomains\n2.   See juicy",'red', attrs=['blink'])
    print(caption)

    choice = input("Select: ")

    if choice == '1':
        scanDomains()
    elif choice == '2':
        printJuicy()
        #print(juicyWord)
    elif choice == 'exit':
        quit()