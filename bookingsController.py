class BookingsController:
    def __init__(self, model):
        self.model = model

    def viewBookings(self):
        return self.model.viewBookings()

    def getBookingById(self, id):
        self.model.getBookingById(id);

    def placeBooking(self, booking):
        self.model.placeBooking(booking)

    def rescheduleBooking(self, old_booking, new_booking):
        self.model.rescheduleBooking(old_booking, new_booking)

    def cancelBooking(self, bookingId):
        self.model.cancelBooking(bookingId)
