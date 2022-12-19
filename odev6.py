isim=input("Adınızı Girin ")
sayac=0
while sayac < len(isim):
  print(isim[sayac])
  sayac += 1
else:
   print("Adının harflerini listelendi")
    
    
 #(zehra şahaplıoğlu tarafından ekleme yapıldı.)   
print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI 💪")
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 
endeks  = kilo/(boy*boy)
 
if endeks <=18:
    print("\n zayıf VKİ:{}".format(endeks))
elif endeks > 18 and endeks <=25 :
    print("\n kilolu VKİ:{}".format(endeks))
elif endeks > 25 and endeks <=30:
    print("\n obez VKİ:{}".format(endeks))
elif endeks > 30:
    print("\n ciddi obez VKİ:{}".format(endeks))
    
    
 
#sayı tahmin oyunu(sennur aldemir tarafından ekleme yapıldı.)
from random import randint
 
rand=randint(1, 100)
sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
﻿
