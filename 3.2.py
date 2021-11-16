bilangan=0
while True:
    i=int(input("masukan bilangan : "))
    if bilangan < i :
        bilangan= i
    if i==0:
        break
print("bilangan terbesar adalah :",bilangan)