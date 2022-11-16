mess = input('Введите сообщение: ')

key = int(input('Введите размер ключа: '))

mode = input('Зашифровываем или дешифровываем?: ')

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

translated = ''

for _ in mess:
    if _ in symbols:
        symbolIndex = symbols.find(_)
        if mode == 'зашифровываем':
            translatedIndex = symbolIndex + key
        elif mode == 'дешифровываем':
            translatedIndex = symbolIndex - key
        else:
            translatedIndex = symbolIndex + key

        if translatedIndex >= len(symbols):
            translatedIndex -= len(symbols)
        elif translatedIndex < 0:
            translatedIndex += len(symbols)

        translated += symbols[translatedIndex]

    else:
        translated += _

print('Зашифровано!\n', translated)
