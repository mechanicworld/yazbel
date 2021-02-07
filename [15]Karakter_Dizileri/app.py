

import os
def clrScreen():
    os.system("cls")
# #---- []|] ----
# # Karakter dizilerini tersine çevirmek

# message = "Bir gül için katlanmaktır acılara."

# print(message[::-1])

# # farklı bir yöntem olarak
# print(reversed(message))# obje lokasyonu tanımlar
# print(*reversed(message))
# print(*reversed(message),sep="")

# # Türkçe karakter sıralaması için 
# import locale 
# locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")

# print(*sorted("çiçek"))
# print(*sorted("çiçek",key=locale.strxfrm))

# # bu işlemi kendi verdiğimiz sıralama ile yapmak istersek eğer
# harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
# çevrim = {i: harfler.index(i) for i in harfler}
# print(*sorted("afgdhkıi", key=çevrim.get))

# # 3 ÖNEMLİ FONKSİYON !!!
# # --1--
# # dir() Bu metot bize Python’daki bir nesnenin özellikleri 
# # hakkında bilgi edinme imkanı verecek.
# import os
# os.system("cls")
# print(type(dir("")))

# sayaç = 0
# for i in dir(""):
#     if "_" not in i[0]:
#         sayaç += 1
#         print(i)

# print("Toplam {} adet metot ile ilgileniyoruz.".format(sayaç))
# #--2--
# #enumerate() sıralama yapmamızı sağlayan bir fonksiyondur
# os.system("cls")
# for sıra, metot in enumerate(dir("")):
#     if "_" not in metot:
#         print(sıra,metot)

# #--3--
# #help() herhangi bir konu hakkında bilgi almak istediğimizde 
# # help fonksiyonu içerisine yazarak bilgi edinebiliriz

# #---- []|] ----
# # Karakter Dizisi genl Metodları
# #replace()

# clrScreen()

# message = "Naber kardeş!"
# print(message.replace("k","K"))
# #split(), rsplit(), splitlines()
# clrScreen()
# message = "İstanbul Büyükşehir Belediyesi"
# print(message.split())
# # rsplit() split ile aynı fonksiyondur sadece okuma olarak sağdan okuma yapar
# clrScreen()
# print(message.rsplit(" ", 1))
# print(message.split(" ", 1))

# metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
# tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
# Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
# düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
# gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
# komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
# adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
# dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
# halini almıştır diyebiliriz."""

# clrScreen()
# print(metin.splitlines())
# print(metin.splitlines(True))

# # lower() ,upper(), islower(), isupper(), endswith(), startswith(),casefold()

# #casefold() alfabelerdeki özel harfler için çalışan bir lower() metodudur
# clrScreen()
# message = "Elma severim"
# print(message.lower())
# print(message.upper())
# print(message[0].isupper())
# print(message[0].isupper())
# print(message.endswith("m"))
# print(message.endswith("M"))
# print(message.startswith("E"))

# # capitalize(), title()

# message = "python ile programlama ne güzel, ne hoş"

# clrScreen()
# print(message.capitalize())
# print(message.title())

# # swapcase()
# clrScreen()
# message = "Merhaba Dostlar ne güzel"
# print(message.swapcase())

# #strip(), lstrip(), rstrip()
# clrScreen()
# message = "    boşluk var başta sonda    "
# print(message.strip())
# print(message.lstrip())
# print(message.rstrip())
# print("Merhaba".strip("M"))
# print("KABAK".strip("K"))
# print("KABAK".lstrip("K"))

# # join(), count()
# clrScreen()
# message = "Adıyaman Spor Kulubü"
# toplam = message.split()
# print(toplam)
# print(type(toplam))
# newToplam = " ".join(toplam)
# print(newToplam)
# print(newToplam.count("a"))
# print(newToplam.lower().count("a"))
# print(newToplam.lower().count("a",1))
# print(newToplam.lower().count("a",2))
# print(newToplam.lower().count("a",10))

# #index(), rindex(), find(), rfind()
# #index() ve rindex() metotları karakter dizisi içindeki 
# #karakteri sorgularken, eğer o karakteri bulamazsa
# #bir ValueError hatası verir
# #ama find() ve rfind() metotları böyle bir durumda -1 çıktısı verir:
# clrScreen()
# message = "python python"
# print(message.index("p"))
# print(message.index("n"))
# print(message.find("z"))
# #print(message.index("z"))

# center(),rjust(), ljust(), zfill()


message = "python"
for i in range(1, 20,2):
    print(message.center(i))
    message = "python"
for i in range(1, 20,2):
    print(message.center(i,"-"))

for i in range(1, 20,2):
    print(message.rjust(i,"-"))
for i in range(1, 20,2):
    print(message.ljust(i,"-"))
for i in range(1, 20,2):
    print(message.zfill(i))

# partition(), rpartition()
clrScreen()

message = "istikbal"
print(message.partition("i"))
print(message.rpartition("i"))
print(message.partition("g"))# eğer harf yok ise
print(message.rpartition("g"))# eğer harf yok ise

# encode()
# bu metot yardımıyla karakter dizilerimizi istediğimiz 
#kodlama sistemine göre kodlayabiliriz
print("çilek".encode("cp1254"))

# expandtabs()
message = "elma\tbir\tmeyvesidir"
print(message.expandtabs(10))

# str.maketrans(), translate()

kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

çeviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."

print(metin.translate(çeviri_tablosu))

print(chr(97))
print(chr(105)) 
# sil ve değiştir
metin = "Cem Yılmaz"

kaynak = "CY"
hedef  = "cy"
silinecek = "eıa "

çeviri_tablosu = str.maketrans(kaynak, hedef, silinecek)

print(metin.translate(çeviri_tablosu))
#Burada ‘C’ ve ‘Y’ harflerini sırasıyla ‘c’ ve ‘y’ harfleriyle 
# eşleştirdik. Bu nedenle orijinal metin içindeki ‘C’ ve ‘Y’ 
# harfleri yerlerini sırasıyla ‘c’ ve ‘y’ harflerine bıraktı.
#  Silinecek karakterler olarak ise ‘e’, ‘ı’, ‘a’ ve boşluk 
# karakterlerini seçtik. Böylece ‘Cem Yılmaz’ adlı orijinal 
# metin içindeki boşluk karakteri de silinerek, bu metin ‘cmylmz’
#  karakter dizisine dönüştü.

# isalpha(), isdigit(), isalnum(),isdecimal()
# isidentifier(), isspace(), isprintable()