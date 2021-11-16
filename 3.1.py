from random import random
n = int(input("masukan jumlah n : "))
a = 0
for i in range (n):
    a+= 1
    while 1:
        b = random()
        if b < 0.5:
            break
    print("data ke:",a,"=>",b)
print("selesai")