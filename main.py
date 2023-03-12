import csv
import datetime

class Pizza:
    def __init__(self):
        self.cost=0.0
        self.description = ""

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class KlasikPizza(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
        self.cost = 10.0


class MargaritaPizza(Pizza):
    def __init__(self):
        self.description = "Margarita Pizza"
        self.cost = 8.0


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turkish Pizza"
        self.cost = 12.0



class SadePizza(Pizza):
    def __init__(self):
        self.description = "Dominos Pizza"
        self.cost = 15.0

class Decorator(Pizza):
    def __init__(self, sauces):
        self.sauces = sauces
        
    def get_cost(self):
        return self.sauces.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        
        return self.sauces.get_description() + ':' + Pizza.get_description(self)


class ZeytinSos(Decorator):
    def __init__(self, sauces):
        self.sauces=sauces
        self.description = "Zeytin"
        self.cost = 1.0


class MantarSos(Decorator):
    def __init__(self, sauces):
        self.sauces=sauces
        self.description = "Mantar"
        self.cost = 1.5


class KeciPeyniriSos(Decorator):
    def __init__(self, sauces):
        self.sauces=sauces
        self.description = "Keci Peyniri"
        self.cost = 2.0


class EtSos(Decorator):
    def __init__(self, sauces):
        self.sauces=sauces
        self.description = "Et"
        self.cost = 2.5


class SoganSos(Decorator):
    def __init__(self, sauces):
        self.sauces=sauces
        self.description = "Sogan"
        self.cost = 1.0


class MisirSos(Decorator):
    def __init__(self, sauces):
        self.sauces=sauces
        self.description = "Misir"
        self.cost = 1.0
def print_menu():
    with open('menu.txt', 'r') as file:
        data = file.read()
        print(data)
def menu_write():
    with open('menu.txt',mode='w') as file:
        menu="* Please Choose Pizza Base: \n1: Klasik\n2: Margarita\n3: TurkPizza\n4: Sade Pizza\n* ve sececeginiz sos:\n11: Zeytin\n12: Mantarlar\n13: Keci Peyniri\n14: Et\n15: Sogan\n16: Misir\n\n* Tesekkur ederiz!"
        file.write(menu)

def main():
    menu_write()
    print_menu()

    # Pizza seçimi
    pizza=""
    while pizza=="":
        try:
            choosePizza = int(input("Lütfen bir pizza seçiniz (1-4): "))
            if choosePizza < 1 or choosePizza > 4:
                print("Lütfen geçerli bir seçim yapınız.")
            else:
                if choosePizza == 1:
                    pizza = KlasikPizza()
                    
                elif choosePizza == 2:
                    pizza = MargaritaPizza()
                    
                elif choosePizza == 3:
                    pizza = TurkPizza()
                    
                else:
                    pizza = SadePizza()
                    
                
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
    

    # Sos seçimi
    sauce=""
    while sauce=="":
        try:
            sos_choice = int(input("Lütfen bir sos seçiniz (11-16): Siparişi Onaylayıp Devam Etmek için (0)"))
            if sos_choice < 11 or sos_choice > 16:
                print("Lütfen geçerli bir seçim yapınız.")
            else:
                if sos_choice == 11:
                    sauce = ZeytinSos(pizza)                   
                elif sos_choice == 12:
                    sauce = MantarSos(pizza)                   
                elif sos_choice == 13:
                    sauce = KeciPeyniriSos(pizza)               
                elif sos_choice == 14:
                    sauce = EtSos(pizza)                  
                elif sos_choice == 15:
                    sauce = SoganSos(pizza)      
                elif sos_choice == 16:
                    sauce = MisirSos(pizza)
                           
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
    


    total_cost = sauce.get_cost()
    description = sauce.get_description()

    print("Seçilen pizza: {}".format(pizza.__class__.__name__))
    print("Seçilen soslar: {}".format(sauce.__class__.__name__))
    print("Toplam fiyat: {} $".format(total_cost))
    print("Açıklama: {}".format(description))
    if input("Siparişi Onaylıyor Musunuz? Evet/Hayır\n").lower()=="evet":
        name=input("İsminizi Giriniz:")
        tc_no=input("TC Kimlik Numarası Giriniz:")
        card_number=input("Kart Numaranızı Giriniz:")
        card_pin=input("Kart Şifrenizi Giriniz:")
        order={
            "Username":name,
            "TC":tc_no,
            "Card Number":card_number,
            "Order Description":description,
            "Order Time":datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Card Pin":card_pin
        }
        with open('Orders_Database.csv', mode='a', newline='') as file:
            filednames=['Username','TC','Card Number','Order Description','Order Time','Card Pin']
            writer=csv.DictWriter(file,fieldnames=filednames)
            writer.writerow(order)
        print("Sipariş başarılı!")
    else:
        print("İyi günler başka bir gün görüşmek üzere!")
       
            
if __name__ == "__main__":
    main()
