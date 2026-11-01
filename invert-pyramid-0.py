n = int(input())
i = 0
total = ""
while i <= n:
    total += str(i)
    i += 1
print(total)
i = 1
j = 0
while i < n:
    while i < n:
        print(total[:len(total)- 1 - j])
        i += 1
        j += 1
    i += 1
    j += 1