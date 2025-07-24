Nilai = [[55, 20, 30],
         [40, 50, 60],
         [70, 80, 90]]
sum = 0
for i in range (len(Nilai)):
    for j in range (len(Nilai[i])):
        sum = sum + Nilai[i][j]
    print(sum)
    sum = sum * 0
    