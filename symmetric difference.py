M = int(input().strip())
a = set(map(int, input().rstrip().split()))
N = int(input().strip())
b = set(map(int, input().rstrip().split()))
key = a.difference(b).union(b.difference(a))
for i in sorted(list(key)):
    print(i)