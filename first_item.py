#1. Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба количества на экран. (использовать цикл)

textString = input('Please enter a string: ')
stringChar = 0
numberChar = 0
symbolChar = 0
for i in textString:
    if i.isdigit():
        numberChar += 1
    elif i.isalpha():
        stringChar += 1
    else:
        symbolChar += 1
#Использую 3 варианта форматирования строк, просто чтобы потренироваться
print(f'F STRING \n\
Lenth string is {len(textString)}\nNumber of digits per string is {numberChar}\n\
Number of al per letter is {stringChar}\n\
Number of symbol per string is {symbolChar}')

print('FORMAT STRING \n\
Lenth string is {3}\nNumber of digits per string is {0}\n\
Number of al per letter is {2}\nNumber of symbol per string is {1}\
'.format(numberChar, symbolChar, stringChar, len(textString)))

print('S STRING\n\
Lenth string is %d Number of digits per string is %d \n\
Number of al per letter is %d \nNumber of symbol per string is %d\
' %(len(textString), numberChar, stringChar, symbolChar))