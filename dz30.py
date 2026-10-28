class Employee:
    def __init__(self, name):
        self.__name = name
        self.__jobs = []

    @property
    def name(self):
        return self.__name

    @property
    def jobs(self):
        return self.__jobs

    def add_job(self, job):
        self.__jobs.append(job)

    def display_info(self):
        print(f"Name: {self.__name}")


class Faculty:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Job:
    def __init__(self, title, company):
        self.__title = title
        self.__company = company


class Student:
    def __init__(self, name, faculty):
        self.__name = name
        self.__faculty = faculty

    @property
    def name(self):
        return self.__name

    @property
    def faculty(self):
        return self.__faculty


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.__subordinates = []

    def add_subordinate(self, employee):
        self.__subordinates.append(employee)

    def display_subordinates(self):
        for emp in self.__subordinates:
            print(f"  - {emp.name}")


class Inter(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.__mentor = None

    def set_mentor(self, mentor):
        self.__mentor = mentor

    def get_mentor(self):
        return self.__mentor


if __name__ == "__main__":
    john = Employee(name="John")
    bob = Inter(name="Bob")
    bob.set_mentor(john)
    print(bob.get_mentor().name)        

    alice = Manager(name="Alice")
    alice.add_subordinate(john)
    alice.add_subordinate(bob)
    alice.display_subordinates()