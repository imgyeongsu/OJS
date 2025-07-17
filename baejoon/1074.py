n, r, c = map(int, input().split())


binr = bin(r)[2:]
binc = bin(c)[2:]

row_n = 0
for i in range(len(binr)):
    if binr[i] == '1':
        row_n += (4 ** (len(binr) - (i + 1))) * 2
row_c = 0
for i in range(len(binc)):
    if binc[i] == '1':
        row_c += (4 ** (len(binc) - (i + 1)))

print(row_n + row_c)
