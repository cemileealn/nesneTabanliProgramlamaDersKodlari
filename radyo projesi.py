class Radyo:
    def __init__(self):
        self.acik = False  # Radyo kapalı olarak başlar
        self.ses = 50      # Varsayılan ses seviyesi 50
        self.istasyon = "101.1"  # Varsayılan istasyon

    def radyo_ac(self):
        if not self.acik:
            self.acik = True
            print("Radyo açıldı.")
        else:
            print("Radyo zaten açık.")

    def radyo_kapat(self):
        if self.acik:
            self.acik = False
            print("Radyo kapatıldı.")
        else:
            print("Radyo zaten kapalı.")

    def ses_arttir(self):
        if self.acik:
            if self.ses < 100:
                self.ses += 1
                print(f"Ses artırıldı: {self.ses}")
            else:
                print("Ses zaten maksimum seviyede.")
        else:
            print("Ses ayarı yapmak için önce radyoyu açmalısınız.")

    def ses_azalt(self):
        if self.acik:
            if self.ses > 1:
                self.ses -= 1
                print(f"Ses azaltıldı: {self.ses}")
            else:
                print("Ses zaten minimum seviyede.")
        else:
            print("Ses ayarı yapmak için önce radyoyu açmalısınız.")

    def istasyon_degistir(self, yeni_istasyon):
        if self.acik:
            self.istasyon = yeni_istasyon
            print(f"İstasyon değiştirildi: {self.istasyon}")
        else:
            print("İstasyon değiştirmek için önce radyoyu açmalısınız.")

# Radyo Kullanımı
radyo = Radyo()

radyo.radyo_ac()         # Radyo açılır
radyo.ses_arttir()       # Ses artırılır
radyo.ses_azalt()        # Ses azaltılır
radyo.istasyon_degistir("95.8")  # İstasyon değiştirilir
radyo.radyo_kapat()      # Radyo kapatılır
