'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
'''

def alphabet_position(text):
    #d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14 'o':15,
    #'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    #generate dict of letters mapped to pos in alphabet
    d = {chr(char+97): char+1 for char in range(26)}
    text = text.lower()
    s = ''
    for i in range(len(text)):
        if text[i] in d:
            s+= str(d[text[i]])
            s+= ' '
        
    return s[:-1]
