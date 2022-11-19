from faker import Faker
fake=Faker()

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name=name
        self.surname=surname
        self.phone=phone
        self.email=email

        self.label_lenght=len(self.name) +len(self.surname)

    def __str___(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.surname} {self.email}'

    def contact(self):
        contact=f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}'
        return contact
        
    def label_lenght(self):
        return self.label_lenght
   
class BusinessContact(BaseContact):
    def __init__(self,position, company, phone_business,*args,**kwargs,):
        super().__init__(*args, **kwargs)
        self.positon=position
        self.company=company
        self.phone_business=phone_business
    
    def contact(self):
        contact=f'Wybieran numer {self.phone_business} i dzwonie do {self.name} {self.surname}'
        return contact

person1=BaseContact(name="alfred",surname="reinhold",email="alfredNreinhold@rhyta.com",phone="+48 123456789")
person2=BusinessContact(name="alfred",surname="reinhold",email="alfredNreinhold@rhyta.com",phone_business="+48 987654321",phone="+48 123456789",position="student",company="Kodilla")

def create_contact(card_type, number_of_cards):
    cards=list()
    if card_type=="base":
        for x in range(number_of_cards):
            person_name=fake.name()
            person=BaseContact(name=person_name.split()[0], surname=person_name.split()[1], email=fake.email(),phone=fake.phone_number())
            cards.append(person)

    if card_type=="business":
        for x in range(number_of_cards):
            person_name=fake.name()
            person=BusinessContact(name=person_name.split()[0], surname=person_name.split()[1], email=fake.email(), phone_business=fake.phone_number(),phone=fake.phone_number(),position=fake.job(), company=fake.company())
            cards.append(person)

create_contact(card_type="business",number_of_cards=4)