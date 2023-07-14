N = int(input())

for i in range(N):
    str1, str2 = input().split()
    answer = ""

    i = 0
    while i < len(str1) + len(str2):
        if (i < len(str1)):
            answer += str1[i]
        if (i < len(str2)):
            answer += str2[i]
        i += 1

    print(answer)