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

    def rescheduleBooking(self, id, name, numPeople, date, time):
        booking = Booking(id, name, numPeople, date, time)
        self.controller.rescheduleBooking()
        print("Booking resecheduled")

    def delete(self, id):
        self.controller.cancelBooking(id)
        print("Booking cancelled")

    # Menu for user input
    def run(self):
        while True:
            print("1. Get all persons")
            print("2. Get person by id")
            print("3. Add person")
            print("4. Update person")
            print("5. Delete person")
            print("6. Get person by name")
            print("7. Filter person by age")
            print("8. Exit")
            print("Enter your choice: ", end="")
            choice = int(input())
            if choice == 1:
                self.viewBookings()
            elif choice == 2:
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
