print("Program Mengurutkan Data")
bilangan1 = int(input("Masukkan bilangan ke-1: "))
bilangan2 = int(input("Masukkan bilangan ke-2: "))
bilangan3 = int(input("Masukkan bilangan ke-3: "))

def bilanganterbesar (bilangan1,bilangan2,bilangan3):
  if bilangan1 > bilangan2 and bilangan2 > bilangan3:
    return bilangan1
  elif bilangan2 > bilangan1 and bilangan2 > bilangan3:
    return bilangan2

  return bilangan3

def bilanganterkecil(bilangan1, bilangan2, bilangan3):
  if bilangan1 < bilangan2 and bilangan1 < bilangan3:
    return bilangan1
  elif bilangan2 < bilangan1 and bilangan2 < bilangan3:
    return bilangan2

  return bilangan3

def bilangantengah(bilangan1, bilangan2, bilangan3):
  if (bilangan2 > bilangan1 > bilangan3) or (bilangan3 > bilangan1 > bilangan2):
    return bilangan1
  elif (bilangan1 > bilangan2 > bilangan3) or  (bilangan3 > bilangan2 > bilangan1):
    return bilangan2
  
  return bilangan3

i1 = bilanganterkecil(bilangan1, bilangan2, bilangan3)
i2 = bilangantengah(bilangan1, bilangan2, bilangan3)
i3 = bilanganterbesar(bilangan1, bilangan2, bilangan3)

print(f'Urutan bilangan: {i1}, {i2}, {i3}')