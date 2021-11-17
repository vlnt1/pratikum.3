nilai = [0,1,2,3,4,5,6,7,8,9]
baris = 10
for a in range(baris) :
    print(*nilai, sep="\t")
    for coloum in range (10):
        nilai [coloum]=nilai[coloum]+1 