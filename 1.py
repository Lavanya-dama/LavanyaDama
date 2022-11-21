def decToBinary(s):
    binaryNum = [0] * s
    i = -1
    while (s > 0):
        binaryNum[i] = s % 2
        s = int(s / 2)
        i += 1
    for j in range(i - 1, -1,-1):
        print(binaryNum[j], end = "")
s = 10
decToBinary(s)
