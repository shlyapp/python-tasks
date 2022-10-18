num = int(input())
x_coord = set()

for i in range(num):
    x, y = map(int, input().split())
    x_coord.add(x)

print(len(x_coord))
