n = int(input())  
s = 0
for i in range(n):
    N = int(input())
    if N % 10 == 9:
        s = s + 1
print(s)