

#---- []|] ----
try:
    ilk_sayı = int(input("ilk_sayı\t:"))
    ikinci_sayı = int(input("ikinci_sayı\t:"))
    print("{} / {} = {}".format(ilk_sayı,ikinci_sayı,(ilk_sayı/ikinci_sayı)))
except ValueError as hata:
    print(hata)

#---- []|] ----
try:
    ilk_sayı = int(input("ilk_sayı\t:"))
    ikinci_sayı = int(input("ikinci_sayı\t:"))
    print("{} / {} = {}".format(ilk_sayı,ikinci_sayı,(ilk_sayı/ikinci_sayı)))
except (ValueError,ZeroDivisionError) as hata:
    print(hata)

#---- []|] ----
# try...except...else.. hatalrı gruplamak için kullanılabilri

try:
    bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: "))
except ValueError:
    print("Lütfen sadece sayı girin!")
else:
    try:
        print(bölünen/bölen)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")
#---- []|] ----
# try...except...finally...
# Finally bloğunun en önemli özelliği, programın çalışması sırasında 
# herhangi bir hata gerçekleşse de gerçekleşmese de işletilecek olmasıdır.7

try:
    dosya = open("dosyaadı", "r")
    ...burada dosyayla bazı işlemler yapıyoruz...
    ...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()
#---- []|] ----
# raise
# bazen yazdığımız bir programda kullanıcın yaptığı hata işlemi
# normal şartlarda hata vermeyecek olsa bile biz one Python tarzı bir
# hata mesajı göndermek isteyebiliriz
tr_karakter = "şçğüöıİ"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass

print("Parola kabul edildi!")
#---- []|] ----
# assert 
#assert ifadesi hızlı bir şekilde kodumuzdaki hataları belirlemek için kullanılır.
giriş = input("Merhaba! Adın ne? ")
if len(giriş) == 0:
    raise AssertionError("İsim bölümü boş.")
print("Hoşgeldiniz.")

#Bu kodu assert kullanarak şu şekilde de yazabilirdik:
giriş = input("Merhaba! Adın ne? ")
assert len(giriş) != 0 , "İsim bölümü boş."
print("Hoşgeldiniz.")
# assert ifadesi assert(ifade) şeklinde KULLANILMAMALIDIR!!
# Assert kullanımının 2 temel faydası vardır
# --1--find ile assert geçen yerleri bulup toplu yoruma alabiliriz
# --2-- Python yorumlayıcı üzerinde -0 parametresi yani optimiz parametresi
# ile çalıştırıldığında assertleri yok sayarak kodu çalıştırır
