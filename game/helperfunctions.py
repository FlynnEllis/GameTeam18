from os import system 
import msvcrt

def print_chat_options(options,cursor):
    for index in range(len(options)):
        if index == cursor:
            print('{ '+ options[index] +' }')
        else:
            print('  ' + options[index])
 
def navigate_chat_options(options,cursor):
    system('cls')
    print_chat_options(options,cursor)
    key = getkey()
    while 1:
        if key == 'up':
            return navigate_chat_options(options,cursor -1)
        elif key == 'down':
            return navigate_chat_options(options,cursor +1)
        else:
            return cursor
        key = getkey()
 
 
 
def getkey():
    while True:
        if msvcrt.kbhit():        
            char = msvcrt.getch()

            if char in [b'\xe0']:
                char = msvcrt.getch()
                return {b'H': 'up', b'P': 'down'}[char]
            else:
            	return char


 

def anykey():
    print('Press any key to continue')
    while True:
        if msvcrt.kbhit():
            return