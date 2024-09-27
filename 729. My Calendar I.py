class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:

        for bookedStart, bookedEnd in self.bookings:
            if start < bookedEnd and end > bookedStart:
                return False
        self.bookings.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)