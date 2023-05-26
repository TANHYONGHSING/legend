#Name : Tan Hyong Hsing
#NO MATRIX : 20DDT21F1002

class Booking:
    def __init__(self):
        self.guest_name = input("Please enter your name: ")
        self.no_of_pax = int(input("Please enter no of pack: "))
        self.date_of_booking = input("Please enter the date (dd/mm/yyyy): ")
        self.stay_period = int(input("Please enter staying period: "))

    def display_message(self):
        print(f"This booking is under {self.guest_name} on {self.date_of_booking} for {self.no_of_pax} pack/packs for {self.stay_period} days.")
        
guest_info = Booking()
guest_info.display_message()
