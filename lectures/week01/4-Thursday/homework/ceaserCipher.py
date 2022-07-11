ceaser_string = "lbh zhfg hayrnea jung lbh unir yrnearq"

cipher_code = 'nopqrstuvwxyzabcdefghijklm'

StringList = list(ceaser_string)

for i in range(len(StringList)):
    if StringList[i] == 'a':
        StringList[i] = 'n'
    elif StringList[i] == 'b':
        StringList[i] = 'o'
    elif StringList[i] == 'c':
        StringList[i] = 'p'
    elif StringList[i] == 'd':
        StringList[i] = 'q'
    elif StringList[i] == 'e':
        StringList[i] = 'r'
    elif StringList[i] == 'f':
        StringList[i] = 's'
    elif StringList[i] == 'g':
        StringList[i] = 't'
    elif StringList[i] == 'h':
        StringList[i] = 'u'
    elif StringList[i] == 'i':
        StringList[i] = 'v'
    elif StringList[i] == 'j':
        StringList[i] = 'w'
    elif StringList[i] == 'k':
        StringList[i] = 'x'
    elif StringList[i] == 'l':
        StringList[i] = 'y'
    elif StringList[i] == 'm':
        StringList[i] = 'z'
    elif StringList[i] == 'n':
        StringList[i] = 'a'
    elif StringList[i] == 'o':
        StringList[i] = 'b'
    elif StringList[i] == 'p':
        StringList[i] = 'c'
    elif StringList[i] == 'q':
        StringList[i] = 'd'
    elif StringList[i] == 'r':
        StringList[i] = 'e'
    elif StringList[i] == 's':
        StringList[i] = 'f'
    elif StringList[i] == 't':
        StringList[i] = 'g'
    elif StringList[i] == 'u':
        StringList[i] = 'h'
    elif StringList[i] == 'v':
        StringList[i] = 'i'
    elif StringList[i] == 'w':
        StringList[i] = 'j'
    elif StringList[i] == 'x':
        StringList[i] = 'k'
    elif StringList[i] == 'y':
        StringList[i] = 'l'
    elif StringList[i] == 'z':
        StringList[i] = 'm'
            
ceaser_string = ''.join(StringList)

print(ceaser_string)
