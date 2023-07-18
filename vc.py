# Name: Shivangi Awasthi
# Access ID: HI3586
# Homework 1 question 1
# with CGI for 5 extra points

import PySimpleGUI as sg

text = ''
password = ''
message = ''


def keysize(msg, ky):
    global message
    message = msg.upper()
    key = ky.upper()
    keyMap = ''
    j = 0
    for i in range(len(message)):
        if (j < len(key)):
            keyMap += key[j]
            j += 1
        else:
            j = 0
            keyMap += key[j]
            j += 1

    global text
    text = message
    global password
    password = keyMap


def VigenereTable():
    array = [['' for r in range(27)] for c in range(27)]
    for i in range(27):
        for j in range(27):
            temp = 0
            if (i + j) == 26:
                temp = 32
                array[i][j] = temp
                continue
            if (i + 65) + j > 91:
                temp = ((i + 65) + j) - 27
                array[i][j] = temp
            else:
                temp = (i + 65) + j
                array[i][j] = temp
    for m in range(27):
        for n in range(27):
            print(chr(array[m][n]) if array[m][n] != 32 else '_', end=' ')
        print()
    return array


def encryption(text, password):
    array = VigenereTable()
    encryptedtext = ''
    for i in range(len(message)):
        x, y = 0, 0
        if ord(text[i]) == 32 and ord(password[i]) == 32:
            x = 26
            y = 26
        elif ord(text[i]) == 32:
            x = 26
            y = ord(password[i]) - 65
        elif ord(password[i]) == 32:
            x = ord(text[i]) - 65
            y = 26
        else:
            x = ord(text[i]) - 65
            y = ord(password[i]) - 65

        encryptedtext += chr(array[x][y])

    return encryptedtext


def count(key, text):
    cnt = 0
    result = ''
    for i in range(27):
        if (key == 32):
            key = 91
        if (key + i > 91):
            result += chr(key + (i - 27))
        elif ((key + i) == 91):
            result += ' '
        else:
            result += chr(key + i)

    for i in range(len(result)):
        if (ord(result[i]) == text):
            break
        else:
            cnt += 1

    return cnt


def decryption(text, password):
    decryptedText = ''
    for i in range(len(text)):

        temp = count(ord(password[i]), ord(text[i]))

        if (temp == 26):
            decryptedText += ' '
        else:
            decryptedText += chr(65 + temp)

    return decryptedText


def main():
    sg.theme('BlueMono')

    layout = [
        [sg.Text('Plain Text'), sg.InputText(key='plainText'), ],
        [sg.Text('Cypher Text'), sg.InputText(key='cipherText'), ],
        [sg.Text('Password'), sg.InputText(key='password'), ],
        [sg.Button('encrypt'), sg.Button('decrypt')],
        [sg.Text('Output:')],
        [sg.Multiline(size=(55, 3), disabled=True, key='output')],
        [sg.Text('Error:')],
        [sg.Multiline(size=(55, 3), disabled=True, key='error')]
    ]

    window = sg.Window('Vigenere Cipher', layout).Finalize()
    while True:
        event, values = window.read()

        if event == 'encrypt' and values['plainText'] and values['password']:

            keysize(values['plainText'], values['password'])
            encrypted = encryption(text, password)
            encrypted = encrypted.replace(' ', '_')
            window['output'].update(encrypted)
            window['error'].update('')

        elif event == 'decrypt' and values['cipherText'] and values['password']:

            cipherText = values['cipherText'].replace('_', ' ')
            keysize(cipherText, values['password'])
            decypted = decryption(text, password)
            window['output'].update(decypted)
            window['error'].update('')

        else:  # either no cipher text in case of decryption and no plain text for encryption is available:
            window['error'].update('Invalid Text. Please Enter Valid Text.')
            window['output'].update('')


if __name__ == '__main__':
    main()
