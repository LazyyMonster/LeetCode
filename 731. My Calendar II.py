class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlapping = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not(start >= e or end <= s):
                return False
            
        for s, e in self.bookings:
            if not(start >= e or end <= s):
                self.overlapping.append((max(start, s), min(end, e)))

        self.bookings.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)s