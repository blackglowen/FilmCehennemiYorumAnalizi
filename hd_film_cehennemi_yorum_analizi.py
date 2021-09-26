import requests
from bs4 import BeautifulSoup
import io
"""
yapılan işlemler kısaca;
sunulan seçeneklerden biri seçilince o film türü için senaryo başlar.
bu senaryoda film türünün bulunduğu sayfaya gider ve oradaki film adları çekilir.
sürekli güncellemelere karşılık film sayfalarında artış veya azalış olabilir. o yüzden bunun otomatik olarak program tarafında güncellenmesi gerkir.
bunun için çekilen film türü sayfasında en altta bulunan sayfa numaraları kısmında en son sayfaya gidilerek oradaki web adresinden sayfa numarası page/7 şeklinde bulunan 7 kısmı alınır. 
bu bizim web adresinin kaç sayfadan oluştuğunu gösterir. ve bu bir for döngüsü içine aktarılarak film adları bir listeye eklenince sayfa sayısı kadar dolaşır yani bütün sayfaları dolaşır ve var olan bütün filmler 
listmeize eklenmiş olur.
burda iki liste oluşturulur. birincisi film adlarının '-' olmadan ki halidir. ikincisi ise web adresine eklenecek olan ve içinde '-' karakteri olan listedir.
birinci liste içinde bir kaç işlem olur bunlardan bir tanesi web adresinden film adı çekilirken şu gelirdi. slate izle 
kullanıcı izle ekini/kelimesini yazmayacağı için bunun kaldırılması için bir işlemden geçirilir. bunun yanında girilen isim büyük harfle yazılmışsa eğer hepsini küçük harflere çevirir.
çünkü kullanıcı yanlışlıkla bir harfi büyük yazarsa bile program aksamadan direk çalışmaya devam eder.

daha sonra bizden bir film adı girmemiz istenir.
girilen film adı bizim elimizde bulunan birinci liste içinde aranır bulunduğu zaman da web adresine eklenecek olan ek kısmı için bir atama gerçekleştirilir.
daha sonra o ek eklendikten sonra da o film adresine gidilir. ve filmin videosunun bulundğu sayfaya giderek orada yorum kısmı çekilir. çekilen kısımda bir hata olabilir o da filmin yorumsuz olmasıdır.
yorumsuz olduğu zaman <ol class... kısmı olmaz o yüzden bool ifadesinin içinde bir <ol class... olup olmadığı kontrol edilir. içi boş ise eğer bir hata mesajı verir ve programdan çıkılır.
eğer yorum varsa da o yorum kısmı çekilerek oradaki text ifadeleri çekilir ve yorumlama metoduna parametreler ile gönderilerek yorumun olumlu ve olumsuz olması araştırrlır ve bir çıktı elde edilir.

önemli not:
filmin çekileceği sitede eğer ki yorumlar tırnak işareti içerisinde bulunuyor ise türkçe karakter hatası verir. yani kelimeleri ,harfleri düzgün çekemeyiz. eğer ki tırnak içerisinde değilse kelimeleri türkçe karakter içerse bile hata vermeden
olduğu gibi çekebiliriz. hdfilmcehennemi sitesinde tırnak işareti içinde olduğu için hata aldık. filmmodunda ise öyle olmadığı için hata almadık o yüzden ikisi için de tanımlayabilmesi için ayrı aryı kodlar yazacağız.


"""

class Analiz():
    def web_kismi(self):
        girilen=input("lütfen bir tür seçiniz....")
        film_nesnesi=film_turleri()

        girilen=str(girilen) #tip dönüşümü yaptım çünkü sayısal bir değer girilebilir. program hata vermesin diye string tipine dönüştürdük.

        if girilen=="2000 ve öncesi":
            film_nesnesi.ikibin_ve_oncesi_filmleri()
        elif girilen=="2001":
            film_nesnesi.ikibin_bir_filmleri()
        elif girilen=="2002":
            film_nesnesi.ikibin_iki_filmleri()
        elif girilen=="2003":
            film_nesnesi.ikibin_uc_filmleri()
        elif girilen=="2004":
            film_nesnesi.ikibin_dort_filmleri()
        elif girilen=="2005":
            film_nesnesi.ikibin_bes_filmleri()
        elif girilen=="2006":
            film_nesnesi.ikibin_alti_filmleri()
        elif girilen=="2007":
            film_nesnesi.ikibin_yedi_filmleri()
        elif girilen=="2008":
            film_nesnesi.ikibin_sekiz_filmleri()
        elif girilen=="2009":
            film_nesnesi.ikibin_dokuz_filmleri()
        elif girilen=="2010":
            film_nesnesi.ikibin_on_filmleri()
        elif girilen=="2011":
            film_nesnesi.ikibin_on_bir_filmleri()
        elif girilen=="2012":
            film_nesnesi.ikibin_on_iki_filmleri()
        elif girilen=="2013":
            film_nesnesi.ikibin_on_uc_filmleri()
        elif girilen=="2014":
            film_nesnesi.ikibin_on_dort_filmleri()
        elif girilen=="2015":
            film_nesnesi.ikibin_on_bes_filmleri()
        elif girilen=="2016":
            film_nesnesi.ikibin_on_alti_filmleri()
        elif girilen=="2017":
            film_nesnesi.ikibin_on_yedi_filmleri()
        elif girilen=="2018":
            film_nesnesi.ikibin_on_sekiz_filmleri()
        elif girilen=="2019":
            film_nesnesi.ikibin_on_dokuz_filmleri()
        elif girilen=="2020":
            film_nesnesi.ikibin_yirmi_filmleri()
        elif girilen=="2021":
            film_nesnesi.ikibin_yirmi_bir_filmleri()
        elif girilen=="aile":
            film_nesnesi.aile_filmleri()
        elif girilen=="aksiyon":
            film_nesnesi.aksiyon_filmleri()
        elif girilen=="animasyon":
            film_nesnesi.animasyon_filmleri()
        elif girilen=="belgesel":
            film_nesnesi.belgesel_filmleri()
        elif girilen=="bilim kurgu":
            film_nesnesi.bilim_kurgu_filmleri()
        elif girilen=="biyografi":
            film_nesnesi.biyografi_filmleri()
        elif girilen=="dini":
            film_nesnesi.dini_filmleri()
        elif girilen=="dram":
            film_nesnesi.dram_filmleri()
        elif girilen=="en iyi":
            film_nesnesi.en_iyi_filmleri()
        elif girilen=="fantastik":
            film_nesnesi.fantastik_filmleri()
        elif girilen=="gençlik":
            film_nesnesi.genclik_filmleri()
        elif girilen=="gerilim":
            film_nesnesi.gerilim_filmleri()
        elif girilen=="gizem":
            film_nesnesi.gizem_filmleri()
        elif girilen=="hint":
            film_nesnesi.hint_filmleri()
        elif girilen=="imdb":
            film_nesnesi.imdb_filmleri()
        elif girilen=="imdb top":
            film_nesnesi.imdb_top_filmleri()
        elif girilen=="komedi":
            film_nesnesi.komedi_filmleri()
        elif girilen=="kore":
            film_nesnesi.kore_filmleri()
        elif girilen=="korku":
            film_nesnesi.korku_filmleri()
        elif girilen=="macera":
            film_nesnesi.macera_filmleri()
        elif girilen=="marvel":
            film_nesnesi.marvel_filmleri()
        elif girilen=="muzikal":
            film_nesnesi.muzikal_filmleri()
        elif girilen=="polisiye":
            film_nesnesi.polisiye_filmleri()
        elif girilen=="psikolojik":
            film_nesnesi.psikolojik_filmleri()
        elif girilen=="romantik":
            film_nesnesi.romantik_filmleri()
        elif girilen=="savaş":
            film_nesnesi.savas_filmleri()
        elif girilen=="spor":
            film_nesnesi.spor_filmleri()
        elif girilen=="suç":
            film_nesnesi.suc_filmleri()
        elif girilen=="tarih":
            film_nesnesi.tarih_filmleri()
        elif girilen=="tavsiye":
            film_nesnesi.tavsiye_filmleri()
        elif girilen=="türk komedi":
            film_nesnesi.turk_komedi_filmleri()
        elif girilen=="western":
            film_nesnesi.western_filmleri()
        elif girilen=="yerli":
            film_nesnesi.yerli_filmleri()
        else :
            print("yanlış değer girildi..\n lütfen doğru yazınız...")
            tekrar=Analiz()
            tekrar.web_kismi()



class film_turleri():
    def ikibin_ve_oncesi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/eski-filmler'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/eski-filmler'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/eski-filmler/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum turkce_karakter_hatasi_var için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_bir_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2001-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2001-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2001-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_iki_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2002-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2002-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2002-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        print(len(film_adlari))
        print("ilk film", film_adlari[0][0])
        print("ilk film", film_adlari[5][17])
        print(len(film_list_bir))
        print(film_list_bir)
        print("girilen film adlari", girilen_film_adlari)
        print("girilen film adları boyutu:", len(girilen_film_adlari))
        print("film adları=", film_adlari)
        print("film adları boyutu", len(film_adlari))

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_uc_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2003-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2003-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2003-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_dort_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2004-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2004-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2004-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_bes_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2005-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2005-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2005-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_alti_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2006-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2006-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2006-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_yedi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2007-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2007-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2007-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_sekiz_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2008-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2008-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2008-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_dokuz_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2009-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2009-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2009-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2010-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2010-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2010-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_bir_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2011-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2011-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım

        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.
        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2011-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_iki_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2012-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2012-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2012-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_uc_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2013-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2013-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2013-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_dort_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2014-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2014-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2014-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_bes_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2015-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2015-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2015-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_alti_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2016-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2016-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2016-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_yedi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2017-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2017-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2017-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_sekiz_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2018-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2018-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2018-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_on_dokuz_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2019-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2019-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2019-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_yirmi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2020-filmleri-hd-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2020-filmleri-hd-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2020-filmleri-hd-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def ikibin_yirmi_bir_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2021-filmleri-fhd-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2021-filmleri-fhd-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/2021-filmleri-fhd-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(
                film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def aile_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/aile-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/aile-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/aile-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def aksiyon_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/aksiyon-film-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/aksiyon-film-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/aksiyon-film-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def animasyon_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/animasyon-film-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/animasyon-film-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/animasyon-film-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def belgesel_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/belgesel-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/belgesel-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/belgesel-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def bilim_kurgu_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/bilimkurgu-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/bilimkurgu-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/bilimkurgu-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def biyografi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/biyografi-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/biyografi-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/biyografi-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def dini_filmleri(self):

        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/dini-filmler'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        # buradaki if ve altında else kısmının amacı film türü girildiğinde sayfamız tek bir sayfadan oluşuyorsa yani altta bulunan sayfa numaraları kısmı yoksa if bloğu çalışır eğer sayfa numaraları kısmı varsa da else kısmı çalışır.
        if bool(sayfa_sayisi_gelen_veri) == False:
            print("sayfa adedi yoktur.")
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/dini-filmler/page/0'
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]
            film_adlari = []
            girilen_film_adlari = []
            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

            # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
            for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
                for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                    girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        else:
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/dini-filmler'
            veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

            sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
            sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
            yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

            print("yorumlar kısmı", yorumlar)
            print(type(yorumlar))
            list = []
            list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
            print("link adresi", list)
            print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
            sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
            print("list degerinin uzunluğu", len(list))
            for i in range(1, len(list)):
                if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                    sayfa_sayisi_listesi.append(list[-i])
            sayfa_sayisi_liste_olarak = []
            for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
                sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
            print(sayfa_sayisi_listesi)
            print("sayfa sayısı", sayfa_sayisi_liste_olarak)
            sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
            sayfa_sayisi = int(sayfa_sayisi)
            print("sayfa", sayfa_sayisi)
            film_adlari = []
            girilen_film_adlari = []

            # sayfalar arasında dolaşılan kısım
            sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

            for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
                sayfa_sayisi = str(i)
                sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/dini-filmler/page/' + sayfa_sayisi
                sys = requests.get(sayfa)
                soup = BeautifulSoup(sys.content, 'html.parser')
                gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
                list_sayfa_bir = []
                for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                    list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
                toplam = 0
                for i in range(len(list_sayfa_bir)):
                    list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

                veri = list_sayfa_bir[0]

                film_list_bir = []
                for i in range(len(list_sayfa_bir)):
                    veri = list_sayfa_bir[i]
                    for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                        sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                        veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                    film_list_bir.append(veri)

                film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
                girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
                # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

            # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
            for m in range(
                    len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
                for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                    girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = "20-yasinda-oleceksin-izle"  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır. burada aslında film_adlari[m][i] şeklinde atama yapmamız lazım ama türkçe karakterden dolayı deneme amaçlı cagri-izle dedik. böylece kullanıcı çağrı girdiğinde program çalışır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        # filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False:  # bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else:  # yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def dram_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/dram-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/dram-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/dram-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def en_iyi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/en-iyi-filmler'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/en-iyi-filmler'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/en-iyi-filmler/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def fantastik_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/fantastik-film-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/fantastik-film-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/fantastik-film-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

   #buraya fragmanlar da eklenebilir ama ben eklemedim.Sitede bu sırada böyle bir seçenek vardır.

    def genclik_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/genclik-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/genclik-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/genclik-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def gerilim_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/gerilim-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/gerilim-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/gerilim-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def gizem_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/gizem-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/gizem-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/gizem-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def hint_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/hint-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/hint-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/hint-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def imdb_filmleri(self): #imdb+7 filmleri içerir
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/imdb-7-ustu-filmler'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/imdb-7-ustu-filmler'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(3, len(sayfa_sayisi_listesi) + 1):  # 3 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir.bir de tür adı içinde bir sayı daha vardır 7 onu almasın diye de 3 ten başlattık yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 3 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/imdb-7-ustu-filmler/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)


        ############################

    def imdb_top_filmleri(self):# imdb top 50 filmleri içerir.
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/imdb-top-250'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/imdb-top-250'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(5, len(sayfa_sayisi_listesi) + 1): # 5 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir.bir de tür adı içinde bir sayı daha vardır 250 onu almasın diye de 5 ten başlattık yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 5 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir. içinde kaç tane sayı olursa olsun şunları almasını istemedik.

            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])

        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)

        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []
        print("sayfa", sayfa_sayisi)
        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/imdb-top-250/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)


        ############################

    def komedi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/komedi-filmleri-izlee'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/komedi-filmleri-izlee'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/komedi-filmleri-izlee/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.
        print(girilen_film_adlari)
        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....\n")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        # filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False:  # bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else:  # yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        """
            bu kısım elimizdeki yorumlar değişkeninde commentlist değeri var mıdır onun kontrolü yapılır. üst kısım ile aynıdır aslında bu farklı bir yöntemdir. 

            degisken=yorumlar[0].get("class") #yorumlardaki class özelliğini alıyoruz. yorum olduğunda commentlist özelliği vardır.
            print("class değerleri",degisken)
            print(degisken[0])
            if degisken[0]=="commentlist": #yorum olduğunda commentlist özelliği olur. yorum varsa burası çalışır. yorum olmadığında commentlist olmadığı için burası çalışmaz.
                print("doğru bulundu")
        """

        ############################

    def kore_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/kore-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/kore-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/kore-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....\n")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        # filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False:  # bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else:  # yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        """
            bu kısım elimizdeki yorumlar değişkeninde commentlist değeri var mıdır onun kontrolü yapılır. üst kısım ile aynıdır aslında bu farklı bir yöntemdir. 

            degisken=yorumlar[0].get("class") #yorumlardaki class özelliğini alıyoruz. yorum olduğunda commentlist özelliği vardır.
            print("class değerleri",degisken)
            print(degisken[0])
            if degisken[0]=="commentlist": #yorum olduğunda commentlist özelliği olur. yorum varsa burası çalışır. yorum olmadığında commentlist olmadığı için burası çalışmaz.
                print("doğru bulundu")
        """

    def korku_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/korku-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/korku-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/korku-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def macera_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/macera-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/macera-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi",list)
        print("link adresinin son karakteri",list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi=[] #bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu",len(list))
        for i in range(1,len(list)):
            if list[-i]=="0" or list[-i]=="1" or list[-i]=="2" or list[-i]=="3" or list[-i]=="4" or list[-i]=="5" or list[-i]=="6" or list[-i]=="7" or list[-i]=="8" or list[-i]=="9" :
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak=[]
        for i in range(2,len(sayfa_sayisi_listesi)+1):#2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı",sayfa_sayisi_liste_olarak)
        sayfa_sayisi="".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi=int(sayfa_sayisi)
        print("sayfa",sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/macera-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

    def marvel_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/marvel-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/marvel-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/marvel-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def muzikal_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/muzikal-filmler'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/muzikal-filmler'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/muzikal-filmler/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def polisiye_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/polisiye-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/polisiye-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/polisiye-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def psikolojik_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/psikolojik-film-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/psikolojik-film-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/psikolojik-film-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)


        ############################

    def romantik_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/romantik-film'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/romantik-film'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/romantik-film/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(
                film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def savas_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/savas-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/savas-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        if bool(sonuc_duzgun.find_all("div",{"class":"wp-pagenavi"}))==False:
            sayfa_sayisi=0
        else:
            yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            print("yorumlar kısmı", yorumlar)
            print(type(yorumlar))
            list = []
            print(list)
            list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
            print("link adresi", list)
            print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
            sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
            print("list degerinin uzunluğu", len(list))
            for i in range(1, len(list)):
                if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                    sayfa_sayisi_listesi.append(list[-i])
            sayfa_sayisi_liste_olarak = []
            for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
                sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
            print(sayfa_sayisi_listesi)
            print("sayfa sayısı", sayfa_sayisi_liste_olarak)

            sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
            sayfa_sayisi = int(sayfa_sayisi)

            print("sayfa", sayfa_sayisi)

        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/savas-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def spor_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/spor-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/spor-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/spor-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(
                film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def suc_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/suc-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/suc-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []
        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/suc-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        ############################

    def tarih_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/tarih-filmleri-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/tarih-filmleri-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.
        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/tarih-filmleri-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)


        ############################

    def tavsiye_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/tavsiye-filmler-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/tavsiye-filmler-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/tavsiye-filmler-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.
            veri = list_sayfa_bir[0]
            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)


        ############################

    def turk_komedi_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/turk-komedi-filmleri'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/turk-komedi-filmleri'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []

        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/turk-komedi-filmleri/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.
            veri = list_sayfa_bir[0]
            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)


        ############################

    def western_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/western-film-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/western-film-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []
        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/western-film-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık
        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        #filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False: #bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else :#yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)



        ############################

    def yerli_filmleri(self):
        # bir sayfanın sayfa sayısı bulunmaya çalışılıyor. çünkü sonradan film eklense bile film sayfa değişse bile sürekli olarak çalışabilmesi, her filmi inceleyebilmek için sayfanın sürekli en son sayfaya kadar gidebilmei, incelenebilmesi gerekir.
        ana_sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/yerli-filmler-izle'
        sys = requests.get(ana_sayfa)
        soup = BeautifulSoup(sys.content, 'html.parser')
        sayfa_sayisi_gelen_veri = soup.find_all("div", {"class": "wp-pagenavi"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
        list_sayfa_bir = []
        for i in range(len(sayfa_sayisi_gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
            list_sayfa_bir.append(sayfa_sayisi_gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.

        sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/yerli-filmler-izle'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu
        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.
        yorumlar = sonuc_duzgun.find_all("a", {"class": "last"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.

        print("yorumlar kısmı", yorumlar)
        print(type(yorumlar))
        list = []
        list = yorumlar[0].get("href")  # burada elimizdeki bs4.element.ResultSet tipindeki değeri alıp  bundaki href değerini yani link değerini alıyoruz. çünkü link uzantısında sayfa numarası vardır. biz bu şelilde o sayfa değerine ulaşıp for içinde kullanırız.
        print("link adresi", list)
        print("link adresinin son karakteri", list[-1])  # elimizde link değeri vardır bu link değerindeki en son karakter alınır. bu biz sayfa numarasını verir.
        sayfa_sayisi_listesi = []  # bunu yapmamızdaki neden sitenin ekinde bulunan sayı tek haneli değilse bile çalışması için bir değerde tutulmalı.
        print("list degerinin uzunluğu", len(list))
        for i in range(1, len(list)):
            if list[-i] == "0" or list[-i] == "1" or list[-i] == "2" or list[-i] == "3" or list[-i] == "4" or list[-i] == "5" or list[-i] == "6" or list[-i] == "7" or list[-i] == "8" or list[-i] == "9":
                sayfa_sayisi_listesi.append(list[-i])
        sayfa_sayisi_liste_olarak = []
        for i in range(2, len(sayfa_sayisi_listesi) + 1):  # 2 den başlattık çünkü değer içerisinde 1 tane 2 var bu film sitesinin adının içindeki 2 dir. yani sayfa sayısı olmadığı için bunu alamayız. +1 dedik çünkü 2 den başlayacağı için bir eleman eksik girer bu da sayfa sayısında eksiklik demektir.
            sayfa_sayisi_liste_olarak.append(sayfa_sayisi_listesi[-i])
        print(sayfa_sayisi_listesi)
        print("sayfa sayısı", sayfa_sayisi_liste_olarak)
        sayfa_sayisi = "".join(sayfa_sayisi_liste_olarak)
        sayfa_sayisi = int(sayfa_sayisi)
        print("sayfa", sayfa_sayisi)
        film_adlari = []
        girilen_film_adlari = []
        # sayfalar arasında dolaşılan kısım
        sayfa_sayisi = sayfa_sayisi + 1  # sayfa_sayisi değerini 1 arttırdık çünkü for içinde 0 dan başlayıp tange içindeki değere kadar devam ediyordu. sayfamızın değeri mesela 7 ise 0,1,2,3,4,5,6 ya kadar gidiyordu.hem en son sayfayı göremiyorduk hem de 0 ve 1 aynı sayfaya karşılık geldiği için liste içinde iki defa aynı sayfa yazılıyordu.

        for i in range(1,sayfa_sayisi):  # 1 den başlattık çünkü kore-filmleri   ,  kore-filmleri/page/0  ve kore-filmleri/page/1 aynı sayfaya çıktığı için 1 den 7 ye kadar gittik(7 dahil değil) böyle yapmasaydık birinci sayfayı bir kaç kez ekler ve en son sayfayı eklemezdi.
            sayfa_sayisi = str(i)
            sayfa = 'https://www.hdfilmcehennemi2.pw/kategori/yerli-filmler-izle/page/' + sayfa_sayisi
            sys = requests.get(sayfa)
            soup = BeautifulSoup(sys.content, 'html.parser')
            gelen_veri = soup.find_all("div", {"class": "movief"})  # film adlarının bulunduğu tagı aldım. sadece filmin adını içeren bir kısım vardı bende onu alabilidim.
            list_sayfa_bir = []
            for i in range(len(gelen_veri)):  # elimizde bulunan film isimlerinin boyutu kadar dolaşsın.
                list_sayfa_bir.append(gelen_veri[i].text)  # listemizin içine var olan film adlarını ekledik.
            toplam = 0
            for i in range(len(list_sayfa_bir)):
                list_sayfa_bir[i] = list_sayfa_bir[i].lower()  # lower metodunun amacı içinde bulunduğu büyük harfli kelimeleri küçük harfe dönüştürmektir. böylece istediğimiz web sitesine gidebiliriz. çünkü orada her şey küçük harfle kodlanmış.

            veri = list_sayfa_bir[0]

            film_list_bir = []
            for i in range(len(list_sayfa_bir)):
                veri = list_sayfa_bir[i]
                for j in range(len(veri)):  # burada yapılan işlem her değeri parçalamak daha sonra da aralarına - işareti koymaktır.
                    sonuc = veri.split()  # elimizdeki değeri parçalamaya yarar. mesela parantez içine biz ,  dersek virgüllere göre parçalar ve liste içinde her parçalanan değer bir listenin elemanı olur.
                    veri = "-".join(sonuc)  # bu kullanımda ise liste içindeki elemanların arasına bu işareti koyar. bizimkilerde boşluk vardı. bunu kullanınca her elemanın kendi içinde olmak üzere arasına - işarei koyar.
                film_list_bir.append(veri)

            film_adlari.append(film_list_bir)  # film adlari - koulmş hali içeriri.  ve her sayfadaki - lenmiş halleri koyar ki bütün - olması gereken kısımlar tutulsun.
            girilen_film_adlari.append((list_sayfa_bir))  # her seferinde çekilen biilgilerden film isimlerini bir yerde tutmamız gerekirdi çünkü eğer böyle yapmazsak sürekli en son hangi değerleri aldıysak içinde de o değerler bulunurdu.
            # bu şekilde çekilen film adları bir yerde tutularak içerisindeki bilgiler değişmemiş oldu. Ve if li yapılarda kullanabildik.

        # film listesindeki izle kısmını/ekini kaldırdık. Böylece kullanıcı sadece filmin adını girerek yorumların sonucunu görebilecek.
        for m in range(len(girilen_film_adlari)):  # listedeki bütün bloklar kadar ilerler. 6 sayfa ise 6 defa ilerler.
            for j in range(len(girilen_film_adlari[m])):  # her blok içindeki değer kadar ilerler. Yani her sayfada kaç adet film varsa o kadar işleme alır.
                girilen_film_adlari[m][j] = girilen_film_adlari[m][j][:-5]  # ilk sayfanın ilk filmindeki, filmadı izle kısmı vardır. burada son5 harf/karakter silinir    biz de her film için izle ekini kaldırdık. böylece kullanıcı sadece film adını girdiğinde program çalışır.

        # girilen film adlari ve film adları kısmının farkı birinde - işareti yok birinde vardır. biri girilen degeri kontrol etmek için diğeri de link kısmına film sayfasına gitsin diye ekleme yapar.

        film_adi = input("lütfen küçük harfler ile filmin adını giriniz....\n")

        # dışardan girilen film adının hangisi olduğu tespit etmek ve link uzantısına eklemek için yazıldı.
        for m in range(len(girilen_film_adlari)):  # bütün listenin boyutu kadar dolaş yani sayfa sayısı kadar
            for i in range(len(girilen_film_adlari[m])):  # bütün sayfaların içindeki filmleri dolaş. yani girilen_film_adlari[m] dediğimizde m 0 a eşittir. o zaman biz demiş oluyoruz ki 0. sayfanın boyutu kadar dolaş yani 0. sayfanın içinde kaç tane  film varsa o kadar dolaş.
                if film_adi == girilen_film_adlari[m][i]:  # sayfalar içinde dolaşıp dışardan girilen film bulunana kadar dolaşır.
                    film_adimiz = film_adlari[m][i]  # bulunan filmin - konularak oluşturulan listedeki bilgi film_adimiz değişkenine atanır.
                    break;  # break dememizin nedeni mesela ilk sayfada filmi bulduysak gidip te bütün sayfaları dolaşmasın direk döngüden çıksın.

        # yorumların çekildiği kısım ve aşağıda yorumlama ile sonuca ulaşılan kısım.
        sayfa = 'https://www.hdfilmcehennemi2.pw/' + film_adimiz + '.html'
        veri = requests.get(sayfa)  # web sayfasındaki değeri alıp veri değişkenine atadık

        sonuc = veri.text  # elimizdeki bilgileri text haline getirdik yani bir metin halinde oldu

        sonuc_duzgun = BeautifulSoup(sonuc, 'html.parser')  # beautifulSoup nesnesine dönüştürdük.

        # filmin bulunduğu sayfaya gidip orada yorum yapıladıysa hata mesajı verir ve programdan çıkılır.yorum varsa da yorum inceleme için else blogu çalışır.
        if bool(sonuc_duzgun.find_all("ol", {"class": "commentlist"})) == False:  # bool yaptık çünkü false ile karşılaştırdık. burda yapılan işlem site içinde ol commentlist yani film hakkında yorum var mıdır? kontrolü yapar.
            print("Film için yorum bulunmamaktadır. İlginizi çektiyse izleyiniz.. \nProgramdan çıkılıyor...")

        else:  # yorum yapıldıysa çalışacak olan kısım..
            yorumlar = sonuc_duzgun.find_all("ol", {"class": "commentlist"})  # sayfadaki ol kısmını getirir. bu ol içinde yorum listesi bulunur. yani yorumun kapsandığı kısmı getirir.
            veri = yorumlar[0].text  # yorumun kapsandığı kısımdan text olan değerleri getirir. içinde yazılan tarihle birlikte yorum ve kimin yazdığı gibi bilgiler de bulunur.
            nesne = yorumlama()
            nesne.turkce_karakter_hatasi_var(sayfa, veri, film_adi)

        """
            bu kısım elimizdeki yorumlar değişkeninde commentlist değeri var mıdır onun kontrolü yapılır. üst kısım ile aynıdır aslında bu farklı bir yöntemdir. 

            degisken=yorumlar[0].get("class") #yorumlardaki class özelliğini alıyoruz. yorum olduğunda commentlist özelliği vardır.
            print("class değerleri",degisken)
            print(degisken[0])
            if degisken[0]=="commentlist": #yorum olduğunda commentlist özelliği olur. yorum varsa burası çalışır. yorum olmadığında commentlist olmadığı için burası çalışmaz.
                print("doğru bulundu")
        """


        ############################


class yorumlama():
    def turkce_karakter_hatasi_olmadan(self,sayfa, veri, film_adi):
        toplam_olumlu = 0
        toplam_olumsuz = 0

        veri=veri.lower()
        for i in range(len(veri)):  # film hakkında olumlu olabilecek kelimeleri içeriyorsa film hakkında olumlu yorum yapılmıştır.  #türkçe karakter kullanılınca çeviricide hata olabiliyor. o yüzden bunları da tanımlamak lazım. kod bunları görünce anlaması gerekir.
            if veri[i] == "f" and (veri[i + 1] == "i" or veri[i + 1] == "ı") and veri[i + 2] == "l" and veri[i + 3] == "m" and veri[i + 4] == " " and veri[i + 5] == "g" and (veri[i + 6] == "ü" or veri[i + 6] == "u")and veri[i + 7] == "z" and veri[i + 8] == "e" and veri[i + 9] == "l" and veri[i + 10] == "d" and (veri[i + 11] == "i" or veri[i + 11] == "ı"):  # film güzeldi
                toplam_olumlu += 1
            if veri[i] == "d" and (veri[i + 1] == "u" or veri[i + 1] == "ü") and veri[i + 2] == "y" and veri[i + 3] == "g" and veri[i + 4] == "u" and veri[i + 5] == "l" and veri[i + 6] == "a" and veri[i + 7] == "n" and veri[i + 8] == "d" and (veri[i + 9] == "ı" or veri[i + 9] == "i") and veri[i + 10] == "m":  # duygulandım
                toplam_olumlu += 1
            if (veri[i] == "g" or veri[i] == "ğ") and (veri[i + 1] == "ü" or veri[i + 1] == "u") and veri[i + 2] == "z" and veri[i + 3] == "e" and veri[i + 4] == "l" and veri[i + 5] == "d" and (veri[i + 6] == "i" or veri[i + 6] == "ı"):  # güzeldi
                toplam_olumlu += 1
            if veri[i] == "h" and veri[i + 1] == "a" and veri[i + 2] == "r" and (veri[i + 3] == "i" or veri[i + 3] == "ı") and veri[i + 4] == "k" and veri[i + 5] == "a":  # harika
                toplam_olumlu += 1
            if veri[i] == "m" and (veri[i + 1] == "u" or veri[i + 1] == "ü") and veri[i + 2] == "a" and veri[i + 3] == "z" and veri[i + 4] == "z" and veri[i + 5] == "a" and veri[i + 6] == "m":  # muazzam
                toplam_olumlu += 1
            if veri[i] == "m" and (veri[i + 1] == "u" or veri[i + 1] == "ü") and veri[i + 2] == "a" and veri[i + 3] == "z" and veri[i + 4] == "a" and veri[i + 5] == "m":  # muazam
                toplam_olumlu += 1
            if (veri[i] == "ç" or veri[i] == "c") and veri[i + 1] == "o" and veri[i + 2] == "k" and veri[i + 3] == " " and veri[i + 4] == "g" and (veri[i + 5] == "ü" or veri[i + 5] == "u") and veri[i + 6] == "z" and veri[i + 7] == "e" and veri[i + 8] == "l":  # çok güzel
                toplam_olumlu += 1
            if veri[i] == "e" and (veri[i + 1] == "ğ" or veri[i + 1] == "g") and veri[i + 2] == "l" and veri[i + 3] == "e" and veri[i + 4] == "n" and veri[i + 5] == "c" and veri[i + 6] == "e" and veri[i + 7] == "l" and (veri[i + 8] == "i" or veri[i + 8] == "ı"):  # eğlenceli
                toplam_olumlu += 1
            if (veri[i] == "s" or veri[i] == "ş") and (veri[i + 1] == "i" or veri[i + 1] == "ı") and (veri[i + 2] == "i" or veri[i + 2] == "ı") and veri[i + 3] == "r":  # siir
                toplam_olumlu += 1
            if veri[i] == "f" and (veri[i + 1] == "i" or veri[i + 1] == "ı") and veri[i + 2] == "l" and veri[i + 3] == "m" and veri[i + 4] == " " and (veri[i + 5] == "g" or veri[i + 5] == "ğ") and (veri[i + 6] == "u" or veri[i + 6] == "ü") and veri[i + 7] == "z" and veri[i + 8] == "e" and veri[i + 9] == "l":  # film guzel
                toplam_olumlu += 1
            if veri[i] == "f" and (veri[i + 1] == "i" or veri[i + 1] == "ı") and veri[i + 2] == "l" and veri[i + 3] == "m" and veri[i + 4] == " " and veri[i + 5] == "g" and (veri[i + 6] == "u" or veri[i + 6] == "ü") and veri[i + 7] == "z" and veri[i + 8] == "e" and veri[i + 9] == "l" and veri[i + 10] == "d" and (veri[i + 11] == "i" or veri[i + 11] == "ı"):  # film guzeldi
                toplam_olumlu += 1
            if (veri[i] == "g" or veri[i] == "ğ") and (veri[i + 1] == "ü" or veri[i + 1] == "u") and veri[i + 2] == "z" and veri[i + 3] == "e" and veri[i + 4] == "l" and veri[i + 5] == " " and veri[i + 6] == "f" and (veri[i + 7] == "i" or veri[i + 7] == "ı") and veri[i + 8] == "m":  # güzel film
                toplam_olumlu += 1
            if veri[i] == "t" and veri[i + 1] == "e" and (veri[i + 2] == "ş" or veri[i + 2] == "s") and veri[i + 3] == "e" and veri[i + 4] == "k" and veri[i + 5] == "k" and (veri[i + 6] == "ü" or veri[i + 6] == "u") and veri[i + 7] == "r":  # teşekkür
                toplam_olumlu += 1
            if veri[i] == "t" and veri[i + 1] == "e" and (veri[i + 2] == "ş" or veri[i + 2] == "s") and veri[i + 3] == "e" and veri[i + 4] == "k" and (veri[i + 5] == "ü" or veri[i + 5] == "u") and veri[i + 6] == "r":  # teşekür
                toplam_olumlu += 1
            if veri[i] == "d" and veri[i + 1] == "e" and veri[i + 2] == "r" and veri[i + 3] == "s" and veri[i + 4] == " " and veri[i + 5] == "v" and veri[i + 6] == "e" and veri[i + 7] == "r" and (veri[i + 8] == "i" or veri[i + 8] == "ı") and veri[i + 9] == "c" and (veri[i + 10] == "i" or veri[i + 10] == "ı"):  # ders verici
                toplam_olumlu += 1

            # olumsuz kelimelerin tespiti:

            if veri[i] == "b" and veri[i + 1] == "e" and (veri[i + 2] == "ğ" or veri[i + 2] == "g") and veri[i + 3] == "e" and veri[i + 4] == "n" and veri[i + 5] == "m" and veri[i + 6] == "e" and veri[i + 7] == "d" and (veri[i + 8] == "i" or veri[i + 8] == "ı") and veri[i + 9] == "m":  # beğenmedim
                toplam_olumsuz += 1
            if veri[i] == "k" and (veri[i + 1] == "ö" or veri[i + 1] == "o") and veri[i + 2] == "t" and (veri[i + 3] == "ü" or veri[i + 3] == "u"):  # kötü
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "e" and veri[i + 2] == "r" and veri[i + 3] == "b" and veri[i + 4] == "a" and veri[i + 5] == "t":  # berbat
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "a" and veri[i + 2] == "k" and veri[i + 3] == "a" and veri[i + 4] == "m" and veri[i + 5] == "a" and veri[i + 6] == "d" and (veri[i + 7] == "ı" or veri[i + 7] == "i") and veri[i + 8] == "m":  # bakamadım
                toplam_olumsuz += 1
            if (veri[i] == "ı" or veri[i] == "i") and veri[i + 1] == "z" and veri[i + 2] == "l" and veri[i + 3] == "e" and veri[i + 4] == "y" and veri[i + 5] == "e" and veri[i + 6] == "m" and veri[i + 7] == "e" and veri[i + 8] == "d" and (veri[i + 9] == "i" or veri[i + 9] == "ı") and veri[i + 10] == "m":  # izleyemedim
                toplam_olumsuz += 1
            if veri[i] == "s" and (veri[i + 1] == "ı" or veri[i + 1] == "i") and veri[i + 2] == "k" and (veri[i + 3] == "i" or veri[i + 3] == "ı") and veri[i + 4] == "c" and (veri[i + 5] == "ı" or veri[i + 5] == "i"):  # sıkicı
                toplam_olumsuz += 1
            if (veri[i] == "g" or veri[i] == "ğ") and (veri[i + 1] == "u" or veri[i + 1] == "ü") and veri[i + 2] == "z" and veri[i + 3] == "e" and veri[i + 4] == "l" and veri[i + 5] == " " and veri[i + 6] == "d" and veri[i + 7] == "e" and (veri[i + 8] == "g" or veri[i + 8] == "ğ") and (veri[i + 9] == "ı" or veri[i + 9] == "i") and veri[i + 10] == "l":  # guzel degıl
                toplam_olumsuz += 1
            if (veri[i] == "ı" or veri[i] == "i") and (veri[i + 1] == "ç" or veri[i + 1] == "c") and (veri[i + 2] == "i" or veri[i + 2] == "ı") and veri[i + 3] == "m" and veri[i + 4] == " " and (veri[i + 5] == "ş" or veri[i + 5] == "s") and (veri[i + 6] == "i" or veri[i + 6] == "ı") and (veri[i + 7] == "ş" or veri[i + 7] == "s") and veri[i + 8] == "t" and (veri[i + 9] == "i" or veri[i + 9] == "ı"):  # içim şişti
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "e" and veri[i + 2] == "l" and veri[i + 3] == "a" and (veri[i + 4] == "s" or veri[i + 4] == "ş") and (veri[i + 5] == "ı" or veri[i + 5] == "i") and veri[i + 6] == "n" and (veri[i + 7] == "ı" or veri[i + 7] == "i") and veri[i + 8] == " " and veri[i + 9] == "v" and veri[i + 10] == "e" and veri[i + 11] == "r" and veri[i + 12] == "s" and (veri[i + 13] == "i" or veri[i + 13] == "ı") and veri[i + 14] == "n":  # belasını versin
                toplam_olumsuz += 1

        print("olumsuz yorumların sayısı:", toplam_olumsuz)
        print("olumlu yorumların saysı", toplam_olumlu)

        dosyaya_yazma = open("C:\\Users\\Asus\\PycharmProjects\\yapay_zeka_staj_projesi\\dosyaya_yazma.txt", "a")
        toplam_olumsuz = str(toplam_olumsuz)
        toplam_olumlu = str(toplam_olumlu)
        if toplam_olumlu == toplam_olumsuz:
            sonucumuz = "film adı: " + film_adi + "\ntoplam olumsuz yorum sayısı=" + toplam_olumsuz + "\ntoplam olumlu yorum sayısı=" + toplam_olumlu + "\ntaviseye olarak= Değerler eşit bir şans verilebilir.\n\n"
            dosyaya_yazma.write(sonucumuz)  # encode kısmı eklemedir.
        if toplam_olumlu < toplam_olumsuz:
            sonucumuz = "film adı=" + film_adi + "\ntoplam olumsuz yorum sayısı=" + toplam_olumsuz + "\ntoplam olumlu yorum sayısı" + toplam_olumlu + "\ntaviseye olarak=" + "izlemesen daha iyi\n\n"
            dosyaya_yazma.write(sonucumuz)
        if toplam_olumlu > toplam_olumsuz:
            sonucumuz = "film adı=" + film_adi + "\ntoplam olumlu yorum saysı=" + "\ntoplam olumsuz yorum sayısı=" + toplam_olumsuz + "\ntoplam olumlu yorum sayısı=" + toplam_olumlu + "\ntaviseye olarak=" + "izlenebilir\n\n"
            dosyaya_yazma.write(sonucumuz)

        dosyaya_yazma.close()  # açılan dosya işlem bittikten sonra kapatılıyor ki bellekte yer kaplamasın.
        print("filmin link adresi=", sayfa)  # hangi filmin yorumunu merak ediyorsak o filme ait web sitesi
        """

        HARF TANIMLAMA YERİ: BU PROGRAMDA EKSİK OLAN ŞEY ALINAN VERİYİ TÜRKÇE KARAKTERLERE DÖNÜŞTÜREMİYOR.

        Ã¶ =ö
        Å=ş
        Ã¼=ü
        Ä±=ı
        Ã§=ç
        Ä=ğ


        """


    def turkce_karakter_hatasi_var(self,sayfa, veri, film_adi):
        toplam_olumlu = 0
        toplam_olumsuz = 0

        """
                Ã¶ =ö
                Å=ş
                Ã¼=ü
                Ä±=ı
                Ã§=ç
                Ä=ğ

        """

        for i in range(len(veri)):
            if veri[i]=="Å" and veri[i+1]=="":
                veri=veri.replace("Å","s ") #replace ile bu değere ait bilgiler "s " ile değiştirildi. bu maketrans ve trasnlate ile aslında aynı işlevdedir. ama orada bazı noktalarda atama kısmında özellikle hata olduğu için
                #replace kullanımını seçtim.

            if veri[i]=="Ä" and veri[i+1]=="":
                veri = veri.replace("Ä","g ")

            if veri[i]=="Ã" and veri[i+1]=="¶":
                veri = veri.replace("Ã¶","o ")

            if veri[i]=="Ã" and veri[i+1]=="¼":
                veri = veri.replace("Ã¼","u ")

            if veri[i]=="Ä" and veri[i+1]=="±":
                veri = veri.replace("Ä±","i ")

            if veri[i]=="Ã" and veri[i+1]=="§":
                veri = veri.replace("Ã§","c ")

        # elimizdeki yorumları küçük harflere dönüştürdük ki hem karşılaştırma yaparken hem de aşağıda replace yaparken var olan olasılıkları azaltmaktı yani teşekkür kelimesinde büyük küçük için birden fazla olasılığı içeren replace kodu azaltmaktı.
        veri=veri.lower()

        #olasılıksal olarak fazla seçeneğin kontrol edildiği ve değiştirildiği kısım. aşağıdaki if kısımları ise bunların işlenmesi sonucu ortaya çıkan kelimeleri yakalamaya çalışan kısımdır.
        veri=veri.replace("tes ekku rler","tesekkurler")
        veri = veri.replace("tesekku rler", "tesekkurler")
        veri = veri.replace("tes ekkurler", "tesekkurler")
        veri=veri.replace("beg endim","begendim")
        veri = veri.replace("beg endi m", "begendim")
        veri = veri.replace("begendi m", "begendim")
        veri = veri.replace("eg lenceliydi", "eglenceliydi")
        veri = veri.replace("eg lenceli ydi", "eglenceliydi")
        veri = veri.replace("eglenceli ydi", "eglenceliydi")
        veri = veri.replace("gu zeldi", "guzeldi")
        veri = veri.replace("hari ka", "harika")
        veri = veri.replace("fi lm gu zel", "film guzel")
        veri = veri.replace("film gu zel", "film guzel")
        veri = veri.replace("fi lm guzel", "film guzel")
        veri = veri.replace("duygulandi m", "duygulandim")
        veri = veri.replace("c ok gu zel", "cok guzel")
        veri = veri.replace("c ok guzel", "cok guzel")
        veri = veri.replace("cok gu zel", "cok guzel")
        veri = veri.replace("sii r", "siir")
        veri = veri.replace("si ir", "siir")
        veri = veri.replace("si i r", "siir")
        veri = veri.replace("s iir", "siir")
        veri = veri.replace("s ii r", "siir")
        veri = veri.replace("s i ir", "siir")
        veri = veri.replace("s i i r", "siir")
        veri = veri.replace("fi lm guzeldi", "film guzeldi")
        veri = veri.replace("fi lm gu zeldi", "film guzeldi")
        veri = veri.replace("film gu zeldi", "film guzeldi")
        veri = veri.replace("gu zel film", "guzel film")
        veri = veri.replace("gu zel fi lm", "guzel film")
        veri = veri.replace("guzel fi lm", "guzel film")
        veri = veri.replace("tes ekkur", "tesekkur")
        veri = veri.replace("tes ekku r", "tesekkur")
        veri = veri.replace("tesekku r", "tesekkur")
        veri = veri.replace("tesekur", "tesekur")
        veri = veri.replace("ders veri ci", "ders verici")
        veri = veri.replace("ders veri ci ", "ders verici")
        veri = veri.replace("ders verici ", "ders verici")
        veri = veri.replace("muhtes em", "muhtesem")
        veri = veri.replace("mu htes em", "muhtesem")
        veri = veri.replace("mu htesem", "muhtesem")
        veri = veri.replace("tavsi ye ederim ", "tavsiye ederim")
        veri = veri.replace("tavsi ye ederi m ", "tavsiye ederim")
        veri = veri.replace("adamlar yapmi s", "adamlar yapmis")
        veri = veri.replace("adamlar yapmi s ", "adamlar yapmis")
        veri = veri.replace("adamlar yapmis ", "adamlar yapmis")
        veri = veri.replace("cok iyi ydi", "cok iyiydi")
        veri = veri.replace("cok i yiydi", "cok iyiydi")
        veri = veri.replace("cok i yi ydi", "cok iyiydi")
        veri = veri.replace("c ok iyiydi", "cok iyiydi")
        veri = veri.replace("c ok iyi ydi", "cok iyiydi")
        veri = veri.replace("c ok i yiydi", "cok iyiydi")
        veri = veri.replace("c ok i yi ydi", "cok iyiydi")
        veri = veri.replace("i yi ydi", "iyiydi")
        veri = veri.replace("iyi ydi", "iyiydi")
        veri = veri.replace("i yiydi", "iyiydi")
        veri = veri.replace("cok iyi di", "cok iyiydi")
        veri = veri.replace("cok i yidi", "cok iyiydi")
        veri = veri.replace("cok i yi di", "cok iyiydi")
        veri = veri.replace("c ok iyidi", "cok iyiydi")
        veri = veri.replace("c ok iyi di", "cok iyiydi")
        veri = veri.replace("c ok i yidi", "cok iyiydi")
        veri = veri.replace("c ok i yi di", "cok iyiydi")
        veri = veri.replace("izlenmeye deg er", "izlenmeye deger")
        veri = veri.replace("i zlenmeye deg er", "izlenmeye deger")
        veri = veri.replace("i zlenmeye deger", "izlenmeye deger")
        veri = veri.replace("izlemeye deg er", "izlenmeye deger")
        veri = veri.replace("i zlemeye deg er", "izlenmeye deger")
        veri = veri.replace("i zlemeye deger", "izlenmeye deger")
        veri = veri.replace("o n numara", "on numara")
        veri = veri.replace("mahvo ldum", "mahvoldum")
        veri = veri.replace("mahvo ldu m", "mahvoldum")
        veri = veri.replace("mahvoldu m", "mahvoldum")
        veri = veri.replace("su per", "super")
        veri = veri.replace("izleyi n", "izleyin")
        veri = veri.replace("i zleyin", "izleyin")
        veri = veri.replace("i zleyi n", "izleyin")


        #olumsuz kelimelerin dönüşümü
        veri = veri.replace("beg enmedim", "begenmedim")
        veri = veri.replace("beg enmedi m", "begenmedim")
        veri = veri.replace("begenmedi m", "begenmedim")
        veri = veri.replace("ko tu", "kotu")
        veri = veri.replace("bakamadi m", "bakamadim")
        veri = veri.replace("i zleyemedim", "izleyemedim")
        veri = veri.replace("i zleyemedi m", "izleyemedim")
        veri = veri.replace("izleyemedi m", "izleyemedim")
        veri = veri.replace("siki ci", "sikici")
        veri = veri.replace("si ki ci", "sikici")
        veri = veri.replace("si kici", "sikici")
        veri = veri.replace("guzel degi l", "guzel degil")
        veri = veri.replace("guzel deg il", "guzel degil")
        veri = veri.replace("guzel deg i l", "guzel degil")
        veri = veri.replace("gu zel degil", "guzel degil")
        veri = veri.replace("gu zel degi l", "guzel degil")
        veri = veri.replace("gu zel deg il", "guzel degil")
        veri = veri.replace("gu zel deg i l", "guzel degil")
        veri = veri.replace("ic im s is ti", "icim sisti") #aslında bundan 64 tane olmalı her ihtimali kapsamalı ama biz sadece kullanımı doğru olanı yazdık.
        veri = veri.replace("belasini versi n", "belasini versin")
        veri = veri.replace("belasini  versin", "belasini versin")
        veri = veri.replace("belasini  versi n", "belasini versin")
        veri = veri.replace("belasi ni versin", "belasini versin")
        veri = veri.replace("belasi ni versi n", "belasini versin")
        veri = veri.replace("belasi ni  versin", "belasini versin")
        veri = veri.replace("belasi ni  versi n", "belasini versin")
        veri = veri.replace("bos bir fi lm", "bos bir film")
        veri = veri.replace("bos bi r film", "bos bir film")
        veri = veri.replace("bos bi r fi lm", "bos bir film")
        veri = veri.replace("bos  bir film", "bos bir film")
        veri = veri.replace("bos  bir fi lm", "bos bir film")
        veri = veri.replace("bos  bi r film", "bos bir film")
        veri = veri.replace("bos  bi r fi lm", "bos bir film")
        veri = veri.replace("bos fi lm", "bos film")
        veri = veri.replace("bos  film", "bos film")
        veri = veri.replace("bos  fi lm", "bos film")
        veri = veri.replace("film bos ", "film bos")
        veri = veri.replace("fi lm bos", "film bos")
        veri = veri.replace("fi lm bos ", "film bos")
        veri = veri.replace("saatimi yedini z", "saatimi yediniz")
        veri = veri.replace("saatimi yedi niz", "saatimi yediniz")
        veri = veri.replace("saatimi yedi ni z", "saatimi yediniz")
        veri = veri.replace("saatimi  yediniz", "saatimi yediniz")
        veri = veri.replace("saatimi  yedini z", "saatimi yediniz")
        veri = veri.replace("saatimi  yedi niz", "saatimi yediniz")
        veri = veri.replace("saatimi  yedi ni z", "saatimi yediniz")
        veri = veri.replace("saati mi yediniz", "saatimi yediniz")
        veri = veri.replace("saati mi yedini z", "saatimi yediniz")
        veri = veri.replace("saati mi yedi niz", "saatimi yediniz")
        veri = veri.replace("saati mi yedi ni z", "saatimi yediniz")
        veri = veri.replace("saati mi  yediniz", "saatimi yediniz")
        veri = veri.replace("saati mi  yedini z", "saatimi yediniz")
        veri = veri.replace("saati mi  yedi niz", "saatimi yediniz")
        veri = veri.replace("saati mi  yedi ni z", "saatimi yediniz")
        veri = veri.replace("satimi yediniz", "saatimi yediniz")
        veri = veri.replace("satimi yedini z", "saatimi yediniz")
        veri = veri.replace("satimi yedi niz", "saatimi yediniz")
        veri = veri.replace("satimi yedi ni z", "saatimi yediniz")
        veri = veri.replace("satimi  yediniz", "saatimi yediniz")
        veri = veri.replace("satimi  yedini z", "saatimi yediniz")
        veri = veri.replace("satimi  yedi niz", "saatimi yediniz")
        veri = veri.replace("satimi  yedi ni z", "saatimi yediniz")
        veri = veri.replace("sati mi yediniz", "saatimi yediniz")
        veri = veri.replace("sati mi yedini z", "saatimi yediniz")
        veri = veri.replace("sati mi yedi niz", "saatimi yediniz")
        veri = veri.replace("sati mi yedi ni z", "saatimi yediniz")
        veri = veri.replace("sati mi  yediniz", "saatimi yediniz")
        veri = veri.replace("sati mi  yedini z", "saatimi yediniz")
        veri = veri.replace("sati mi  yedi niz", "saatimi yediniz")
        veri = veri.replace("sati mi  yedi ni z", "saatimi yediniz")
        veri = veri.replace("saki n izleme", "sakin izleme")
        veri = veri.replace("saki n i zleme", "sakin izleme")
        veri = veri.replace("sakin i zleme", "sakin izleme")
        veri = veri.replace("tavsi ye etmem", "tavsiye etmem")



        print(veri)
        for i in range(len(veri)):  # film hakkında olumlu olabilecek kelimeleri içeriyorsa film hakkında olumlu yorum yapılmıştır.  #türkçe karakter kullanılınca çeviricide hata olabiliyor. o yüzden bunları da tanımlamak lazım. kod bunları görünce anlaması gerekir.
            if veri[i] == "b" and veri[i + 1] == "e" and veri[i + 2] == "g" and veri[i + 3] == "e" and veri[i + 4] == "n" and veri[i + 5] == "d" and veri[i + 6] == "i" and veri[i + 7] == "m":  # begendim
                toplam_olumlu += 1
            if veri[i] == "d" and veri[i + 1] == "u" and veri[i + 2] == "y" and veri[i + 3] == "g" and veri[i + 4] == "u" and veri[i + 5] == "l" and veri[i + 6] == "a" and veri[i + 7] == "n" and veri[i + 8] == "d" and veri[i + 9] == "i" and veri[i + 10] == "m":  # duygulandim
                toplam_olumlu += 1
            if veri[i] == "h" and veri[i + 1] == "a" and veri[i + 2] == "r" and veri[i + 3] == "i" and veri[i + 4] == "k" and veri[i + 5] == "a":  # harika
                toplam_olumlu += 1
            if veri[i] == "m" and veri[i + 1] == "u" and veri[i + 2] == "a" and veri[i + 3] == "z" and veri[i + 4] == "z" and veri[i + 5] == "a" and veri[i + 6] == "m":  # muazzam
                toplam_olumlu += 1
            if veri[i] == "m" and veri[i + 1] == "u" and veri[i + 2] == "a" and veri[i + 3] == "z" and veri[i + 4] == "a" and veri[i + 5] == "m":  # muazam
                toplam_olumlu += 1
            if veri[i] == "e" and veri[i + 1] == "g" and veri[i + 2] == "l" and veri[i + 3] == "e" and veri[i + 4] == "n" and veri[i + 5] == "c" and veri[i + 6] == "e" and veri[i + 7] == "l" and veri[i + 8] == "i":  # eglenceli
                toplam_olumlu += 1
            if veri[i] == "s" and veri[i + 1] == "i" and veri[i + 2] == "i" and veri[i + 3] == "r":  # siir
                toplam_olumlu += 1
            if veri[i] == "f" and veri[i + 1] == "i" and veri[i + 2] == "l" and veri[i + 3] == "m" and veri[i + 4] == " " and veri[i + 5] == "g" and veri[i + 6] == "u" and veri[i + 7] == "z" and veri[i + 8] == "e" and veri[i + 9] == "l":  # film guzel
                toplam_olumlu += 1
            if veri[i] == "f" and veri[i + 1] == "i" and veri[i + 2] == "l" and veri[i + 3] == "m" and veri[i + 4] == " " and veri[i + 5] == "g" and veri[i + 6] == "u" and veri[i + 7] == "z" and veri[i + 8] == "e" and veri[i + 9] == "l" and veri[i + 10] == "d" and veri[i + 11] == "i":  # film guzeldi
                toplam_olumlu += 1
            if veri[i] == "c" and veri[i + 1] == "o" and veri[i + 2] == "k" and veri[i + 3] == " " and veri[i + 4] == "g" and veri[i + 5] == "u" and veri[i + 6] == "z" and veri[i + 7] == "e" and veri[i + 8] == "l":  # cok guzel
                toplam_olumlu += 1
            if veri[i] == "g" and veri[i + 1] == "u" and veri[i + 2] == "z" and veri[i + 3] == "e" and veri[i + 4] == "l" and veri[i + 5] == "d" and veri[i + 6] == "i":  # guzeldi
                toplam_olumlu += 1
            if veri[i] == "g" and veri[i + 1] == "u" and veri[i + 2] == "z" and veri[i + 3] == "e" and veri[i + 4] == "l" and veri[i + 5] == " " and veri[i + 6] == "f" and veri[i + 7] == "i" and veri[i + 8] == "m":  # guzel film
                toplam_olumlu += 1
            if veri[i] == "t" and veri[i + 1] == "e" and veri[i + 2] == "s" and veri[i + 3] == "e" and veri[i + 4] == "k" and veri[i + 5] == "k" and veri[i + 6] == "u" and veri[i + 7] == "r":  # tesekkur
                toplam_olumlu += 1
            if veri[i] == "t" and veri[i + 1] == "e" and veri[i + 2] == "s" and veri[i + 3] == "e" and veri[i + 4] == "k" and veri[i + 5] == "u" and veri[i + 6] == "r":  # tesekur
                toplam_olumlu += 1
            if veri[i] == "d" and veri[i + 1] == "e" and veri[i + 2] == "r" and veri[i + 3] == "s" and veri[i + 4] == " " and veri[i + 5] == "v" and veri[i + 6] == "e" and veri[i + 7] == "r" and veri[i + 8] == "i" and veri[i + 9] == "c" and veri[i + 10] == "i":  # ders verici
                toplam_olumlu += 1
            if veri[i] == "e" and veri[i + 1] == "f" and veri[i + 2] == "s" and veri[i + 3] == "a" and veri[i + 4] == "n" and veri[i + 5] == "e":  # efsane
                toplam_olumlu += 1
            if veri[i] == "i" and veri[i + 1] == "z" and veri[i + 2] == "l" and veri[i + 3] == "e" and veri[i + 4] == "y" and veri[i + 5] == "i" and veri[i + 5] == "n":  # izleyin
                toplam_olumlu += 1
            if veri[i] == "s" and veri[i + 1] == "u" and veri[i + 2] == "p" and veri[i + 3] == "e" and veri[i + 4] == "r":  #super
                toplam_olumlu += 1
            if veri[i] == "m" and veri[i + 1] == "a" and veri[i + 2] == "h" and veri[i + 3] == "v" and veri[i + 4] == "o" and veri[i + 5] == "l" and veri[i + 6] == "d" and veri[i + 7] == "u" and veri[i + 8] == "m":  # mahvoldum
                toplam_olumlu += 1
            if veri[i] == "o" and veri[i + 1] == "n" and veri[i + 2] == " " and veri[i + 3] == "n" and veri[i + 4] == "u" and veri[i + 5] == "m" and veri[i + 6] == "a" and veri[i + 7] == "r" and veri[i + 8] == "a":  # on numara
                toplam_olumlu += 1
            if veri[i] == "m" and veri[i + 1] == "u" and veri[i + 2] == "h" and veri[i + 3] == "t" and veri[i + 4] == "e" and veri[i + 5] == "s" and veri[i + 6] == "e" and veri[i + 7] == "m":  # muhtesem
                toplam_olumlu += 1
            if veri[i] == "t" and veri[i + 1] == "a" and veri[i + 2] == "v" and veri[i + 3] == "s" and veri[i + 4] == "i" and veri[i + 5] == "y" and veri[i + 6] == "e" and veri[i + 7] == " " and veri[i + 8] == "e" and veri[i + 9] == "d" and veri[i + 10] == "e" and veri[i + 11] == "r" and veri[i + 12] == "i" and veri[i + 13] == "m":  # tavsiye ederim
                toplam_olumlu += 1
            if veri[i] == "a" and veri[i + 1] == "d" and veri[i + 2] == "a" and veri[i + 3] == "m" and veri[i + 4] == "l" and veri[i + 5] == "a" and veri[i + 6] == "r" and veri[i + 7] == " " and veri[i + 8] == "y" and veri[i + 9] == "a" and veri[i + 10] == "p" and veri[i + 11] == "m" and veri[i + 12] == "i" and veri[i + 13] == "s":  # adamlar yapmis
                toplam_olumlu += 1
            if veri[i] == "c" and veri[i + 1] == "o" and veri[i + 2] == "k" and veri[i + 3] == " " and veri[i + 4] == "i" and veri[i + 5] == "y" and veri[i + 6] == "i" and veri[i + 7] == "y" and veri[i + 8] == "d" and veri[i + 9] == "i":  # cok iyiydi ve cok iyidi yorumlarını aynı şekilde komtrol eder.
                toplam_olumlu += 1
            if veri[i] == "i" and veri[i + 1] == "z" and veri[i + 2] == "l" and veri[i + 3] == "e" and veri[i + 4] == "n" and veri[i + 5] == "m" and veri[i + 6] == "e" and veri[i + 7] == "y" and veri[i + 8] == "e" and veri[i + 9] == " " and veri[i] == "d" and veri[i + 1] == "e" and veri[i + 2] == "g" and veri[i + 3] == "e" and veri[i + 4] == "r":  # izlenmeye deger ve izlemeye deger kısımlarını içerir.
                toplam_olumlu += 1



            # olumsuz kelimelerin tespiti:


            if veri[i] == "b" and veri[i + 1] == "e" and veri[i + 2] == "g" and veri[i + 3] == "e" and veri[i + 4] == "n" and veri[i + 5] == "m" and veri[i + 6] == "e" and veri[i + 7] == "d" and veri[i + 8] == "i" and veri[i + 9] == "m":  # begenmedim
                toplam_olumsuz += 1
            if veri[i] == "k" and veri[i + 1] == "o" and veri[i + 2] == "t" and veri[i + 3] == "u":  # kotu
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "e" and veri[i + 2] == "r" and veri[i + 3] == "b" and veri[i + 4] == "a" and veri[i + 5] == "t":  # berbat
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "a" and veri[i + 2] == "k" and veri[i + 3] == "a" and veri[i + 4] == "m" and veri[i + 5] == "a" and veri[i + 6] == "d" and veri[i + 7] == "i" and veri[i + 8] == "m":  # bakamadim
                toplam_olumsuz += 1
            if veri[i] == "i" and veri[i + 1] == "z" and veri[i + 2] == "l" and veri[i + 3] == "e" and veri[i + 4] == "y" and veri[i + 5] == "e" and veri[i + 6] == "m" and veri[i + 7] == "e" and veri[i + 8] == "d" and veri[i + 9] == "i" and veri[i + 10] == "m":  # izleyemedim
                toplam_olumsuz += 1
            if veri[i] == "s" and veri[i + 1] == "i" and veri[i + 2] == "k" and veri[i + 3] == "i" and veri[i + 4] == "c" and veri[i + 5] == "i":  # sikici
                toplam_olumsuz += 1
            if veri[i] == "g" and veri[i + 1] == "u" and veri[i + 2] == "z" and veri[i + 3] == "e" and veri[i + 4] == "l" and veri[i + 5] == " " and veri[i + 6] == "d" and veri[i + 7] == "e" and veri[i + 8] == "g" and veri[i + 9] == "i" and veri[i + 10] == "l":  # guzel degil
                toplam_olumsuz += 1
            if veri[i] == "i" and veri[i + 1] == "c" and veri[i + 2] == "i" and veri[i + 3] == "m" and veri[i + 4] == " " and veri[i + 5] == "s" and veri[i + 6] == "i" and veri[i + 7] == "s" and veri[i + 8] == "t" and veri[i + 9] == "i":  # icim sisti
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "e" and veri[i + 2] == "l" and veri[i + 3] == "a" and veri[i + 4] == "s" and veri[i + 5] == "i" and veri[i + 6] == "n" and veri[i + 7] == "i" and veri[i + 8] == " " and veri[i + 9] == "v" and veri[i + 10] == "e" and veri[i + 11] == "r" and veri[i + 12] == "s" and veri[i + 13] == "i" and veri[i + 14] == "n":  # belasini versin
                toplam_olumsuz += 1
            if veri[i] == "s" and veri[i + 1] == "a" and veri[i + 2] == "a" and veri[i + 3] == "t" and veri[i + 4] == "i" and veri[i + 5] == "m" and veri[i + 6] == "i" and veri[i + 7] == " " and veri[i + 8] == "y" and veri[i + 9] == "e" and veri[i + 10] == "d" and veri[i + 11] == "i" and veri[i + 12] == "n" and veri[i + 13] == "i" and veri[i + 14] == "z":  # saatimi yediniz
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "o" and veri[i + 2] == "s" and veri[i + 3] == " " and veri[i + 4] == "b" and veri[i + 5] == "i" and veri[i + 6] == "r" and veri[i + 7] == " " and veri[i + 8] == "f" and veri[i + 9] == "i" and veri[i + 10] == "l" and veri[i + 11] == "m":  # bos bir film
                toplam_olumsuz += 1
            if veri[i] == "b" and veri[i + 1] == "o" and veri[i + 2] == "s" and veri[i + 3] == " " and veri[i + 4] == "f" and veri[i + 5] == "i" and veri[i + 6] == "l" and veri[i + 7] == "m":  # bos film
                toplam_olumsuz += 1
            if veri[i] == "f" and veri[i + 1] == "i" and veri[i + 2] == "l" and veri[i + 3] == "m" and veri[i + 4] == " " and veri[i + 5] == "b" and veri[i + 6] == "o" and veri[i + 7] == "s":  # film bos
                toplam_olumsuz += 1
            if veri[i] == "t" and veri[i + 1] == "a" and veri[i + 2] == "v" and veri[i + 3] == "s" and veri[i + 4] == "i" and veri[i + 5] == "y" and veri[i + 6] == "e" and veri[i + 7] == " " and veri[i+8] == "e" and veri[i + 9] == "t" and veri[i + 10] == "m" and veri[i + 11] == "e" and veri[i + 12] == "m":  # tavsiye etmem
                toplam_olumsuz += 1

        print("olumsuz yorumların sayısı:", toplam_olumsuz)
        print("olumlu yorumların saysı", toplam_olumlu)

        dosyaya_yazma = open("C:\\Users\\Asus\\PycharmProjects\\yapay_zeka_staj_projesi\\dosyaya_yazma.txt", "a")
        toplam_olumsuz = str(toplam_olumsuz)
        toplam_olumlu = str(toplam_olumlu)
        if toplam_olumlu == toplam_olumsuz:
            sonucumuz = "film adı: " + film_adi + "\ntoplam olumsuz yorum sayısı=" + toplam_olumsuz + "\ntoplam olumlu yorum sayısı=" + toplam_olumlu + "\ntaviseye olarak= Değerler eşit bir şans verilebilir.\n\n"
            dosyaya_yazma.write(sonucumuz)  # encode kısmı eklemedir.
        if toplam_olumlu < toplam_olumsuz:
            sonucumuz = "film adı=" + film_adi + "\ntoplam olumsuz yorum sayısı=" + toplam_olumsuz + "\ntoplam olumlu yorum sayısı" + toplam_olumlu + "\ntaviseye olarak=" + "izlemesen daha iyi\n\n"
            dosyaya_yazma.write(sonucumuz)
        if toplam_olumlu > toplam_olumsuz:
            sonucumuz = "film adı=" + film_adi + "\ntoplam olumlu yorum saysı=" + "\ntoplam olumsuz yorum sayısı=" + toplam_olumsuz + "\ntoplam olumlu yorum sayısı=" + toplam_olumlu + "\ntaviseye olarak=" + "izlenebilir\n\n"
            dosyaya_yazma.write(sonucumuz)

        dosyaya_yazma.close()  # açılan dosya işlem bittikten sonra kapatılıyor ki bellekte yer kaplamasın.
        print("filmin link adresi=", sayfa)  # hangi filmin yorumunu merak ediyorsak o filme ait web sitesi
        """

        HARF TANIMLAMA YERİ: BU PROGRAMDA EKSİK OLAN ŞEY ALINAN VERİYİ TÜRKÇE KARAKTERLERE DÖNÜŞTÜREMİYOR.

        Ã¶ =ö
        Å=ş
        Ã¼=ü
        Ä±=ı
        Ã§=ç
        Ä=ğ


        """

deger=Analiz()
deger.web_kismi()