"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных
"""

dict = {1: ["Иванов", "Иван", "89217335689"], 2: ["Долгов", "Андрей", "89652334567"]}

def findElement(dict):
    element = input("Введите значение для поиска:""\n")
    for i in dict:    
        for j in range(len(dict[i])):
            if element in dict[i][j]:
                print(dict[i])

def addStr(dict):
    save = list(input("Введите фамилию, имя, телефон через пробел:""\n").split(" "))
    s = 1
    while True:
        if s in dict:
            s+=1
        else:
            dict[s] = save
            break

def printPhonebook(dict):
    print(dict)

def printSurnames(dict):
    for i in dict:
        print(dict[i][0])

def changeStr(dict):
    number1 = int(input('Введите номер строки для изменения:''\n'))
    print("Что именно будем менять?""\n"
          "1 - фамилия""\n"
          "2 - имя""\n"
          "3 - телефон""\n"
          "4 - всю строчку целиком")
    number2 = int(input()) - 1
    if number2 == 3:
        text = input("На что будем менять?""\n")
        dict[number1] = list(text.split(" "))
    else:
        text = input("На что будем менять?""\n")
        dict[number1][number2] = text

def deleteStr(dict):
    number = int(input("Введите номер строки для удаления:""\n"))
    del dict[number]

def findOrDeleteElement(dict):
    element = input("Введите значение для поиска:""\n")
    for i in dict:    
        for j in range(len(dict[i])):
            if element in dict[i][j]:
                print("Найдена запись:")
                print(dict[i])
                number = int(input("1 - изменяем элемент записи""\n"
                                   "2 - удаляем элемент записи""\n"
                                   "3 - оставляем как есть""\n"))
                if number == 1:
                    dict[i][j] = input("Введите новое значение:""\n")
                if number == 2:
                    del dict[i][j]
                    break
                if number == 3:
                    pass
            

    
    
print("Введите номер команды:" "\n"
"1 - вывести телефонную книгу" "\n"
"2 - вывести фамилии" "\n"
"3 - добавить запись" "\n"
"4 - найти запись по элементу" "\n"
"5 - изменить запись по номеру строки" "\n"
"6 - удалить запись по номеру строки""\n"
"7 - поиск по элементу с последующим изменением или удалением данных")

with open('phoneBook.txt', 'w', encoding = 'utf-8') as file:
    for i in dict:
        file.write(f'{dict[i][0]} {dict[i][1]} {dict[i][2]}\n')
collect = {}
collectKey = 1
with open('phoneBook.txt', 'r', encoding = 'utf-8') as file:
    for i in file:
        i = i.replace('\n', '')
        collect[collectKey] = list(i.split(" "))
        collectKey+=1

menuNumber = input()
if menuNumber == "1":
    printPhonebook(collect)
if menuNumber == "2":
    printSurnames(collect)
if menuNumber == "3":
    addStr(collect)
if menuNumber == "4":
    findElement(collect)
if menuNumber == "5":
    changeStr(collect)
if menuNumber == "6":
    deleteStr(collect)
if menuNumber == "7":
    findOrDeleteElement(collect)

with open('phoneBook.txt', 'w', encoding = 'utf-8') as file: 
    for i in collect:

       # file.write(f'{collect[i][0]} {collect[i][1]} {collect[i][2]}\n')  
        file.write(f'{" ".join(collect[i])}\n')  

print(collect)




