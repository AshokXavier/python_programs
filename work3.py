print("--- BUS TICKET BOOKING SYSTEM ---")
seats=[1,2,3,4,5,6,7,8,9,10]
price = 500

while(True):
  print("1. Book Ticket\n2. View Seat Availability\n3. Cancel Ticket\n4. Exit\n")
  choice=int(input("Enter your choice: "))
  
  if choice==1:
    if len(seats) == 0:
      print("Sorry! No seats available.")
      continue
    passenger_name=input("Enter Passenger Name: ")
    passenger_age=int(input("Enter Passenger Age: "))
    print("Available Seats: ")
    for i in range(len(seats)):
      print(seats[i],end=" ")
    print()
    while(True):

      seat_number=int(input("Enter Seat Number: "))
      if seat_number in seats:
        print("Seat Available")
        seats.remove(seat_number)
        break
      else:
        print("Seat not available")
    if passenger_age<12:
      price = 300
      print("Child Discount Applied")
    elif passenger_age>60:
      price = 350
      print("Senior Citizen Discount Applied")

    print("Ticket Booked Sucesfully")
    print(passenger_name)
    print(seat_number)
    print("Final Ticket Price:", price)

  elif choice==2:
    for i in range(len(seats)):
      print(seats[i],end=" ")
    print()

  elif choice==3:
    cancel_ticket=int(input("Enter the ticket to be cancelled: "))
    if cancel_ticket not in seats:
      print("Cancel The Booking")
      print("Ticket Cancelled succesfully")
      seats.append(cancel_ticket)
      seats.sort()
    else:
      print("Seat is already available")

  elif choice==4:
    print("Thank you for choosing Bus Ticket Booking System.")
    break

  else:
    print("Wrong Choice")
    

