class BookingsController:
    def __init__(self, model):
        self.model = model

    def viewBookings(self):
        return self.model.viewBookings()

    def placeBooking(self, booking):
        self.model.placeBooking(booking)

    def rescheduleBooking(self, old_booking, new_booking):
        self.model.rescheduleBooking(old_booking, new_booking)

    def cancelBooking(self, bookingId):
        self.model.cancelBooking(bookingId)
