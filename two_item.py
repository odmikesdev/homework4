# Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке встречается искомый символ. Полученное число выведите на экран. 

#First Variant
userString = input('Please enter a string for find: ')
userSymbol = input('Please enter a finding symbol: ')
searchNumber = userString.count(userSymbol)
print(f'The fragment was found once: {searchNumber}')

#Two Varian
#Вынес вычисления за цикл, чтобы при каждой итерации их не считать
#Поиск подстроки в строке
print('variant 2')
userSymbolFirst = userSymbol[0]
items = len(userSymbol)
iteration = 0
result = 0
for i in userString:
    if i == userSymbolFirst and userString[iteration:iteration+items] == userSymbol:
        #Данный пункт использовал, так как в противном случае вхождение 55 в 555 посчитает за 2, что не верно
        userString = userString[iteration+items-1:]
        result += 1
    iteration += 1

print('The fragment was found once: {}'.format(result))

