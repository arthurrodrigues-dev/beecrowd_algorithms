N = int(input())


for i in range(N):
    str1, str2 = input().split()
    res = ""
    i = 0
    while i < len(str1) + len(str2):
        if (i < len(str1)):
            res += str1[i]
        if (i < len(str2)):
            res += str2[i]
        i += 1
    print(res)