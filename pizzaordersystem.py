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

    def get_cost(self):
        return self.cost


class MargaritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 8.0

    def get_cost(self):
        return self.cost


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turkish Pizza"
        self.cost = 12.0

    def get_cost(self):
        return self.cost


class SadePizza(Pizza):
    def __init__(self):
        self.description = "Dominos Pizza"
        self.cost = 15.0

    def get_cost(self):
        return self.cost


class Decoator(Pizza):
    def __init__(self, component):
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class ZeytinSos(Decoator):
    def __init__(self, component):
        Decoator.__init__(self, component)
        self.description = "Zeytin"
        self.cost = 1.0


class MantarSos(Decoator):
    def __init__(self, component):
        Decoator.__init__(self, component)
        self.description = "Mantar"
        self.cost = 1.5


class KeciPeyniriSos(Decoator):
    def __init__(self, component):
        Decoator.__init__(self, component)
        self.description = "Keci Peyniri"
        self.cost = 2.0


class EtSos(Decoator):
    def __init__(self, component):
        Decoator.__init__(self, component)
        self.description = "Et"
        self.cost = 2.5


class SoganSos(Decoator):
    def __init__(self, component):
        Decoator.__init__(self, component)
        self.description = "Sogan"
        self.cost = 1.0


class MisirSos(Decoator):
    def __init__(self, component):
        Decoator.__init__(self, component)
        self.description = "Misir"
        self.cost = 1.0


def print_menu():
    with open('menu.txt', 'r') as file:
        data = file.read()
        print(data)


def main():
    menu_file = open("menu.txt", "r")
    print(menu_file.read())
    menu_file.close()

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
    while True:
        sos_list=[]
        try:
            sos_choice = int(input("Lütfen bir sos seçiniz (11-16): "))
            if sos_choice < 11 or sos_choice > 16:
                print("Lütfen geçerli bir seçim yapınız.")

            else:
                break
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
        sos_list.append(sos_choice)

    # Seçilen pizza ve sosların fiyatlarını hesaplama
    if pizza_choice == 1:
        pizza = KlasikPizza()
    elif pizza_choice == 2:
        pizza = MargaritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    else:
        pizza = SadePizza()

    if sos_choice == 11:
        sos = ZeytinSos(pizza)
    elif sos_choice == 12:
        sos = MantarSos(pizza)
    elif sos_choice == 13:
        sos = KeciPeyniriSos(pizza)
    elif sos_choice == 14:
        sos = EtSos(pizza)
    elif sos_choice == 15:
        sos = SoganSos(pizza)
    else:
        sos = MisirSos(pizza)

    total_cost = sos.get_cost()
    description = sos.get_description()

    print("Seçilen pizza: {}".format(pizza.__class__.__name__))
    print("Seçilen sos: {}".format(sos.__class__.__name__))
    print("Toplam fiyat: {} TL".format(total_cost))
    print("Açıklama: {}".format(description))
    if input("Siparişi Onaylıyor Musunuz? Evet/Hayır").lower()=="evet":
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
            writer.writeheader()
            writer.writerow(order)
        print("Sipariş başarılı!")
    else:
        print("İyi günler başka bir gün görüşmek üzere!")
       
            
if __name__ == "__main__":
    main()
