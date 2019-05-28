spam = ['apple', 'bananas', 'tofu', 'cats']
def commacode(list1):
    for i in range(len(list1) - 1):
        print(list1[i] + ', ', end="")
    print('and ' + list1[len(list1) - 1])

commacode(spam)
