d = [input() for i in range(int(input()))]
s = input()
print(sum(1 for w in s.split() if not w in d and sum(
    1 for c in w if c.isupper()) != 1))
