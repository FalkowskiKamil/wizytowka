from faker import Faker
fake=Faker()
class BaseContact:
    def __init__(self, imie, nazwisko, telefon, adres_email):
        self.imie=imie
        self.nazwisko=nazwisko
        self.telefon=telefon
        self.adres_email=adres_email
        # Variables
        self._lenght_fullname=0
    def __str___(self):
        return f'{self.imie} {self.nazwisko}'
    def __repr__(self):
        return f'{self.imie} {self.nazwisko} {self.adres_email}'
    def contact(self):
        contact=f'Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}'
        return contact
    @property
    def lenght_fullname(self):
        self._lenght_fullname=len(self.imie) +len(self.nazwisko) +1
        return self._lenght_fullname
    @lenght_fullname.setter
    def lenght_fullname(self,value):
        if value==self._lenght_fullname:
            self._lenght_fullname=value
            return self._lenght_fullname
        else:
            self._lenght_fullname=self._lenght_fullname
            return self._lenght_fullname
class BusinessContact(BaseContact):
    def __init__(self,stanowisko, nazwa_firmy, telefon_sluzbowy,*args,**kwargs,):
        super().__init__(*args, **kwargs)
        self.stanowisko=stanowisko
        self.nazwa_firmy=nazwa_firmy
        self.telefon_sluzbowy=telefon_sluzbowy
    def contact(self):
        contact=f'Wybieran numer {self.telefon_sluzbowy} i dzwonie do {self.imie} {self.nazwisko}'
        return contact
Person1=BaseContact(imie="alfred",nazwisko="reinhold",adres_email="alfredNreinhold@rhyta.com",telefon="+48 123456789")
Person2=BusinessContact(imie="alfred",nazwisko="reinhold",adres_email="alfredNreinhold@rhyta.com",telefon_sluzbowy="+48 987654321",telefon="+48 123456789",stanowisko="student",nazwa_firmy="Kodilla")

def create_contact():
    visitor_type=int(input("Wybierz rodzaj wizytowki: 1=podstawowa, 2=biznesowa: "))
    number_visitor=int(input("Podaj liczbę wizytowek: "))
    if visitor_type==1:
        for x in range(number_visitor):
            Person_name=fake.name()
            Person=BaseContact(imie=Person_name.split()[0], nazwisko=Person_name.split()[1], adres_email=fake.email(),telefon=fake.phone_number())
            print(Person)
    if visitor_type==2:
        for x in range(number_visitor):
            Person_name=fake.name()
            Person=BusinessContact(imie=Person_name.split()[0], nazwisko=Person_name.split()[1], adres_email=fake.email(), telefon_sluzbowy=fake.phone_number(),telefon=fake.phone_number(),stanowisko=fake.job(), nazwa_firmy=fake.company())
            print(Person)
create_contact()