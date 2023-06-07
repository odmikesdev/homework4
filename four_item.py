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

# - В седьмой строке выведите все символы в обратном порядке.
i = len(userString)
while i > 0:
    userString += userString[i-1]
    i -= 1
userString = userString[int((len(userString))/2):]
print(f'Inverted string: {userString}')
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
i = 1
while i <= len(userString):
    print(userString[-i], end=" ")
    i += 2
# - В девятой строке выведите длину данной строки.
print(f'\nLenth string: {len(userString)}')