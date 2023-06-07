# Дана строка. (сделать срезы)
# - Сначала выведите третий символ этой строки.
# - Во второй строке выведите предпоследний символ этой строки.
# - В третьей строке выведите первые пять символов этой строки.
# - В четвертой строке выведите всю строку, кроме последних двух символов.
# - В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# - В седьмой строке выведите все символы в обратном порядке.
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# - В девятой строке выведите длину данной строки.
# try:
#     userString = input('Please enter a string of at least 10 characters:')
#     if len(userString) < 10:
#         raise Exception
# except Exception:
#     print('The string must have more than 10 characters.')
userString = 'qweasdzxcr'
#- Сначала выведите третий символ этой строки.
print(f'The 3 character of the string: {userString[2]}')
#- Во второй строке выведите предпоследний символ этой строки.
print(f'The penultimate character of this string: {userString[-2]}')
#- В третьей строке выведите первые пять символов этой строки.
print(f'The first five characters of this string: {userString[:5]}')
#- В четвертой строке выведите всю строку, кроме последних двух символов.
print(f'Print the entire line except for the last two characters: {userString[:-2]}')
# - В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
i = 0
evenString = ''
oddString = ''
while i < len(userString)-1:
    if i % 2 == 0:
        evenString = evenString + userString[i]
    else:
        oddString = oddString + userString[i]
    i += 1
print(f'Print all characters with even indices (assuming that indexing starts from 0, so the characters are printed starting from the first one): {evenString}')
print(f'Print all characters with odd indices: {oddString}')