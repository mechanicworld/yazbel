import os
# ---- []|] ----
# Kaçış dizisi --- escape sequence
# "\" işaretini kaçış dizisi olarak şu şekilde kullanabilirz
# aynı zamanda satır bölücüü olarak da kullanılır
os.system("cls")
print("\"book \" kelimesi Türkçede \"kitap\" anlamına gelir.")
print("merhaba dost\
    bugün ben geldim\
    evde değilsen\
    sonra gelirim")
# Yukarıda görüldüğü gibi eğer " " işareti kullanmak 
# istiyorsam bir kaçış dizisi eklemesi ile farklı tırnak kullanmak
# zorunda olmadan kullanabilirim
# ---- []|] ----
# \ kaçış dizisi karakterine başka karakterler
# eklenerek farklı görevleri bulunan yeni kaçış
# dizileri oluşturulabilir
# (\n) satır başı
os.system("cls")
print("Hello \n Hello")
# (\t) tab için kullanılır
os.system("cls")
print("Hello \t Hello")
# (\a) bip sesidir
os.system("cls")
print("\a")
# (\r) aynı satır 
os.system("cls")
print("Hello Tello Mello")
print("Hello \r Tello \r Mello")
# (\b) imleç kaydırma işareti olarak geçer
os.system("cls")
print("yahoo.com\b")
print("yahoo.com\b.uk")
# (\u)(\U)(\N) unicode ifadesidir bu bize tanımlı karakterleirn unicode larını veriri
print("\U00000131")
