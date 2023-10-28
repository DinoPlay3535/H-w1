class Worker:
    def __init__(self, name, work, salary=1000, age=18):
        self.name = name
        self.work = work
        self.salary = salary
        self.age = age

    def printer(self):
        print(self.name, self.work, self.salary, self.age)

    def earn(self, salary = 1):
        self.salary += salary

    def grow(self, age = 1):
        self.age += age

kevin = Worker(name="Kevin", work="Programmer", salary=5000, age=23)

kevin.printer()
kevin.earn(1200)
kevin.grow(2)
kevin.printer()