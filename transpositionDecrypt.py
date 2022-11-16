import math

mess = input('Enter message: ')
key = int(input('Key: '))


def decMess() -> object:
    mess1 = mess
    key1 = key
    numOfColumns = int(math.ceil(len(mess1) / key1))
    numOfRows = key1
    numOfShadeBoxes = (numOfColumns * numOfRows) - len(mess1)

    plainTxt = [''] * numOfColumns

    column = 0
    row = 0

    for _ in mess1:
        plainTxt[column] += _
        column += 1

        if (column == numOfColumns) or (column == (numOfColumns - 1) and (row >= (numOfRows - numOfShadeBoxes))):
            column = 0
            row += 1
    ret = ''.join(plainTxt) + '|'
    return ret


print(decMess())
