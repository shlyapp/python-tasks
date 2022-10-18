data = set()
result = list()

a = input()
while a != '#':
    operand, name = list(map(str, a.split()))
    if operand == '+':
        data.add(name)
    elif operand == '-':
        data.remove(name)
    else:
        if name in data:
            result.append("YES")
        else:
            result.append('NO')
    a = input()

for element in result:
    print(element)
