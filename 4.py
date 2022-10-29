# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def Read_file(file_name):
    with open(file_name, "r") as file:
        result = file.read()
    return result

def Write_file(file_name, data):
    with open(file_name, "w") as file:
        result = file.write(str(data))
    return result

def RLE_coding(data):
    count = 1
    result = ''
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result = result + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data) - 2] != data[-1]):
        result = result + str(count) + data[-1]
    return result

def RLE_decoding(data):
    number = ''
    result = ''
    for i in range(len(data)):
        if not data[i].isalpha():
            number += data[i]
        else:
            result = result + data[i] * int(number)
            number = ''
    return result

text = Read_file('Text.txt')
print(f"Данные после сжатия: {RLE_coding(text)}")
print(f"Данные после дешифровки: {RLE_decoding(RLE_coding(text))}")
Write_file('Output.txt', RLE_coding(text))