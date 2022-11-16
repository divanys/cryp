mess = input('Enter message: ')
key = int(input('Key: '))


def encryptMess() -> object:
    key1 = key
    mess1 = mess
    cipherTxt = [''] * key1  # Каждая строка в списке ciphertext представляет столбец таблицы
    # Отобразить зашифрованную строку, хранящуюся в переменной
    # ciphertext, вставив после нее символ 1 на случай, если
    # в конце зашифрованного сообщения имеют с я пробелы

    for column in range(key1):  # Цикл по всем столбцам в списке ciphertext
        currentIndex = column

        while currentIndex < len(mess1):  # Цикл, пока значение currentindex не превысит длину сообщения
            # Поместить в конец текущего столбца в списке ciphertext
            # символ сообщения с индексом currentindex
            cipherTxt[column] += mess1[currentIndex]
            currentIndex += key1
    ret = ''.join(cipherTxt) + '|'
    return ret


print(encryptMess())
