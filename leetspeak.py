user_input = input('Type a word? ')
user_input = user_input.upper()
leet = ['A','E','G','I','O','S','T']
numbers = ['4','3','6','1','0','5','7']

for letter in user_input:
    if letter in leet:
        print(numbers[leet.index(letter)])
    else:
        print(letter)