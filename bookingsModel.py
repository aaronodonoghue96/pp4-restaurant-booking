class BookingsModel:
    def __init__(self):
        self.bookings = []

    def placeBooking(self, booking):
        self.bookings.append(booking)

    def viewBookings(self):
        return self.bookings

    def getBookingById(self, bookingId):
        for booking in self.bookings:
            if booking.id == bookingId:
                return booking
        return None

    def update(self, old_booking, new_booking):
        self.delete(old_booking.id)
        self.add(new_booking)
        raise Exception("No booking to update was found")

    def delete(self, bookingId):
        for b in self.bookings:
            if b.id == bookingId:
                self.bookings.remove(b)
                return
        raise Exception("No booking to delete was found")
