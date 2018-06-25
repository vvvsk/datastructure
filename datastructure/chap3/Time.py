# codeing:UTF-8
class Time():
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def hours(self):
        return self._hours

    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._seconds

    def __add__(self, other):
        '''时间之减法'''
        seconds = self._seconds + other.seconds()
        minutes = self._minutes + other.minutes()
        hours = self._hours + other.hours()
        if seconds >= 60:
            seconds -= 60
            minutes += 1
        if minutes >= 60:
            minutes -= 60
            hours += 1
        if hours >= 24:
            hours -= 24
        return Time(hours, minutes, seconds)

    def __sub__(self, other):
        '''时间之减法'''
        seconds = self._seconds - other.seconds()
        minutes = self._minutes - other.minutes()
        hours = self._hours - other.hours()
        if seconds < 0:
            seconds += 60
            minutes -= 1
        if minutes < 0:
            minutes += 60
            hours -= 1
        if hours < 0:
            raise ValueError
        return Time(hours, minutes, seconds)

    def __lt__(self, other):
        '''比较时间'''
        try:
            time = self - other
        except ValueError:
            return True
        return False

    def __eq__(self, other):
        '''时间相等判断'''
        if self._hours == other.hours and self._minutes() == other.minutes() and self._seconds == other.seconds():
            return True
        else:
            return False

    def __str__(self):
        return str(self._hours) + ':' + str(self._minutes) + ':' + str(self._seconds)


a = Time(10, 49, 20)
b = Time(20, 20, 42)
print(a + b)
print(b - a)
# print(a - b)
print(a < b)
print(a == b)
