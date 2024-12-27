class Film:
    def __init__(self, ad, tur, cikis_yili):
        self.ad = ad
        self.tur = tur
        self.cikis_yili = cikis_yili

    def __str__(self):
        return f"{self.ad} ({self.cikis_yili}) - Tür: {self.tur}"


class Kullanici:
    def __init__(self, isim):
        self.isim = isim
        self.izlenen_filmler = []

    def film_izle(self, film):
        if film not in self.izlenen_filmler:
            self.izlenen_filmler.append(film)
            print(f"{film.ad} izlenmiş olarak işaretlendi.")
        else:
            print(f"{film.ad} zaten izlenmiş.")

    def izlenen_filmleri_goster(self):
        if self.izlenen_filmler:
            print(f"{self.isim} tarafından izlenen filmler:")
            for film in self.izlenen_filmler:
                print(f" - {film}")
        else:
            print(f"{self.isim} henüz hiç film izlemedi.")


class Arsiv:
    def __init__(self):
        self.filmler = []

    def film_ekle(self, film):
        self.filmler.append(film)
        print(f"{film.ad} arşive eklendi.")

    def film_sil(self, film):
        if film in self.filmler:
            self.filmler.remove(film)
            print(f"{film.ad} arşivden silindi.")
        else:
            print(f"{film.ad} arşivde bulunamadı.")

    def tum_filmleri_goster(self):
        if self.filmler:
            print("Arşivdeki tüm filmler:")
            for film in self.filmler:
                print(f" - {film}")
        else:
            print("Arşive henüz film eklenmemiş.")


arsiv = Arsiv()

film1 = Film("Matrix", "Bilim Kurgu", 1999)
film2 = Film("Inception", "Bilim Kurgu", 2010)
film3 = Film("Forrest Gump", "Drama", 1994)

arsiv.film_ekle(film1)
arsiv.film_ekle(film2)
arsiv.film_ekle(film3)

arsiv.tum_filmleri_goster()

kullanici = Kullanici("Cemile Kevser")

kullanici.film_izle(film1)
kullanici.film_izle(film2)

kullanici.izlenen_filmleri_goster()