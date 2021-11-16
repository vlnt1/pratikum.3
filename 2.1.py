bilangan1 = int(input("masukan bilangan 1 : "))
bilangan2 = int(input("masukan bilangan 2 : "))
bilangan3 = int(input("masukan bilangan 3 : "))
if bilangan1 > bilangan2 and bilangan1 > bilangan3:
  print("Bilangan 1 lebih besar")
elif bilangan2 > bilangan1 and bilangan2 > bilangan3:
  print("Bilangan 2 lebih besar")
else:
  print("Bilangan 3 lebih besar")