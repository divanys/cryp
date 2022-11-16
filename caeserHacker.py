mess = input('Enter message: ')
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for _ in range(len(symbols)):
    translated = ''
    for i in mess:
        if i in symbols:
            symbolIndex = symbols.find(i)
            translatedIndex = symbolIndex - _

            if translatedIndex < 0:
                translatedIndex += len(symbols)

            translated += symbols[translatedIndex]

        else:
            translated += i

    print('Key %s: %s' % (_, translated))
