class Rational():
    @staticmethod
    def _gcd(m, n):
        '''求最大公约数'''
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n

    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, float):
            (numerator, denominator) = numerator.as_integer_ratio()
        # 检查传入参数是否为整数
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        if denominator == 0:
            raise ZeroDivisionError
        sign = 1  # 符号，正负性
        if numerator < 0:
            numerator, sign = -numerator, -sign
        if denominator < 0:
            denominator, sign = -denominator, -sign
        g = Rational._gcd(numerator, denominator)

        self._numerator = sign * numerator // g
        self._denominator = denominator // g

    def numerator(self):
        return self._numerator

    def denominator(self):
        return self._denominator

    def __add__(self, other):
        '''加法'''
        denominator = self._denominator * other.denominator()
        numerator = self._numerator * other.denominator() + self._denominator * other.numerator()
        return Rational(numerator, denominator)

    def __sub__(self, other):
        '''减法'''
        denominator = self._denominator * other.denominator()
        numerator = self._numerator * other.denominator() - self._denominator * other.numerator()
        return Rational(numerator, denominator)

    def __mul__(self, other):
        denominator = self._denominator * other.denominator()
        numerator = self._numerator * other.numerator()
        return Rational(numerator, denominator)

    def __floordiv__(self, other):
        '''地板除'''
        if other.numerator() == 0:
            raise ZeroDivisionError
        return Rational(self._numerator * other.denominator(), self._denominator * other.numerator())

    def __lt__(self, other):
        '''小于'''
        if (self - other).numerator() < 0:
            return True
        return False

    def __gt__(self, other):
        '''大于'''
        if (self - other).numerator() > 0:
            return True
        return False

    def __eq__(self, other):
        '''等于'''
        if (self - other).numerator() == 0:
            return True
        return False

    def __le__(self, other):
        '''小于等于'''
        if (self - other).numerator() <= 0:
            return True
        return False

    def __ge__(self, other):
        '''大于等于'''
        if (self - other).numerator() >= 0:
            return True
        return False

    def __ne__(self, other):
        '''不等于'''
        if (self - other).numerator() != 0:
            return True
        return False

    def to_int(self):
        return self._numerator // self._denominator

    def to_float(self):
        return self._numerator / self._denominator

    def __str__(self):
        return str(self._numerator) + '/' + str(self._denominator)


a = Rational(1, 3)
b = Rational(1, 4)
print(a.to_int())
print(b.to_float())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a < b)
print(a > b)
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)
c = Rational(4.5)
print(c)
