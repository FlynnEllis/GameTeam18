from os import system 
import msvcrt, random, time

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
    print('\nPress any key to continue')
    while True:
        if msvcrt.kbhit():
            return

def psychedelic():
    for i in range(0,8):

        colours_list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        for i in colours_list: 
            time.sleep(0.05)
            system('color 0' + i)




def shuffle_string(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)

def garble_word(word):
    # No operation needed on sufficiently small words
    # (Also, main algorithm requires word length >= 2)
    if len(word) <= 3:
        return word

    # Split word into first & last letter, and middle letters
    first, mid, last = word[0], word[1:-1], word[-1]

    return first + shuffle_string(mid) + last

def output(sentence,sobriety):
    if sobriety <= 0:
        words = sentence.split(' ')
        print (' '.join(map(garble_word, words)))
    else:
        print(sentence)