#1.Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi, da se dodadat vo list i da se soberat site broevi vo listata

"""lista=[]
br_sum=0
for i in range(4):
    br=int(input("vnesete broj"))
    lista.append(br)
    br_sum=br_sum+br

print(lista)
print(br_sum)"""


#2.Da se napravi programa vo koja korisntikot ke moze da vnese proizvolen broj na broevi, da se dodadt vo lista i da se najde najgolemiot broj

"""list=[]
br=int(input("kolku broevi sakate da vnesete "))
for i in range(br):
    x=int(input("vnesete broj "))
    list.append(x)

print(list)
print(max(list))"""


#3. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na elementi, da se ispecati listata i korisnikot da moze da izbere kolku
#  elementi i koi elementi ke gi izbrise

"""list=[]
br=int(input("kolku broevi sakate da vnesete "))
for i in range(br):
    x=int(input("vnesete broj"))
    list.append(x)

print(list)

el_brishenje=int(input("Kolku elementi sakate da izbrishete "))
for i in range(el_brishenje):
    y=int(input("element so koj indeks da bide izbrishan "))
    del list[y]

print(list)"""


#4. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na iminja, da se dodadat vo lista, i da se najde najdolgoto ime

"""dolzina=[]
list=[]
br=int(input("kolku iminja sakate da vnesete "))
for i in range(br):
    ime=(input("vnesete ime "))
    list.append(ime)
    ime_dolzina=len(ime)
    dolzina.append(ime_dolzina)

print(list)
print(max(dolzina))"""


#5. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na broevi, da se dodadat vo lista i da se najde vtoriot najgolem broj

"""list=[]
br=int(input("kolku broevi sakate da vnesete "))
for i in range(br):
    x=int(input("vnesete broj"))
    list.append(x)
 
mx = max(list[0], list[1])
secondmax = min(list[0], list[1])
n = len(list)
for i in range(2,n):
    if list[i] > mx:
        secondmax = mx
        mx = list[i]
    elif list[i] > secondmax and \
        mx != list[i]:
        secondmax = list[i]
    elif mx == secondmax and \
        secondmax != list[i]:
          secondmax = list[i]
 
print("Second highest number is : ",\
      str(secondmax))
"""

#6. Da se napravi programa koja ke bide upotrebuvana vo nekoja prodavnica za prodazba. Korisnikot da moze da vnesuva 
#produkti se dodeka ne izbere deka saka da plati. Produktitte da se dodavaat vo edna lista, cenite vo druga lista. Koga ke izbere deka saka da 
# plati da mu se ispecatat produktite i cenite vo nalik na "fiskalna smetka". Da ima moznost korisnikot da plati i da se presmeta dali i kolku
#  treba da mu se vrati kusur

cena_lista = []
produkti=[]
total=0
while True:
    produkt = input("Vnesi go produktot: ")
    cena = int(input("Vnesi ja cenata: "))
    produkti.append(produkt)
    cena_lista.append(cena)
    da_ne = input("Dali sakate da pristapite kon plakanje (da/ne): ")
    if (da_ne == 'da'):
        break

print(produkti)
print(cena_lista)
for i in range(0, len(cena_lista)):
    total = total + cena_lista[i]
print("za naplata imate {}".format(total))

plakanje = int(input("Vnesete ja uplatata: "))
while True:
    if (plakanje < total):
        plakanje = int(input("Ve molime uplatete {} ".format(total)))
    else:
        break
kusur = plakanje - total
print("Uplateni se {} den, vkupnata cena e {}, kusurot e {}".format(plakanje, total, kusur))