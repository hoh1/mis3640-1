class Time:
    """
    Represents the time of day.

    attributes: hour, minute, second
    """

    def print_time(self):
        """Prints a string representation of the time."""
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 0
start.print_time()
print(start.time_to_int())

end = start.increment(2000)
end.print_time()
print(end.is_after(start))
