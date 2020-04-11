
print("Enter dimentions (nxm):", end='')
n,m = map(int, input().split())

print("Enter {} rows:".format(n))

rows = [input() for _ in range(n)]

print(rows)

k = int(input('enter key:'))
for row in rows:
    print(int(row.split()[k]))

for row in sorted(rows, key = lambda row:int(row.split()[k])):
    print(row)