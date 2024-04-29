class BookingsView:
    def __init__(self, controller):
        self.controller = controller

    def viewBookings(self):
        bookings = self.controller.viewBookings()
        for booking in bookings:
            print(booking.name, booking.numPeople, booking.date, booking.time)

    def placeBooking(self, id, name, numPeople, date, time):
        booking = Booking(id, name, numPeople, date, time)
        self.controller.placeBooking(booking)
        print("Booking placed")

    def rescheduleBooking(self, oldId, newId, name, numPeople, date, time):
        booking = Booking(newId, name, numPeople, date, time)
        self.controller.rescheduleBooking(controller.getBookingById(oldId), booking)
        print("Booking resecheduled")

    def delete(self, id):
        self.controller.cancelBooking(id)
        print("Booking cancelled")

    # Menu for user input
    def run(self):
        while True:
            print("1. View bookings")
            print("2. Get booking by id")
            print("3. Place booking")
            print("4. Reschedule booking")
            print("5. Cancel booking")
            print("6. Quit")
            print("Enter your choice: ", end="")
            choice = int(input())
            if choice == 1:
                self.viewBookings()
            elif choice == 2:
                print("Enter the id of the booking you want to see", end="")
                id = input()
                self.getBookingById(id)
            elif choice == 3:
                print("Enter your booking id, name, party size, date, and time: ", end="")
                details = input().split()
                if len(details) < 5:
                    raise Exception("You must provide all details")
                else:
                    id = details[0]
                    name = details[1]
                    numPeople = int(details[2])
                    date = details[3]
                    time = details[4]
                    self.placeBooking(id, name, numPeople, date, time)
            elif choice == 4:
                print("Enter the id of the booking you want to reschedule")
                oldId = input()
                print("Enter your new booking id, name, party size, date, and time: ", end="")
                details = input().split()
                if len(details) < 5:
                    raise Exception("You must provide all details")
                else:
                    newId = details[0]
                    name = details[1]
                    numPeople = int(details[2])
                    date = details[3]
                    time = details[4]
                    self.rescheduleBooking(oldId, newId, name, numPeople, date, time)
            elif choice == 5:
                print("Enter the id of the booking you want to cancel")
                id = input()
                self.cancelBooking(id)
            elif choice == 6:
                break;
