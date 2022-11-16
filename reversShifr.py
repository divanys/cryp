mess = input('Введите сообщение: ')

translated: str = ''
i = len(mess) - 1
while i >= 0:
    translated += mess[i]
    i -= 1

print('Ваш шифр: ', translated)