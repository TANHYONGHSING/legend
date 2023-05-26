# Author : Tan Hyong Hsing (20DDT21F1002)

class customer :
    VIP_member = 0.06
    normal_member = 0.04
    none_member = 0

    def __init__(self,type,total,discount):
        self.type = type
        self.total = total
        self.discount = discount


    def calculation():
        customer.type = input("     Masukan keahlian anda (vip/biasa/tiada) : ")
        customer.total = int(input("            Masukan jumlah bayaran : "))

        if customer.type == "vip" :
            print(f"          Diskaun yang diperolehi    : 6 %")
            discount_price = (customer.total * customer.VIP_member)
            new_total = (customer.total - discount_price)
            print("            Bayaran yang dikenakan : " + str(new_total))
        elif customer.type == "biasa" :
            print(f"          Diskaun yang diperolehi    : 4 %")
            discount_price = (customer.total * customer.normal_member)
            new_total = (customer.total - discount_price)
            print("            Bayaran yang dikenakan : " + str(new_total))
        elif customer.type == "tiada" :
            print(f"          Diskaun yang diperolehi    : 0 %")
            discount_price = (customer.total * customer.none_member)
            new_total = (customer.total - discount_price)
            print("            Bayaran yang dikenakan : " + str(new_total))
        else :
            print("Invalid input")


customer.calculation()
