isim=input("Adınızı Girin ")
sayac=0
while sayac < len(isim):
  print(isim[sayac])
  sayac += 1
else:
   print("Adının harflerini listelendi")
    
    
    
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
    
    
