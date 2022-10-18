n = int(input())
words = dict()

for i in range(n):
    line = list(filter(None, input().replace(
        '-', ' ').replace(',', ' ').split(' ')))
    for j in range(len(line) - 1):
        if words.get(line[j + 1]) is None:
            words[line[j + 1]] = line[0]
        else:
            words[line[j + 1]] = f"{words.get(line[j + 1])}, {line[0]}"

a = list((sorted(words.keys())))

for element in a:
    print(f"{element} - {words.get(element)}")
