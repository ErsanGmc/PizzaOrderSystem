import csv
import datetime

class Pizza:
    def __init__(self):
        self.cost=0
        self.description = "Unknown Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class KlasikPizza(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.cost = 10.0
    def get_description(self):
        return super().get_description()
    def get_cost(self):
        return super().get_cost()


class MargaritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 8.0

    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turkish Pizza"
        self.cost = 12.0

    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()


class SadePizza(Pizza):
    def __init__(self):
        self.description = "Dominos Pizza"
        self.cost = 15.0

    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class ZeytinSos(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Zeytin"
        self.cost = 1.0


class MantarSos(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mantar"
        self.cost = 1.5


class KeciPeyniriSos(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Keci Peyniri"
        self.cost = 2.0


class EtSos(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Et"
        self.cost = 2.5


class SoganSos(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Sogan"
        self.cost = 1.0


class MisirSos(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Misir"
        self.cost = 1.0
def print_menu():
    with open('menu.txt', 'r') as file:
        data = file.read()
        print(data)


def main():
    print_menu()

    # Pizza seçimi
    while True:
        try:
            pizza_choice = int(input("Lütfen bir pizza seçiniz (1-4): "))
            if pizza_choice < 1 or pizza_choice > 4:
                print("Lütfen geçerli bir seçim yapınız.")
            else:
                break
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    # Sos seçimi
    sos_list=[]
    while True:
        try:
            sos_choice = int(input("Lütfen bir sos seçiniz (11-16): Siparişi Onaylayıp Devam Etmek için (0)"))
            if sos_choice==0:
                break
            elif sos_choice < 11 or sos_choice > 16:
                print("Lütfen geçerli bir seçim yapınız.")
            else:
                sos_list.append(sos_choice)
                continue
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
    print(sos_list)
    while sos_choice==0:
    # Seçilen pizza ve sosların fiyatlarını hesaplama
        if pizza_choice == 1:
            pizza = KlasikPizza()
            break
        elif pizza_choice == 2:
            pizza = MargaritaPizza()
            break
        elif pizza_choice == 3:
            pizza = TurkPizza()
            break
        else:
            pizza = SadePizza()
            break

    pizza_base=pizza.get_cost()
    sos_cost=0
    sos_description=""
    for element in sos_list:
            if element == 11:
                sos_cost += ZeytinSos(pizza).cost
                sos_description+=" "+ZeytinSos(pizza).description
            elif element == 12:
                sos_cost += MantarSos(pizza).cost
                sos_description+=" "+MantarSos(pizza).description
                
            elif element == 13:
                sos_cost += KeciPeyniriSos(pizza).cost
                sos_description+=" "+KeciPeyniriSos(pizza).description

            elif element == 14:
                sos_cost += EtSos(pizza).cost
                sos_description+=" "+EtSos(pizza).description

            elif element == 15:
                sos_cost += SoganSos(pizza).cost
                sos_description+=" "+SoganSos(pizza).description

            else:
                sos_description+=" "+MisirSos(pizza).description
                sos_cost +=MisirSos(pizza).cost

    total_cost = pizza_base+sos_cost
    description = pizza.get_description()+sos_description

    print("Seçilen pizza: {}".format(pizza.__class__.__name__))
    print("Seçilen soslar: {}".format(sos_description))
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
            "Order Time":datetime.datetime.now(),
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
