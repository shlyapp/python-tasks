num_files = int(input())
files = dict()

for i in range(num_files):
    line = list(map(str, input().split()))
    file_name = line[0]
    mod = line[1:]
    files[file_name] = mod

num_operations = int(input())
result = list()

for i in range(num_operations):
    mod, file_name = map(str, input().split())
    if mod == 'read':
        mod = 'R'
    if mod == 'write':
        mod = 'W'
    if mod == 'execute':
        mod = 'X'

    if files.get(file_name) is not None and mod in files.get(file_name):
        result.append("OK")
    else:
        result.append("Access denied")

for element in result:
    print(element)
