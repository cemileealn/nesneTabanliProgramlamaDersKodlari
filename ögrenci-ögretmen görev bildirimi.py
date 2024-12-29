from abc import ABC, abstractmethod

# Soyut sınıf
class Kullanici(ABC):  # User yerine Kullanici
    def __init__(self, ad, kimlik_no):
        self.ad = ad
        self.__kimlik_no = kimlik_no  # kimlik_no bilgisi gizli (encapsulation)

    def kimlik_no_al(self):  # get_id yerine kimlik_no_al
        return self.__kimlik_no

    @abstractmethod
    def tanit(self):  # introduce yerine tanit
        pass

    @abstractmethod
    def gorev(self):  # task yerine gorev
        pass

# Ogrenci sınıfı
class Ogrenci(Kullanici):  # Student yerine Ogrenci
    def __init__(self, ad, kimlik_no, notu):
        super().__init__(ad, kimlik_no)
        self.notu = notu

    def tanit(self):  # Soyut metodu dolduruyoruz
        return f"Benim adım {self.ad}. Kimlik numaram {self.kimlik_no_al()} ve öğrenciyim."

    def gorev(self):  # Soyut metodu dolduruyoruz
        return f"Derslerime çalışıyorum ve notum: {self.notu}."

# Ogretmen sınıfı
class Ogretmen(Kullanici):  # Teacher yerine Ogretmen
    def __init__(self, ad, kimlik_no, ders):
        super().__init__(ad, kimlik_no)
        self.ders = ders

    def tanit(self):  # Soyut metodu dolduruyoruz
        return f"Benim adım {self.ad}. Kimlik numaram {self.kimlik_no_al()} ve öğretmenim."

    def gorev(self):  # Soyut metodu dolduruyoruz
        return f"{self.ders} dersini öğretiyorum."

# Test kodu
ogrenci = Ogrenci("Ali", 12345, "A")  # Student yerine Ogrenci nesnesi
ogretmen = Ogretmen("Ayşe", 67890, "Matematik")  # Teacher yerine Ogretmen nesnesi

print(ogrenci.tanit())
print(ogrenci.gorev())
print(ogretmen.tanit())
print(ogretmen.gorev())
