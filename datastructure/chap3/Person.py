import datetime


class Person():
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str)) and sex in ('女', '男'):
            raise PersonValueError(name, sex)
        try:
            birthday = datetime.date(*birthday)
        except:
            raise PersonValueError('Wrong date', birthday)

        self._name = name
        self._sex = sex
        self._birthday = birthday
        self._ident = ident
        Person._num += 1

    def ident(self):
        return self._ident

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonTypeError
        self._name = name

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError
        return self._ident < other.ident()

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return "".join((self._ident, self._name, self._sex, str(self._birthday)))

    def detail(self):
        return ','.join(('编号：' + self._ident,
                         '性别：' + self._sex,
                         '姓名：' + self._name,
                         '出生日期：' + str(self._birthday)))


class Student(Person):
    _id_num = 0

    @classmethod
    def _id_generator(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_generator())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected:", course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def detail(self):
        return ','.join((Person.detail(self),
                         "入学日期：" + str(self._enroll_date),
                         "院系：" + self._department,
                         "课程记录：" + str(self.scores())))


class Stuff(Person):
    _id_num = 0

    @classmethod
    def _id_generator(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Stuff._id_generator(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("wrong date", entry_date)
        else:
            self._entry_date = datetime.date.today()

        self._salary = 1720
        self._department = "未定"
        self._position = "未定"

    def set_salary(self, salary):
        if not isinstance(salary, int):
            raise TypeError
        self._salary = salary

    def set_department(self, department):
        self._department = department

    def set_position(self, position):
        self._position = position

    def detail(self):
        return ','.join((super().detail(),
                         "入职日期：" + str(self._entry_date),
                         "院系：" + self._department,
                         "职位：" + str(self._position),
                         "工资:" + str(self._salary)))


class PersonValueError(ValueError):
    pass


class PersonTypeError(TypeError):
    pass


class Postgraduate(Student):
    _id_num = 0

    def __init__(self, name, sex, birthday, department, major):
        super().__init__(name, sex, birthday, department, Student._id_generator())
        if not isinstance(major, str):
            raise PersonValueError("major Error", major)
        self._major = major

    def detail(self):
        return "".join(Student.detail(),
                       "主修：" + self._major)


class Teacher(Stuff):
    _id_num = 0

    @classmethod
    def _id_generator(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "3{:4}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, teaching, entry_date=None):
        Person.__init__(self, name, sex, birthday, Teacher._id_generator(birthday))
        self._teaching = teaching
        self._salary = 3000
        self._workdays = None
        self._entry_date = entry_date

    def set_wokdays(self, workdays):
        if not isinstance(workdays, int) or workdays > 7 or workdays < 0:
            raise PersonValueError("workday,Error")
        self._workdays = workdays

    def set_salary(self):
        if self._workdays >= 5:
            self._salary += 4000
        elif 3 < self._workdays < 5:
            self._salary += 2500
        else:
            self._salary += 1000

    def detail(self):
        return "".join((Stuff.detail(self),
                        " 教授课程：" + self._teaching))


class Clerk(Stuff):
    _id_num = 0

    @classmethod
    def _id_generator(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "4{:4}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, workfor, entry_date=None):
        Person.__init__(self, name, sex, birthday, Clerk._id_generator(birthday))
        self._workfor = workfor
        self._salary = 2000
        self._workdays = None
        self._entry_date = entry_date

    def set_wokdays(self, workdays):
        if not isinstance(workdays, int) or workdays > 7 or workdays < 0:
            raise PersonValueError("workday,Error")
        self._workdays = workdays

    def set_salary(self):
        if self._workdays >= 5:
            self._salary += 3000
        elif 3 < self._workdays < 5:
            self._salary += 1800
        else:
            self._salary += 900

    def detail(self):
        return "".join((Stuff.detail(self),
                        "工作:"+self._workfor))
p1 = Person("谢阳", '男', (1996, 10, 4), '11514040')
p2 = Person("方润凯", '男', (1998, 9, 14), '11514028')
p3 = Person("张宏", '男', (1997, 1, 16), '11514019')
plist = [p1, p2, p3]
for p in plist:
    print(p.detail())

p4 = Student("谢阳", '男', (1996, 10, 4), '化学')
p5 = Student("方润凯", '男', (1998, 9, 14), '化工')
p6 = Student("张宏", '男', (1997, 1, 16), '哲学')
plist = [p4, p5, p6]
for p in plist:
    print(p.detail())

p7 = Stuff("谢阳", '男', (1996, 10, 4), (2015, 9, 1))
p8 = Stuff("方润凯", '男', (1998, 9, 14), (2015, 10, 1))
p9 = Stuff("张宏", '男', (1997, 1, 16), (2015, 11, 1))
plist = [p7, p8, p9]
for p in plist:
    print(p.detail())

p10 = Teacher("谢阳", '男', (1996, 10, 4), "math", (2015, 9, 1))
p11 = Teacher("方润凯", '男', (1998, 9, 14), "chemistry", (2015, 10, 1))
p12 = Teacher("张宏", '男', (1997, 1, 16), "Chinese", (2015, 11, 1))
p10.set_wokdays(6)
p10.set_salary()
p11.set_wokdays(4)
p11.set_salary()
p12.set_wokdays(2)
p12.set_salary()
plist = [p10, p11, p12]
positions = ["officer", "professor", "president"]
departments = ["化工", "哲学", "数学"]
for p, position, department in zip(plist, positions, departments):
    p.set_position(position)
    p.set_department(department)

    print(p.detail(), "年纪:" + str(p.age()))


p13 = Clerk("谢阳", '男', (1996, 10, 4), "大厨", (2015, 9, 1))
p14 = Clerk("方润凯", '男', (1998, 9, 14), "扫地", (2015, 10, 1))
p15 = Clerk("张宏", '男', (1997, 1, 16), "洗碗", (2015, 11, 1))
p13.set_wokdays(6)
p13.set_salary()
p14.set_wokdays(4)
p14.set_salary()
p15.set_wokdays(2)
p15.set_salary()
plist = [p13, p14, p15]
positions = ["officer", "professor", "president"]
departments = ["化工", "哲学", "数学"]
for p, position, department in zip(plist, positions, departments):
    p.set_position(position)
    p.set_department(department)

    print(p.detail(), "年纪:" + str(p.age()))
