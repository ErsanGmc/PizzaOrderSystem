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

    # Pizza se??imi
    pizza=""
    while pizza=="":
        try:
            choosePizza = int(input("L??tfen bir pizza se??iniz (1-4): "))
            if choosePizza < 1 or choosePizza > 4:
                print("L??tfen ge??erli bir se??im yap??n??z.")
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
            print("L??tfen ge??erli bir say?? giriniz.")
    

    # Sos se??imi
    sauce=""
    while sauce=="":
        try:
            sos_choice = int(input("L??tfen bir sos se??iniz (11-16): Sipari??i Onaylay??p Devam Etmek i??in (0)"))
            if sos_choice < 11 or sos_choice > 16:
                print("L??tfen ge??erli bir se??im yap??n??z.")
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
            print("L??tfen ge??erli bir say?? giriniz.")
    


    total_cost = sauce.get_cost()
    description = sauce.get_description()

    print("Se??ilen pizza: {}".format(pizza.__class__.__name__))
    print("Se??ilen soslar: {}".format(sauce.__class__.__name__))
    print("Toplam fiyat: {} $".format(total_cost))
    print("A????klama: {}".format(description))
    if input("Sipari??i Onayl??yor Musunuz? Evet/Hay??r\n").lower()=="evet":
        name=input("??sminizi Giriniz:")
        tc_no=input("TC Kimlik Numaras?? Giriniz:")
        card_number=input("Kart Numaran??z?? Giriniz:")
        card_pin=input("Kart ??ifrenizi Giriniz:")
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
        print("Sipari?? ba??ar??l??!")
    else:
        print("??yi g??nler ba??ka bir g??n g??r????mek ??zere!")
       
            
if __name__ == "__main__":
    main()
