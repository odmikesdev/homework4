try:
    userString = input('Please enter string: ')
    userWord = input('Please enter word: ')
    changeWord = input('Please enter word for change: ')
    if userWord == changeWord:
        raise Exception()
except Exception:
    print('Word for change must != word for search')
item = 0
while item != -1:
    item = userString.find(userWord)
    if item !=-1:
        userString = userString.replace(userWord, changeWord, 1)
print(userString)

