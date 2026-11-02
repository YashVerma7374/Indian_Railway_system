# Defining variable for Indian railway system

train_name= "Rajdhani express"
train_NO = 12301
ticket_price = 2450.50
is_AC_Available = True
seat_NO = [1,2,3,4,5]

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

print("=== iNDAIN RAILWAYS BOOKING SYSTEM ===")
passenger_name = input("Enter Your Name:- ")
age = int(input("Enter age:- "))
destination = input("Enter destination : ")

# Displaying booking Conformation

print("\n === Booking Details ===")
print(f"Passenger : {passenger_name}")
print(f"Age : {age }")
print(f"destination : {destination}")
print("!!!Booking confirmed!!!")
