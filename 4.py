num = int(input())

telephone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wzyx']
numbers = list()

for i in range(num):
    company = input()
    number = ''
    for letter in company:
        for j in range(len(telephone)):
            if letter in telephone[j]:
                number += str(j)
                break
    numbers.append(number)

print(len(set(numbers)))
