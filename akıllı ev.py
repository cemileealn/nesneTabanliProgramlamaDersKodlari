class Cihazlar:
    def __init__(self, ad):
        self.ad = ad
        self.acik_mi = False

    def ac(self):
        self.acik_mi = True
        print(f"{self.ad} cihazı açıldı.")

    def kapa(self):
        self.acik_mi = False
        print(f"{self.ad} cihazı kapandı.")


class Isiklar(Cihazlar):
    def __init__(self, ad, parlaklik=0):
        super().__init__(ad)
        self.parlaklik = parlaklik

    def parlaklik_ayarla(self, parlaklik):
        if 0 <= parlaklik <= 100:
            self.parlaklik = parlaklik
            print(f"{self.ad} ışığının parlaklık seviyesi {self.parlaklik} olarak ayarlandı.")
        else:
            print("Parlaklık değeri 0 ile 100 arasında olmalıdır. Lütfen tekrar deneyiniz!")


class Klima(Cihazlar):
    def __init__(self, ad, sicaklik=20):
        super().__init__(ad)
        self.sicaklik = sicaklik

    def sicaklik_ayarla(self, sicaklik):
        if 16 <= sicaklik <= 30:
            self.sicaklik = sicaklik
            print(f"{self.ad} klimasının sıcaklık değeri {self.sicaklik}°C olarak ayarlandı.")
        else:
            print("Yanlış sıcaklık seçimi. Sıcaklık 16 ile 30 arasında olmalıdır. Lütfen tekrar deneyiniz!")


class GuvenlikKamerasi(Cihazlar):
    def __init__(self, ad):
        super().__init__(ad)


class AkilliEv:
    def __init__(self, adres):
        self.adres = adres
        self.cihazlar = []

    def cihaz_ekle(self, cihaz):
        self.cihazlar.append(cihaz)
        print(f"Seçmiş olduğunuz {cihaz.ad} cihazı eklendi.")

    def cihaz_sil(self, cihaz):
        self.cihazlar.remove(cihaz)
        print(f"Seçmiş olduğunuz {cihaz.ad} cihazı silindi.")


ev = AkilliEv("Malatya, Battalgazi")

isik1 = Isiklar("Oda Işığı", 34)
ev.cihaz_ekle(isik1)

klima1 = Klima("Oda Kliması", 24)
ev.cihaz_ekle(klima1)

kamera1 = GuvenlikKamerasi("Güvenlik Kamerası")
ev.cihaz_ekle(kamera1)

isik1.ac()
isik1.parlaklik_ayarla(76)

klima1.ac()
klima1.sicaklik_ayarla(21)