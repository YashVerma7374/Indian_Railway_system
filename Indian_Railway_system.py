# Defining variable for Indian railway system

# train_name= "Rajdhani express"
# train_NO = 12301
# ticket_price = 2450.50
# is_AC_Available = True
# seat_NO = [1,2,3,4,5]

# Showing the details using print function

# print("Train Name:- ",train_name)
# print("Train NO:- ",train_NO)
# print("Ticket Price:- ",ticket_price)
# print("AC Availablety:- ",is_AC_Available)
# print("SEAT NO:- ",seat_NO)

# # showing tha data types of variables using function

# print("The data type of Train Name: ",type(train_name))
# print("The data type of Train number: ",type(train_NO))
# print("The data type of Ticket price: ",type(ticket_price))
# print("The data type of AC availablety: ",type(is_AC_Available))
# print("The data type of SEAT NO: ",type(seat_NO))

# Getting passengrer information

# print("=== iNDAIN RAILWAYS BOOKING SYSTEM ===")
# passenger_name = input("Enter Your Name:- ")
# age = int(input("Enter age:- "))
# destination = input("Enter destination : ")

# # Displaying booking Conformation

# print("\n === Booking Details ===")
# print(f"Passenger : {passenger_name}")
# print(f"Age : {age }")
# print(f"destination : {destination}")
# print("!!!Booking confirmed!!!")


# base_price = 1500
# service_charge = 100
# total_price = base_price + service_charge
# print(f"Base Price : ₹{base_price}")
# print(f"Service Charge : ₹{service_charge}")
# print(f"Total Price : ₹{total_price}")

# # comparision operator

# passenger_age = 25
# senior_citizen = 60
# is_senior = passenger_age >= senior_citizen

# print(f"\n Is passenger senior citizen? {is_senior}🙁")


# logical operator

# has_ticket = True
# has_id_proof = False
# can_board = has_ticket and has_id_proof

# print(f"\n Can Board Train? {can_board}")

# # control flow IF statement

# Age = int(input ("Enter Passenger Age:  "))

# if Age < 5:
#     price = 0
#     category = "infant (Free)"
# elif  Age < 12:
#     price = 750
#     category = "Chid (50% Discount)"
# elif Age > 60:
#     price = 1200
#     category = "Senior Citizen (20% Discount)"
# else:
#     price = 1500
#     category = "Adult"

# print(f"Category : {category}")
# print(f"Ticket price :₹ {price}")

# for loop - Display avilable trains

# trains =[
#     {"name": "Rajdhani Express","Number": 12301,"destination": "New delhi"},
#     {"name": "Hawrah Express","Number": 12801,"destination": "Hawrah"},
#     {"name": "Decan Express","Number": 12108,"destination": "Nagpur"},
#     {"name": "ADI tejas Express","Number": 14802,"destination": "Ahemdabad"},
#     {"name": "Koyna Express","Number": 18030,"destination": "Pune"},
#     {"name": "Madgaon Express","Number": 22050,"destination": "goa"},
#     {"name": "Gitanjali Express","Number": 11235,"destination": "Mumbai"},
# ]

# print("Available Trains: ")
# for train in trains:
#     print(f"{train['Number']}-{train['name']} to {train['destination']}")

# While loop - booking system menu

print("\n=== booking menu ===")
choice = 0

while choice != 3:
    print("1. Book Ticket")
    print("2. Check Status")
    print("3. exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Booking ticket ............\n")
    elif choice == 2:
        print("checking status\n")
    elif choice == 3:
         print("Thank you for using Indian Railways!!!\n")
    else:
        print("\nInvalid Choice!\n")

