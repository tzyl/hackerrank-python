n = int(input())
s = "min(int, int)"
n -= 2
while n:
    s = "min(int, " + s + ")"
    n -= 1
print(s)
