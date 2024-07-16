#MUSTAFA KILIÇ     11.05.2022
import sys
bilgiler =["Numara","Ad","Soyad","Deger(M)","Yas",""]
futbolcu= None
son_numara = None
print("FUTBOLCU BİLGİ OTOMASYONUNA HOŞGELDİNİZ")
def menu():

    print( "  Menu","0-Listeleme", "1-Guncelleme", "2-Ekleme","3-Arama","4-Ortalama bul","5-Transfer teklifi degerlendirme","6-Silme","7-Cikis", sep="\n")
    secim = int(input("Hangi işlemi yapmak istiyorsunuz?"))
    if (secim == 0):
        futbolcu_listele()
        menu()
    elif (secim == 1):
        guncelleme_yap()
        menu()

    elif (secim == 2):
        #  önceki halini görmek için futbolcu listeleme yaptım.
        futbolcu_listele()
        futbolcu_ekle()
        menu()

    elif (secim == 3):
        aramayap()
        menu()

    elif (secim==4):
        ort_bul()
        menu()

    elif (secim==5):
        transfer()
        menu()

    elif (secim == 6):
        futbolcu_sil()

    elif (secim == 7):
        sys.exit()
        menu()

    else:
        print("yanlis secim yaptiniz menuye donuyorsunuz")
        menu()

def futbolcu_listele():
    global futbolcu
    if (futbolcu == None):
        futbolcu = dict()

    def fut_format(fut_list):
        global futbolcu
        global son_numara
        for fut in fut_list:
            fut_values = fut.split(" ")
            data = dict()
            for i in range(1, len(fut_values)):
                data[bilgiler[i]] = fut_values[i]
            futbolcu[fut_values[0]] = data
            son_numara = fut_values[0]

    with open("futbolcu.txt", "r") as ffile:
       flist = ffile.readlines()
    fut_format(flist)

    for fut in futbolcu.keys():
        print("futbolcu Id:{}".format(fut), end=" ")
        for fut_bilgi in futbolcu[fut].keys():
            print("{:} : {:}".format(fut_bilgi, futbolcu[fut][fut_bilgi]), end=" ")
        print()
def futbolcu_ekle():
    global futbolcu
    global son_numara
    son_numara = str(int(son_numara) + 1)
    ad = input("eklenecek futbolcunun adı :")
    soyad = input("eklenecek futbolcunun soyadı :")
    deger = input("eklenecek futbolcunun degeri(m) :")
    yas = input("eklenecek futbolcunun yasi :")


    futbolcu[son_numara] = {"Ad": ad, "Soyad": soyad, "Deger": deger, "Yas": yas }
    with open("futbolcu.txt", "a") as ffile:
        ffile.write("\n")
        ffile.write(son_numara)
        for i in futbolcu[son_numara].keys():
            ffile.write(" " + futbolcu[son_numara][i])


def futbolcu_sil():
    sil=int(input("silinecek kisinin numarasini giriniz"))
    with open("futbolcu.txt", "r") as ffile:
        flist = ffile.readlines()

    del flist[sil-1]
    print("Basariyla silme islemini gerceklestirdiniz.")
    print("Guncel hal bu sekildedir {}".format(flist))
    with open("futbolcu.txt", "w") as ffile:
        ffile.writelines(flist)

def aramayap():
    ara=int(input("aranacak idyi giriniz"))
    with open("futbolcu.txt", "r")as ffile:
        flist=ffile.readlines()

    if ara<=len(flist):
        print("Aradıginiz idye ait veri bulundu ve asagidaki gibidir")
        print(flist[ara-1])
    else:
        print("Aradıginiz idye ait veri bulunamadi menuye donuyorsunuz")


def guncelleme_yap():
    guncelle = int(input("güncellemek istediğiniz kişinin sırasini giriniz"))
    with open("futbolcu.txt", "r") as ffile:
        flist = ffile.readlines()
    degisecek=(flist[guncelle-1])
    print("guncellenmesini istediginiz kisinin su anki bilgileri-> {}".format(degisecek),end="\n")
    sp=degisecek.split()

    ad = input("guncellemeden sonraki ad :")
    soyad = input("guncellemeden sonraki soyad :")
    deger = input("guncellemeden sonraki deger :")
    yas = input("guncellemeden sonraki yas :")

    sp[1] = ad
    sp[2] = soyad
    sp[3] = deger
    sp[4] = yas
    metin=""
    for kelime in sp:
        metin=metin+kelime+" "
    metin+="\n"
    flist[guncelle-1]=metin

    with open("futbolcu.txt", "w") as ffile:
        ffile.writelines(flist)
    with open("futbolcu.txt", "r") as ffile:
        flist=ffile.read()
    print(flist)
def ort_bul():
    with open("futbolcu.txt", "r") as ffile:
        flist = ffile.readlines()
    sp=[]
    for i in range(len(flist)):
        deg=flist[i]
        sp+=deg.split()

    toplam=float(sp[3])

    for i in range(0,len(sp),5):
        toplam+=float(sp[3+i])
    x=len(flist)
    ort= toplam/x
    print("////////////////////")
    print("Ortalama={}".format(ort))
    print("////////////////////")

def transfer():
    with open("futbolcu.txt", "r") as ffile:
        flist = ffile.readlines()

    oyuncu = int(input("teklif vermek istediginiz oyuncunun idsini giriniz"))
    print("oyuncun bilgileri asagidaki gibidir")
    print(flist[oyuncu-1])
    teklif=(flist[oyuncu-1])
    sp=teklif.split()
    vdeger = float(input("teklif ettiginiz tutari giriniz "))
    x=float(sp[3])
    if vdeger<x*0.7:
        print("Teklifiniz yeterli değil fakat yeni gorusme yapabiliriz")
        secim=int(input("Teklifinizi arttırmak istiyor musunuz?1-evet,2-hayir"))
        if secim==1:
            ydeger=int(input("teklif ettiginiz tutari giriniz "))
            if ydeger < x * 0.7:
                print("Teklifiniz yine yeterli değil maalesef anlaşma şartları sağlanamadı ")
            elif x * 0.7 <= ydeger <= x * 1.1:
                print("Teklifiniz kulübümüz tarafından degerlendirilmeye alınmıştır 1 hafta icinde size geri donus yapilacaktir.")
            else:
                print("Teklifiniz kulübümüz tarafından  kabul edildi oyuncuyla gorusme yapabilirsiniz")
        else:
            print("iyi gunler hoscakalin")

    elif x*0.7 <= vdeger <= x :
        print("Teklifiniz kulübümüz tarafından degerlendirilmeye alınmıştır 1 hafta icinde size geri donus yapilacaktir.")
    else:
        print("Teklifiniz kulübümüz tarafından  kabul edildi oyuncuyla gorusme yapabilirsiniz")


menu()