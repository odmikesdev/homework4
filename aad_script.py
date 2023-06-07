loreIpsum = "lorem ipsum is simply dummy 999999 text of the printing and typesetting industry! lorem ipsum has been the\
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type\
and scrambled it to make a type specimen book. it has survived not only five centuries, but also the\
leap into electronic typesetting, remaining essentially unchanged. it was 99999 popularised in the 1960s with the\
release of letraset sheets containing lorem ipsum passages, and more recently with desktop publishing software\
like aldus pagemaker including versions of lorem ipsum! lorem ipsum is simply dummy 999999 text of the printing and typesetting industry. lorem ipsum has been the\
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type\
and scrambled it to make a type specimen book. it has survived not only five centuries, but also the\
leap into electronic typesetting, remaining essentially unchanged. it was 99999 popularised in the 1960s with the\
release of letraset sheets containing lorem ipsum passages, and more recently with desktop publishing software\
like aldus pagemaker including versions of lorem ipsum."

# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в тексте.
loreIpsum = loreIpsum.capitalize()
countSymbols = 0
countChars = 0
countDigit = 0
exclamationPoints = 0
i = 1
countString = len(loreIpsum) - 1

while i < countString:
    if (loreIpsum[i] == '.' or loreIpsum[i] == '!' or loreIpsum[i] == '?') and i+1 < countString and loreIpsum[i+1] == ' ':
        loreIpsum = loreIpsum[:i+2]+loreIpsum[i+2].title()+loreIpsum[i+3:]
    if loreIpsum[i].isalnum():
        if loreIpsum[i].isdigit():
            countDigit += 1
    elif loreIpsum[i] == '!':
        exclamationPoints += 1
        countSymbols += 1
    else:
        countSymbols += 1
    i += 1
print(f'Number of digits: {countDigit}')
print(f'Punctuation occurs in the text: {countSymbols}')
print(f'! occurs in the text: {exclamationPoints}')



